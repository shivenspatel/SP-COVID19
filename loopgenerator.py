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

def filenameamr(name):
    return 'templates/applemobility/'+name+'_covid-19_amobilityreport.html'

# Positivity Rate Graph
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    reset_output()

    url = 'https://covidtracking.com/api/v1/states/%s/daily.json' % sab
    data=pd.read_json(url)
    df=pd.DataFrame(data)

    file_path=filename(sa)
    print(file_path)
    output_file(file_path)

    positive_increase=df['positiveIncrease']
    positive_increase.tolist()

    test_increase=df['totalTestResultsIncrease']
    test_increase.tolist()

    dates=df['date']
    dates.tolist()

    positive=df['positive']
    positive.tolist()

    h_currently=df['hospitalizedCurrently']
    h_currently.tolist()

    deaths=df['deathIncrease']
    deaths.tolist()

    t_deaths=df['death']
    t_deaths.tolist()

    t_pos=df['positive']
    t_pos.tolist()

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    rate=[]
    for p, t in zip(positive_increase, test_increase):
        if t==0:
            rate.append(0)
        else:
            rate.append(p/t)

    m_dates = []
    for item in dates:
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

    df2=pd.DataFrame({'Date':d_dates,'Rate':rate, 'Deaths':deaths, 'Tests':test_increase, 
                  'Positive':positive_increase, 'Currently_Hospitalized':h_currently, 
                  'Date_String':f_dates, 'Total_Positive':t_pos, 'Total_Deaths':t_deaths})
    df2.set_index('Date_String', inplace=True)
    df3 = df2[str(date.today()):'2020-03-02']

    df4=df3['Rate']

    ra=pd.DataFrame()
    ra['Average']=df4.rolling(window=7, min_periods=1).mean()
    ra['Date'] = df3['Date']
    ra.set_index('Date', inplace=True)
    
    df5=df3.copy()
    r_a=ra['Average']
    df5['Rolling Average']=ra
    df5

    # file_save = 'ExcelDataFrames/{0}'.format(sl)
    # df5.to_excel(file_save, index = False, header=True)

    graph_name = "COVID-19 Positivity Rate in {0}".format(str(sl))
    g=figure(title=graph_name, x_axis_type='datetime')
    g.line(x='Date', y='Rate', source=df5, line_color='navy', line_width=2.5, legend_label='Positivity Rate')
    g.line(x='Date', y='Rolling Average', source=df5, line_color='red', line_width=2.5, legend_label='Positivity Rate Rolling Average')


    hover = HoverTool()
    hover.tooltips=[
        ('Dates', '@Date_String'),
        ('Deaths', '@Deaths'),
        ('Positive Cases', '@Positive'),
        ('Currently Hospitalized', '@Currently_Hospitalized'),
        ('Total Cases', '@Total_Positive'),
        ('Total Deaths', '@Total_Deaths')
    ]

    g.add_tools(hover)
    save(g)

# Death Rate Graph
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    reset_output()

    url = 'https://covidtracking.com/api/v1/states/%s/daily.json' % sab
    data=pd.read_json(url)
    df=pd.DataFrame(data)

    file_path=filenamedr(sa)
    print(file_path)
    output_file(file_path)

    positive_increase=df['positiveIncrease']
    positive_increase.tolist()

    test_increase=df['totalTestResultsIncrease']
    test_increase.tolist()

    dates=df['date']
    dates.tolist()

    positive=df['positive']
    positive.tolist()

    h_currently=df['hospitalizedCurrently']
    h_currently.tolist()

    deaths=df['deathIncrease']
    deaths.tolist()

    t_deaths=df['death']
    t_deaths.tolist()

    t_pos=df['positive']
    t_pos.tolist()

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    m_dates = []
    for item in dates:
        m_dates.append(str(item))

    r_dates = []
    def insertChar(mystring, position, chartoinsert ):
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
    
    death_rate=[]
    for c, d in zip(t_pos, t_deaths):
        if c==0:
            death_rate.append(0)
        else:
            death_rate.append(d/c)

    drformat=[]
    for d in death_rate:
        n=str(round((d*100),2))
        s=n+'%'
        drformat.append(s)

    df2=pd.DataFrame({'Date':d_dates, 'Deaths':deaths, 'Tests':test_increase, 
                  'Positive':positive_increase, 'Currently_Hospitalized':h_currently, 
                  'Date_String':f_dates, 'Total_Positive':t_pos, 'Total_Deaths':t_deaths, 'Death Rate':death_rate,
                'Death_Rate_Format':drformat})
    df2.set_index('Date_String', inplace=True)
    df3 = df2[str(date.today()):'2020-03-02']

    df4=df3['Death Rate']

    ra=pd.DataFrame()
    ra['Average']=df4.rolling(window=7, min_periods=1).mean()
    ra['Date'] = df3['Date']
    ra.set_index('Date', inplace=True)
    
    df5=df3.copy()
    r_a=ra['Average']
    df5['Rolling Average']=ra
    df5

    # file_save = 'ExcelDataFrames/{0}'.format(sl)
    # df5.to_excel(file_save, index = False, header=True)

    graph_name = "COVID-19 Death Rate in {0}".format(str(sl))
    g=figure(title=graph_name, x_axis_type='datetime')
    g.line(x='Date', y='Death Rate', source=df5, line_color='navy', line_width=2.5, legend_label='Death Rate')
    g.line(x='Date', y='Rolling Average', source=df5, line_color='red', line_width=2.5, legend_label='Death Rate Rolling Average')


    hover = HoverTool()
    hover.tooltips=[
        ('Dates', '@Date_String'),
        ('Deaths', '@Deaths'),
        ('Positive Cases', '@Positive'),
        ('Currently Hospitalized', '@Currently_Hospitalized'),
        ('Total Cases', '@Total_Positive'),
        ('Total Deaths', '@Total_Deaths'),
        ('Death Rate', '@Death_Rate_Format')
    ]
    g.add_tools(hover)
    save(g)

