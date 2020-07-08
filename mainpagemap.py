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

m = folium.Map(location=[39.8283, -95.5795], zoom_start=4)

folium.Choropleth(
    geo_data=geojsonmap,
    name='Positive Cases',
    data=df,
    columns=['state', 'positive'],
    key_on='feature.properties.STUSPS',
    fill_color='OrRd',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Positive COVID-19 Cases'
).add_to(m)

for sn, sa in zip(df2.index, df1.index):
    popup="""
    {0}
    Cases: {1}
    Deaths: {2}
    """.format(sn, df1.loc[sa]['positive'], df1.loc[sa]['death'])

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='white', color='white', radius=10).add_to(m)

folium.LayerControl().add_to(m)

m.save("templates/map.html")
