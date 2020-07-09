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

pd.options.mode.chained_assignment = None

# Positivity Rate Graph
def positivityrate():
    reset_output()

    url = 'https://covidtracking.com/api/v1/us/daily.json'
    data=pd.read_json(url)
    df=pd.DataFrame(data)

    file_path='templates/positivityrate/US_covid-19_positivityrate.html'
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

    graph_name = "COVID-19 Positivity Rate in the United States"
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

positivityrate()

# Daily Deaths Graph
def dailydeaths():
    data=pd.read_json('https://covidtracking.com/api/v1/us/daily.json')
    df=pd.DataFrame(data)
    df

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    file_path='templates/newdeaths/US_covid-19_newdeaths.html'
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

    g=figure(title="COVID-19 Daily New Deaths in the United States", x_axis_type='datetime')
    g.vbar(x='Date', top='Deaths', source=df2, color='red', legend_label='New Deaths')
    g.line(x='Date', y='RAverageDeaths', source=df2, line_color='gray', line_width=2.5, legend_label='New Deaths Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

dailydeaths()

# Daily Positives Graph
def dailypositives():
    data=pd.read_json('https://covidtracking.com/api/v1/us/daily.json')
    df=pd.DataFrame(data)

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

    file_path='templates/newcases/US_covid-19_newpositive.html'
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

    g=figure(title="COVID-19 Daily New Positive Cases in the United States", x_axis_type='datetime')
    g.vbar(x='Date', top='Positive', source=df2, color='red', legend_label='New Positives')
    g.line(x='Date', y='RAveragePos', source=df2, line_color='gray', line_width=2.5, legend_label='New Positives Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

dailypositives()
 