# Daily Deaths Graph
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    data=pd.read_json('https://covidtracking.com/api/v1/states/{0}/daily.json'.format(sab))
    df=pd.DataFrame(data)
    df

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    file_path=filenamedea(sa)
    print(file_path)
    output_file(file_path)

    dates=df['date']
    dates.tolist()

    m_dates = []
    for item in dates:
        m_dates.append(str(item))
    
    r_dates = []
    def insertChar(mystring, position, chartoinsert ):
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

    df2=pd.DataFrame({'Date':d_dates, 'Deaths':df['deathIncrease'].tolist(), 'Tests':df['totalTestResultsIncrease'].tolist(), 
                  'Positive':df['positiveIncrease'].tolist(), 'Currently_Hospitalized':df['hospitalizedCurrently'].tolist(), 
                  'Date_String':f_dates, 'Total_Positive':df['positive'].tolist(), 'Total_Deaths':df['death'].tolist()})
    df2.set_index('Date_String', inplace=True)

    df2['RAveragePos']=df2['Positive'].rolling(window=7, min_periods=1).mean()
    df2['RAverageDeaths']=df2['Deaths'].rolling(window=7, min_periods=1).mean()

    hover = HoverTool()
    hover.tooltips=[
        ('Dates', '@Date_String'),
        ('Deaths', '@Deaths'),
        ('Positive Cases', '@Positive'),
        ('Currently Hospitalized', '@Currently_Hospitalized'),
        ('Total Cases', '@Total_Positive'),
        ('Total Deaths', '@Total_Deaths'),
        ('Total Tests', '@Tests')
    ]

    g=figure(title="COVID-19 Daily New Deaths in {0}".format(sl), x_axis_type='datetime')
    g.vbar(x='Date', top='Deaths', source=df2, color='red', legend_label='New Deaths')
    g.line(x='Date', y='RAverageDeaths', source=df2, line_color='gray', line_width=2.5, legend_label='New Deaths Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

# Daily Positives Graph
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    data=pd.read_json('https://covidtracking.com/api/v1/states/{0}/daily.json'.format(sab))
    df=pd.DataFrame(data)
    df

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    file_path=filenamepos(sa)
    print(file_path)
    output_file(file_path)

    dates=df['date']
    dates.tolist()

    m_dates = []
    for item in dates:
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

    df2=pd.DataFrame({'Date':d_dates, 'Deaths':df['deathIncrease'].tolist(), 'Tests':df['totalTestResultsIncrease'].tolist(), 
                  'Positive':df['positiveIncrease'].tolist(), 'Currently_Hospitalized':df['hospitalizedCurrently'].tolist(), 
                  'Date_String':f_dates, 'Total_Positive':df['positive'].tolist(), 'Total_Deaths':df['death'].tolist()})
    df2.set_index('Date_String', inplace=True)

    df2['RAveragePos']=df2['Positive'].rolling(window=7, min_periods=1).mean()
    df2['RAverageDeaths']=df2['Deaths'].rolling(window=7, min_periods=1).mean()
    df2['RAverageHosp']=df2['Currently_Hospitalized'].rolling(window=7, min_periods=1).mean()

    hover = HoverTool()
    hover.tooltips=[
        ('Dates', '@Date_String'),
        ('Deaths', '@Deaths'),
        ('Positive Cases', '@Positive'),
        ('Currently Hospitalized', '@Currently_Hospitalized'),
        ('Total Cases', '@Total_Positive'),
        ('Total Deaths', '@Total_Deaths'),
        ('Total Tests', '@Tests')
    ]

    g=figure(title="COVID-19 Daily New Positive Cases and Current Hospitalizations in {0}".format(sl), x_axis_type='datetime')
    g.vbar(x='Date', top='Positive', source=df2, color='blue', legend_label='New Cases')
    g.line(x='Date', y='RAveragePos', source=df2, line_color='navy', line_width=2.5, legend_label='New Cases Rolling Average')
    g.line(x='Date', y='RAverageHosp', source=df2, line_color='red', line_width=2.5, legend_label='Currently Hospitalized Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

#Google Mobility Rate
googleorigin=pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    google=googleorigin.copy()

    file_path=filenamegmr(sa)
    print(file_path)
    output_file(file_path)

    google=google[google['country_region_code']=='US']
    google=google[google['sub_region_1']== sl]
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

    g=figure(title=f"Mobility Data in {sl} (Google)", x_axis_type='datetime')
    g.line(x='Dates', y='retail', source=google, line_color='red', line_width=2.5, legend_label='Retail and Recreation')
    g.line(x='Dates', y='grocery', source=google, line_color='orange', line_width=2.5, legend_label='Grocery and Pharmacy')
    g.line(x='Dates', y='parks', source=google, line_color='gray', line_width=2.5, legend_label='Parks')
    g.line(x='Dates', y='transit', source=google, line_color='green', line_width=2.5, legend_label='Transit Stations')
    g.line(x='Dates', y='work', source=google, line_color='blue', line_width=2.5, legend_label='Workplaces')
    g.line(x='Dates', y='home', source=google, line_color='purple', line_width=2.5, legend_label='Residential')

    g.legend.location = "bottom_left"
    g.legend.click_policy="hide"

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

    g.legend.label_text_font_size = '8pt'
    g.legend.background_fill_alpha = 0.35
    save(g)

#Apple Mobility Rate
today = date.today()
yesterday = today - dt.timedelta(days=2)
appleorigin=pd.read_csv(f"https://covid19-static.cdn-apple.com/covid19-mobility-data/2012HotfixDev17/v3/en-us/applemobilitytrends-{yesterday}.csv")
for sl, sa, sab in zip(statelist, stateabbreviations, stateabbreviationslower):
    apple=appleorigin.copy()
    apple=apple[apple['country'] == 'United States']
    apple=apple[apple['region'] == sl]

    file_path=filenameamr(sa)
    print(file_path)
    output_file(file_path)

    columns=[]
    for i in apple.columns:
        columns.append(i)

    rows=apple.values.tolist()

    appledf=pd.DataFrame({'Date_str':columns, 'Data':rows[0]})
    appledf=appledf.drop([0,1,2,3,4,5])

    dateforapple=[]
    for i in appledf['Date_str']:
        dateforapple.append(datetime.strptime(i, '%Y-%m-%d'))
    appledf['Date']=dateforapple

    appledf['Data_ra']=appledf['Data'].rolling(window=7, min_periods=1).mean()
    
    a=figure(title=f"Mobility Data in {sl} (Apple)", x_axis_type='datetime')
    a.line(x='Date', y='Data', source=appledf, line_color='gray', line_width=2.5, legend_label='Driving')
    a.line(x='Date', y='Data_ra', source=appledf, line_color='black', line_width=2.5, legend_label='Driving Rolling Average')

    a.legend.location = "top_left"
    a.legend.click_policy="hide"

    save(a)

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
        %s
        Cases: %s
        Deaths: %s
        """ % (cd, df4.loc[cd]['cases'], df4.loc[cd]['deaths'])
        
        folium.CircleMarker(location=(float(df3.loc[cn]['LAT']), float(df3.loc[cn]['LON'])), 
                            tooltip=cn, popup=popup, fill=True, fill_color='white', color='white', radius=5).add_to(m)

        print(cn, cd)

    print(filenamemap(sa))
    m.save(filenamemap(sa))

 