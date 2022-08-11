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

df2=pandas.read_csv("Map/statecenters.csv")
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
    <b>{0}</b>
    <b>Cases per 100K:</b> {1}
    <b>Deaths per 100K:</b> {2}
    """.format(sn, int(df1.loc[sa]['casespo']), int(df1.loc[sa]['deathspo']))

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='gray', color='gray', radius=7).add_to(m)
    
for sn, sa in zip(df2.index, df1.index):
    popup="""
    <b>{0}</b>
    <b>Cases per 100K:</b> {1}
    <b>Deaths per 100K:</b> {2}
    """.format(sn, int(df1.loc[sa]['casespo']), int(df1.loc[sa]['deathspo']))

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='gray', color='gray', radius=7).add_to(d)    

m.save("templates/positives.html")
d.save("templates/deaths.html")

moderna = pandas.read_json("https://data.cdc.gov/resource/b7pe-5nws.json")
pfizer = pandas.read_json("https://data.cdc.gov/resource/saz5-9hgg.json")
master = pandas.DataFrame()

f_states=[]
for i in list(pfizer["jurisdiction"]):
    new_state = ''.join(e for e in i if e.isalpha() | e.isspace())
    f_states.append(new_state)

master["pfizer_state"] = f_states
master["pfizer_total"] = list(pfizer["total_pfizer_allocation_first_dose_shipments"])
master["moderna_state"] = list(moderna["jurisdiction"]) 
master["moderna_total"] = list(moderna["total_moderna_allocation_first_dose_shipments"])

statelist = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

for i, state in zip(master.index, master["pfizer_state"]):
    if state not in statelist:
        master.drop([i], inplace=True)

master["pfizer_total"] = master["pfizer_total"].str.replace(",","").astype(float)
master["moderna_total"] = master["moderna_total"].str.replace(",","").astype(float)

total_vax=[]
for p, m in zip(list(master["pfizer_total"]), list(master["moderna_total"])):
  total_vax.append(p+m)

master["total"] = total_vax

master.sort_values("pfizer_state", ascending=True, inplace=True)
master['state'] = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

master['population'] = [4833722, 735132, 6626624, 2959373, 38332521, 5268367,3596080, 925749, 19552860, 9992167, 1404054, 1612136, 12882135, 6570902, 3090416, 2893957, 4395295, 4625470, 1328302, 5928814, 6692824, 9895622, 5420380,2991207, 6044171, 1015165, 1868516, 2790136, 1323459, 8899339, 2085287, 19651127, 9848060, 723393, 11570808, 3850568, 3930065, 12773801, 1051511, 4774839, 844877, 6495978, 26448193, 2900872, 626630, 8260405, 6971406, 1854304, 5742713, 582658]

ppop=[]
mpop=[]
tpop=[]
for t, p in zip(master["pfizer_total"], master["population"]):
    pp=((t*100000)/p)
    ppop.append(pp)

for t, p in zip(master["moderna_total"], master["population"]):
    pp=((t*100000)/p)
    mpop.append(pp)

for t, p in zip(master["total"], master["population"]):
    pp=((t*100000)/p)
    tpop.append(pp)

master["pfizer_population"]=ppop
master["moderna_population"]=mpop
master["total_population"]=tpop

master.sort_values("total", ascending=True, inplace=True)
master.reset_index(drop=True, inplace=True)

vt = folium.Map(location=[39.8283, -95.5795], zoom_start=4)

folium.Choropleth(
    geo_data=geojsonmap,
    name='Total Allocated Vaccinations in Each State',
    data=master,
    columns=['state', 'total'],
    key_on='feature.properties.STUSPS',
    fill_color='YlGnBu',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Total Allocated Vaccines'
).add_to(vt)

for sn, st in zip(master['pfizer_state'], master['total']):
    popup=f"""
    <b>{sn}</b>
    <b>Total:</b> {int(st)}
    """

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='gray', color='gray', radius=7).add_to(vt)

vt.save("templates/total_vaccines.html")

vp = folium.Map(location=[39.8283, -95.5795], zoom_start=4)

folium.Choropleth(
    geo_data=geojsonmap,
    name='Total Allocated Vaccinations per 100k Citizens in Each State',
    data=master,
    columns=['state', 'total_population'],
    key_on='feature.properties.STUSPS',
    fill_color='YlGnBu',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Allocated Vaccines per 100k Citizens'
).add_to(vp)

for sn, st in zip(master['pfizer_state'], master['total_population']):
    popup=f"""
    <b>{sn}</b>
    <b>Total:</b> {int(st)}
    """

    folium.CircleMarker(location=(float(df2.loc[sn]['latitude']), float(df2.loc[sn]['longitude'])), 
                        tooltip=sn, popup=popup, fill=True, fill_color='gray', color='gray', radius=7).add_to(vp)

vp.save("templates/pop_vaccines.html")

unr = pandas.DataFrame()
unr = pandas.read_html("https://www.bls.gov/web/laus/laumstrk.htm", match='State')
unr = unr[0]
unr.drop([51, 52, 53], inplace=True)
unr.drop(columns=['Rank'], inplace=True)
unr.rename(columns={unr.columns[1]:"Rate"}, inplace=True)
unr = unr.astype({'State':str, 'Rate':float})

ue = folium.Map(location=[39.8283, -95.5795], zoom_start=4)

folium.Choropleth(
    geo_data=geojsonmap,
    name='Unemployment Rate in Each State',
    data=unr,
    columns=['State', 'Rate'],
    key_on='feature.properties.NAME',
    fill_color='RdPu',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Unemployment Rate (Lower is Better)').add_to(ue)

dc = pandas.Series({'latitude':38.9072, 'longitude':-77.0369, 'stf':"DC", 'st':"dc", 'population':684498}, name="District of Columbia")
df2 = df2.append(dc)
df2.sort_values("name", inplace=True)

for sn, st in zip(unr['State'], unr['Rate']):
    popup=f"""
    <b>{sn}</b>
    <b>Rate: </b> {str(st)+"%"}
    """

    folium.CircleMarker(location=(df2.loc[sn]['latitude'], df2.loc[sn]['longitude']), 
                        tooltip=sn, popup=popup, fill=True, fill_color='gray', color='gray', radius=7).add_to(ue)

ue.save("templates/unemploymentrate.html")

