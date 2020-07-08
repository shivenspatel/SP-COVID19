import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, save
from datetime import datetime
import urllib.request as request
import json 
from operator import truediv 
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from datetime import date
from bokeh.io import reset_output
import folium

def counties(sl, sa, sab):
    #Pulling Data
    cdata=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv")
    hdata=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")

    county_data=pd.read_csv('Counties/c_03mr20 - Copy.csv')

    geojsonmap='Counties/us-counties.json'

    cdata = cdata.fillna(0)
    cdata['fips_str'] = cdata['fips'].astype(int).astype(str)

    center_data=pd.read_csv('Counties/table-1.csv')
    center_data.set_index('state', inplace=True)
    latitude = center_data['latitude']
    longitude = center_data['longitude']

    df4 = pd.DataFrame()
    df5 = pd.DataFrame()
    
    df1=cdata
    df1.set_index('county', inplace=True)
    df1 = df1.sort_values('county')
    df4 = df1[df1['fips_str'] != '0']

    df2=county_data
    df2.set_index('COUNTYNAME', inplace=True)
    df2 = df2.sort_values(by=['COUNTYNAME'])
    pd.set_option('display.max_rows', 500)
    df2['FIPS'] = df2['FIPS'].astype(float)
    df2['fips_str']=df2['FIPS'].astype(int).astype(str)

    df3 = pd.DataFrame()
    df4['county'] = df4.index
    df4.set_index('fips', inplace=True)

    fips=[]
    fips=df4.index.tolist()

    for i, x in zip(df2['FIPS'], df2.index):
        if float(i) in fips:
            df3 = df3.append(df2.loc[x])
        else:
            print(i)

    m = folium.Map(location=[39.8283, -95.5795], zoom_start=4) 

    df4['fips'] = df4.index
    df4.set_index('county', inplace=True)

    folium.Choropleth(
    geo_data=geojsonmap,
    name='Positive Cases',
    data=df4,
    columns=['fips_str', 'cases'],
    key_on='feature.fips',
    fill_color='OrRd',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Positive COVID-19 Cases').add_to(m)

    for cn, cd in zip(df3.index, df4.index):
        popup="""
        %s
        Cases: %s
        Deaths: %s
        """ % (cd, df4.loc[cd]['cases'], df4.loc[cd]['deaths'])
        
        folium.CircleMarker(location=(float(df3.loc[cn]['LAT']), float(df3.loc[cn]['LON'])), 
                            tooltip=cn, popup=popup, fill=True, fill_color='white', color='white', radius=5).add_to(m)

        print(cn, cd)

    print("counties.html")
    m.save('counties.html')

counties('Unites States', 'US', 'us')