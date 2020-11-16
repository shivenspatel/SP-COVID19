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
import datetime as dt

pd.options.mode.chained_assignment = None

statelist = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

stateabbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

stateabbreviationslower = []
for i in stateabbreviations:
    stateabbreviationslower.append(i.lower())

def filename(name):
    return 'templates/positivityrate/'+name+'_covid-19_positivityrate.html'

def filenamemap(name):
    return 'templates/countymaps/'+name+'_covid-19_countymap.html'

def filenamepos(name):
    return 'templates/newcases/'+name+'_covid-19_newpositive.html'

def filenamedea(name):
    return 'templates/newdeaths/'+name+'_covid-19_newdeaths.html'

def filenamedr(name):
    return 'templates/deathrate/'+name+'_covid-19_deathrate.html'

def filenamegmr(name):
    return 'templates/googlemobility/'+name+'_covid-19_gmobilityreport.html'

def filenameh(name):
    return 'templates/hospital/'+name+'_covid-19_hospital.html'

def filenametest(name):
    return 'templates/testing/'+name+'_covid-19_testing.html'

googleorigin=pd.read_csv("filtered.csv", 
dtype={"country_region_code":object,
"country_region":object,
"sub_region_1":object,
"sub_region_2":object,
"metro_area":object,
"iso_3166_2_code":object,
"census_fips_code":float,
"date":object,
"retail_and_recreation_percent_change_from_baseline":float,
"grocery_and_pharmacy_percent_change_from_baseline":float,
"parks_percent_change_from_baseline":float,
"transit_stations_percent_change_from_baseline":float,
"workplaces_percent_change_from_baseline":float,
"residential_percent_change_from_baseline":float}, low_memory=False)

