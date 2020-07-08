import folium
import pandas

geojsonmap=f'Map/cb_2018_us_state_500k.geojson'
data=pandas.read_json('https://covidtracking.com/api/v1/states/current.json')
df=pandas.DataFrame(data)

print(df)

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

folium.LayerControl().add_to(m)

m.save("templates/map.html")
