import folium
import pandas

geojsonmap=f'Map/cb_2018_us_state_500k.geojson'
data=pandas.read_json('https://covidtracking.com/api/v1/states/current.json')
df=pandas.DataFrame(data)

df2=pandas.read_csv("Map/us-state-capitals.csv")
df2.set_index('name', inplace=True)

df1=df.copy()
df1.set_index('state', inplace=True)
df1=df1.drop(['AS', 'DC', 'GU', 'MP', 'PR', 'VI'])
df1['statename']=["Alaska","Alabama","Arkansas","Arizona","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Iowa","Idaho","Illinois",
  "Indiana","Kansas","Kentucky","Louisiana","Massachusetts","Maryland","Maine",
  "Michigan","Minnesota","Missouri","Mississippi","Montana","North Carolina","North Dakota",
  "Nebraska","New Hampshire","New Jersey","New Mexico","Nevada","New York",
  "Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Virginia","Vermont","Washington","Wisconsin","West Virginia","Wyoming"]
df1.sort_values(by='statename',ascending=True,inplace=True)
df1['states']=df1.index

df2=pandas.read_csv("Map/us-state-capitals.csv")
df2.set_index('name', inplace=True)
df2['population']=[4833722, 735132, 6626624, 2959373, 38332521, 5268367, 3596080, 925749, 19552860, 9992167, 1404054, 1612136, 12882135, 6570902,
3090416, 2893957, 4395295, 4625470, 1328302, 5928814, 6692824, 9895622, 5420380, 2991207, 6044171, 1015165, 1868516, 2790136, 1323459, 8899339, 2085287, 19651127, 9848060, 723393, 11570808, 3850568,
3930065, 12773801, 1051511, 4774839, 844877, 6495978, 26448193, 2900872, 626630, 8260405, 6971406, 1854304, 5742713, 582658]

m = folium.Map(location=[39.8283, -95.5795], zoom_start=4)
d = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

casespo=[]
for cases, population in zip(df1['positive'], df2['population']):
    cpo=((cases*100000)/population)
    casespo.append(cpo)

df1['casespo']=casespo

deathspo=[]
for deaths, population in zip(df1['death'], df2['population']):
    dpo=((deaths*100000)/population)
    deathspo.append(dpo)

df1['deathspo']=deathspo

folium.Choropleth(
    geo_data=geojsonmap,
    name='Cases per 100,000 Citizens',
    data=df1,
    columns=['states', 'casespo'],
    key_on='feature.properties.STUSPS',
    fill_color='OrRd',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Cases Per 100,000 Citizens'
).add_to(m)

folium.Choropleth(
    geo_data=geojsonmap,
    name='Deaths per 100,000 Citizens',
    data=df1,
    columns=['states', 'deathspo'],
    key_on='feature.properties.STUSPS',
    fill_color='OrRd',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Deaths per 100,000 Citizens'
).add_to(d)

for sn, sa in zip(df2.index, df1.index):
    popup="""
    {0}
    Cases per 100K: {1}
    Deaths per 100K: {2}
    """.format(sn, int(df1.loc[sa]['casespo']), int(df1.loc[sa]['deathspo']))

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='white', color='white', radius=10).add_to(m)
    
for sn, sa in zip(df2.index, df1.index):
    popup="""
    {0}
    Cases per 100K: {1}
    Deaths per 100K: {2}
    """.format(sn, int(df1.loc[sa]['casespo']), int(df1.loc[sa]['deathspo']))

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='white', color='white', radius=10).add_to(d)    

folium.LayerControl().add_to(m)
folium.LayerControl().add_to(d)

m.save("templates/positives.html")
d.save("templates/deaths.html")