for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    df = pd.read_csv(f'https://covidtracking.com/api/v1/states/{sab}/daily.csv')

    positivity_rate = []
    positive=list(df['positiveIncrease'])
    tottest=list(df['totalTestResultsIncrease'])
    for p, t, i in zip(positive, tottest, df.index):
        if t == 0:
            positivity_rate.append(0)
        else:
            if i >= len(positive)-8:
                positivity_rate.append(sum(positive[i:])/sum(tottest[i:]))
            else:
                positivity_rate.append(sum(positive[i:i+7])/sum(tottest[i:i+7]))

    prformat=[]
    for p in positivity_rate:
        n=str(round((p*100),2))
        s=n+'%'
        prformat.append(s)

    death_rate = []
    for c, d in zip(df['positive'], df['death']):
        if c==0:
            death_rate.append(0)
        else:
            death_rate.append(d/c)

    drformat=[]
    for d in death_rate:
        n=str(round((d*100),2))
        s=n+'%'
        drformat.append(s)

    m_dates = []
    for item in df['date']:
        m_dates.append(str(item))

    r_dates = []
    def insertChar(mystring, position, chartoinsert ):
        longi = len(mystring)
        mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
        return mystring 
    
    for m in m_dates:
        r_dates.append(insertChar(m, 4, '-'))

    f_dates = []
    for r in r_dates:
        f_dates.append(insertChar(r, 7, '-'))

    d_dates = []
    for f in f_dates:
        d_dates.append(datetime.strptime(f, '%Y-%m-%d'))

    df['dates_f'] = d_dates
    df['dates_s'] = f_dates
    df['PosRate'] = positivity_rate
    df['DeaRate'] = death_rate
    df['PosRateFormat'] = prformat
    df['DeaRateFormat'] = drformat

    df['PosRateAvg']=df['PosRate'].rolling(window=7, min_periods=1).mean()
    df['DeaRateAvg']=df['DeaRate'].rolling(window=7, min_periods=1).mean()

    df['RAverageHosp']=df['hospitalizedCurrently'].rolling(window=7, min_periods=1).mean()
    df['RAverageICU']=df['inIcuCurrently'].rolling(window=7, min_periods=1).mean()
    df['RAverageVent']=df['onVentilatorCurrently'].rolling(window=7, min_periods=1).mean()

    df['DeaAverage']=df['deathIncrease'].rolling(window=7, min_periods=1).mean()
    df['PosAverage']=df['positiveIncrease'].rolling(window=7, min_periods=1).mean()
    df['TotAverage']=df['totalTestResultsIncrease'].rolling(window=7, min_periods=1).mean()
    df['NegAverage']=df['negativeIncrease'].rolling(window=7, min_periods=1).mean()

    pr=figure(title=f"COVID-19 Positivity Rate in {sl}", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    pr.line(x='dates_f', y='PosRate', source=df, line_color='navy', line_width=2.5, legend_label='7 Day Test Positivity Rate')
    pr.line(x='dates_f', y='PosRateAvg', source=df, line_color='red', line_width=2.5, legend_label='Positivity Rate Rolling Average')

    prhover = HoverTool()
    prhover.tooltips=[
        ('Date', '@dates_s'),
        ('Deaths', '@deathIncrease'),
        ('Positive Cases', '@positiveIncrease'),
        ('Total Cases', '@positive'),
        ('Total Deaths', '@death'),
        ('Positivity Rate', '@PosRateFormat')
    ]

    pr.legend.location = "top_left"
    pr.legend.click_policy="hide"
    pr.legend.label_text_font_size = '8pt'
    pr.legend.background_fill_alpha = 0.35

    prfile=filename(sa)
    output_file(prfile)
    pr.add_tools(prhover)
    print(prfile)
    save(pr)

    dr=figure(title=f"COVID-19 Death Rate in {sl}", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    dr.line(x='dates_f', y='DeaRate', source=df, line_color='navy', line_width=2.5, legend_label='Cummulative Death Rate')
    dr.line(x='dates_f', y='DeaRateAvg', source=df, line_color='red', line_width=2.5, legend_label='Death Rate Rolling Average')

    drhover = HoverTool()
    drhover.tooltips=[
        ('Date', '@dates_s'),
        ('Deaths', '@deathIncrease'),
        ('Positive Cases', '@positiveIncrease'),
        ('Total Cases', '@positive'),
        ('Total Deaths', '@death'),
        ('Death Rate', '@DeaRateFormat')
    ]

    dr.legend.location = "top_left"
    dr.legend.click_policy="hide"
    dr.legend.label_text_font_size = '8pt'
    dr.legend.background_fill_alpha = 0.35

    drfile=filenamedr(sa)
    output_file(drfile)
    dr.add_tools(drhover)
    print(drfile)
    save(dr)

    d=figure(title=f"COVID-19 Daily New Deaths in {sl}", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    d.vbar(x='dates_f', top='deathIncrease', source=df, color='red', legend_label='New Deaths', width=43200000)
    d.line(x='dates_f', y='DeaAverage', source=df, line_color='gray', line_width=2.5, legend_label='New Deaths Rolling Average')

    dhover = HoverTool()
    dhover.tooltips=[
        ('Date', '@dates_s'),
        ('Deaths', '@deathIncrease'),
        ('Total Deaths', '@death')
    ]

    d.legend.location = "top_left"
    d.legend.click_policy="hide"
    d.legend.label_text_font_size = '8pt'
    d.legend.background_fill_alpha = 0.35

    dfile=filenamedea(sa)
    output_file(dfile)
    d.add_tools(dhover)
    print(dfile)
    save(d)

    p=figure(title=f"COVID-19 Daily New Cases in {sl}", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    p.vbar(x='dates_f', top='positiveIncrease', source=df, color='blue', legend_label='New Deaths', width=43200000)
    p.line(x='dates_f', y='PosAverage', source=df, line_color='navy', line_width=2.5, legend_label='New Deaths Rolling Average')

    phover = HoverTool()
    phover.tooltips=[
        ('Date', '@dates_s'),
        ('Cases', '@positiveIncrease'),
        ('Total Cases', '@positive')
    ]

    p.legend.location = "top_left"
    p.legend.click_policy="hide"
    p.legend.label_text_font_size = '8pt'
    p.legend.background_fill_alpha = 0.35

    pfile=filenamepos(sa)
    output_file(pfile)
    p.add_tools(phover)
    print(pfile)
    save(p)

    google=googleorigin.copy()

    google=google[google['sub_region_1'] == sl]
    google=google[google['sub_region_2'].isnull()]

    dates=[]
    for i in google['date']:
        dates.append(datetime.strptime(i, '%Y-%m-%d'))
    google['Dates']=dates

    google['retail']=google['retail_and_recreation_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['grocery']=google['grocery_and_pharmacy_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['parks']=google['parks_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['transit']=google['transit_stations_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['work']=google['workplaces_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['home']=google['residential_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()

    g=figure(title=f"Mobility Data in {sl} (Google)", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    g.line(x='Dates', y='retail', source=google, line_color='red', line_width=2.5, legend_label='Retail and Recreation')
    g.line(x='Dates', y='grocery', source=google, line_color='orange', line_width=2.5, legend_label='Grocery and Pharmacy')
    g.line(x='Dates', y='parks', source=google, line_color='gray', line_width=2.5, legend_label='Parks')
    g.line(x='Dates', y='transit', source=google, line_color='green', line_width=2.5, legend_label='Transit Stations')
    g.line(x='Dates', y='work', source=google, line_color='blue', line_width=2.5, legend_label='Workplaces')
    g.line(x='Dates', y='home', source=google, line_color='purple', line_width=2.5, legend_label='Residential')

    g.legend.location = "bottom_left"
    g.legend.click_policy="hide"
    g.legend.label_text_font_size = '8pt'
    g.legend.background_fill_alpha = 0.35

    hover = HoverTool()

    hover.tooltips=[
        ('Dates', '@date'),
        ('Retail and Recreation % Change', '@retail_and_recreation_percent_change_from_baseline'),
        ('Grocery and Pharmacy % Change', '@grocery_and_pharmacy_percent_change_from_baseline'),
        ('Parks % Change', '@parks_percent_change_from_baseline'),
        ('Transit Station % Change', '@transit_stations_percent_change_from_baseline'),
        ('Workplace % Change', '@workplaces_percent_change_from_baseline'),
        ('Residential % Change', '@residential_percent_change_from_baseline')
    ]

    g.add_tools(hover)

    gfile=filenamegmr(sa)
    output_file(gfile)
    print(gfile)
    save(g)

    h=figure(title=f"COVID-19 Hospitalization Data in {sl}", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

    h.line(x='dates_f', y='hospitalizedCurrently', source=df, line_color='navy', line_width=2.5, legend_label='Currently Hospitalized')
    h.line(x='dates_f', y='RAverageHosp', source=df, line_color='blue', line_width=2.5, legend_label='Currently Hospitalized Rolling Average')

    h.line(x='dates_f', y='inIcuCurrently', source=df, line_color='maroon', line_width=2.5, legend_label='Currently in ICU')
    h.line(x='dates_f', y='RAverageICU', source=df, line_color='red', line_width=2.5, legend_label='Currently in ICU Rolling Average')

    h.line(x='dates_f', y='onVentilatorCurrently', source=df, line_color='violet', line_width=2.5, legend_label='Currently on Ventilator')
    h.line(x='dates_f', y='RAverageVent', source=df, line_color='purple', line_width=2.5, legend_label='Currently on Ventilator Rolling Average')

    hhover = HoverTool()
    hhover.tooltips=[
        ('Dates', '@dates_s'),
        ('Currently Hospitalized', '@hospitalizedCurrently'),
        ('In ICU', '@inIcuCurrently'),
        ('On Ventilator', '@onVentilatorCurrently')
    ]

    h.legend.location = "top_left"
    h.legend.click_policy="hide"
    h.legend.label_text_font_size = '8pt'
    h.legend.background_fill_alpha = 0.35
    h.add_tools(hhover)

    hfile = filenameh(sa)
    output_file(hfile)
    print(hfile)
    save(h)

    t = figure(x_axis_type='datetime', title=f'COVID-19 Testing Data in {sl}', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

    t.vbar_stack(['positiveIncrease', 'negativeIncrease'], x='dates_f', width=43200000, 
        color=['red', 'gray'], source=df, legend_label=['Positive Results', 'Negative Results'])

    t.line(x='dates_f', y='PosAverage', source=df, line_color='maroon', line_width=2.5, legend_label='Positive Results Rolling Average')
    t.line(x='dates_f', y='NegAverage', source=df, line_color='navy', line_width=2.5, legend_label='Negative Results Rolling Average')
    t.line(x='dates_f', y='TotAverage', source=df, line_color='black', line_width=2.5, legend_label='Total Results Rolling Average')
    
    t.legend.location = "top_left"
    t.legend.click_policy="hide"
    t.legend.label_text_font_size = '8pt'
    t.legend.background_fill_alpha = 0.35

    thover = HoverTool()
    thover.tooltips = [
        ('Dates', '@dates_s'),
        ('New Positive Tests', '@positiveIncrease'),
        ('New Negative Tests', '@negativeIncrease'),
        ('Total Tests Performed', '@totalTestResultsIncrease')
    ]

    t.add_tools(thover)

    tfile = filenametest(sa)
    output_file(tfile)
    print(tfile)
    save(t)

#Map
cdataorigin=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv")
hdataorigin=pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    #Pulling Data
    cdata=cdataorigin.copy()
    hdata=hdataorigin.copy()

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
    
    df1=cdata[cdata['state'] == sl]
    df1.set_index('county', inplace=True)
    df1 = df1.sort_values('county')
    df4 = df1[df1['fips_str'] != '0']

    df2=county_data[county_data['STATE'] == sa]
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

    stateloctag="{0}".format(sa)
    m = folium.Map(location=[float(latitude.loc[stateloctag]), float(longitude.loc[stateloctag])], zoom_start=6) 

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
        <b>%s</b>
        <b>Cases</b>: %s
        <b>Deaths</b>: %s
        """ % (cd, df4.loc[cd]['cases'], df4.loc[cd]['deaths'])
        
        folium.CircleMarker(location=(float(df3.loc[cn]['LAT']), float(df3.loc[cn]['LON'])), 
                            tooltip=cn, popup=popup, fill=True, fill_color='white', color='white', radius=5).add_to(m)

        print(cn, cd)

    print(filenamemap(sa))
    m.save(filenamemap(sa))

def main():
    google=googleorigin.copy()

    google=google[google['country_region_code']=='US']
    google=google[google['sub_region_1'].isnull()]

    dates=[]
    for i in google['date']:
        dates.append(datetime.strptime(i, '%Y-%m-%d'))
    google['Dates']=dates

    google['retail']=google['retail_and_recreation_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['grocery']=google['grocery_and_pharmacy_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['parks']=google['parks_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['transit']=google['transit_stations_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['work']=google['workplaces_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()
    google['home']=google['residential_percent_change_from_baseline'].rolling(window=7, min_periods=1).mean()

    g=figure(title="Mobility Data in the US (Google)", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    g.line(x='Dates', y='retail', source=google, line_color='red', line_width=2.5, legend_label='Retail and Recreation')
    g.line(x='Dates', y='grocery', source=google, line_color='orange', line_width=2.5, legend_label='Grocery and Pharmacy')
    g.line(x='Dates', y='parks', source=google, line_color='gray', line_width=2.5, legend_label='Parks')
    g.line(x='Dates', y='transit', source=google, line_color='green', line_width=2.5, legend_label='Transit Stations')
    g.line(x='Dates', y='work', source=google, line_color='blue', line_width=2.5, legend_label='Workplaces')
    g.line(x='Dates', y='home', source=google, line_color='purple', line_width=2.5, legend_label='Residential')

    g.legend.location = "bottom_left"
    g.legend.click_policy="hide"
    g.legend.label_text_font_size = '8pt'
    g.legend.background_fill_alpha = 0.35

    hover = HoverTool()

    hover.tooltips=[
        ('Dates', '@date'),
        ('Retail and Recreation % Change', '@retail_and_recreation_percent_change_from_baseline'),
        ('Grocery and Pharmacy % Change', '@grocery_and_pharmacy_percent_change_from_baseline'),
        ('Parks % Change', '@parks_percent_change_from_baseline'),
        ('Transit Station % Change', '@transit_stations_percent_change_from_baseline'),
        ('Workplace % Change', '@workplaces_percent_change_from_baseline'),
        ('Residential % Change', '@residential_percent_change_from_baseline')
    ]

    g.add_tools(hover)

    gfile='templates/googlemobility/US_covid-19_gmobilityreport.html'
    output_file(gfile)
    print(gfile)
    save(g)

main()