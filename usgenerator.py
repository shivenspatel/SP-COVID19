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
    g=figure(title=graph_name, x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
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
def deathrate():
    reset_output()

    url = 'https://covidtracking.com/api/v1/us/daily.json'
    data=pd.read_json(url)
    df=pd.DataFrame(data)

    file_path='templates/deathrate/US_covid-19_deathrate.html'
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

    graph_name = "COVID-19 Death Rate in the United States"
    g=figure(title=graph_name, x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
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
def dailydeaths():   
    reset_output()

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

    g=figure(title="COVID-19 Daily New Deaths in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    g.vbar(x='Date', top='Deaths', source=df2, color='red', legend_label='New Deaths', width=43200000)
    g.line(x='Date', y='RAverageDeaths', source=df2, line_color='gray', line_width=2.5, legend_label='New Deaths Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

# Daily Positives Graph
def dailypositives():
    reset_output()

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

    g=figure(title="COVID-19 Daily New Positive Cases in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    g.vbar(x='Date', top='Positive', source=df2, color='blue', legend_label='New Cases', width=43200000)
    g.line(x='Date', y='RAveragePos', source=df2, line_color='navy', line_width=2.5, legend_label='New Cases Rolling Average')

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.add_tools(hover)
    save(g)

#Google Mobility Rate
googleorigin=pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")
def googlemobility():
    reset_output()

    google=googleorigin.copy()

    file_path='templates/googlemobility/US_covid-19_gmobilityreport.html'
    print(file_path)
    output_file(file_path)

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

    g=figure(title=f"Mobility Data in the US (Google)", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
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

#Hospitalization Data
def hospital():
    reset_output()

    data=pd.read_json('https://covidtracking.com/api/v1/us/daily.json')
    hospfile = 'templates/hospital/US_covid-19_hospital.html'
    output_file(hospfile)
    print(hospfile)

    inpdata=pd.read_csv('https://healthdata.gov/sites/default/files/reported_inpatient_all_20200720_0537.csv')
    ICUdata=pd.read_csv('https://healthdata.gov/sites/default/files/icu_final_20200720_0537.csv')
    df=pd.DataFrame(data)

    # inpdata = inpdata[inpdata['state'] == sa]
    # inpdata.reset_index(inplace=True)

    # total_inpatient=[]
    # for occupied, percentage in zip(inpdata['Inpatient Beds Occupied Estimated'], inpdata['Percentage of Inpatient Beds Occupied Estimated']):
    #     if percentage != 0:
    #         total_inpatient.append((occupied/percentage)-occupied)
    #     else:
    #         total_inpatient.append(0)
        
    # inpdata['Total_Inpatient_Beds_Available']=total_inpatient

    # inpdates=pd.date_range('2020-01-01', inpdata['collection_date'].iloc[-1])
    # inpdata['dates']=inpdates

    # ICUdata = ICUdata[ICUdata['state'] == sa]

    # total_icu=[]
    # for occupied, percentage in zip(ICUdata['ICU Beds Occupied Estimated'], ICUdata['Percentage of ICU Beds Occupied Estimated']):
    #     if percentage != 0:
    #         total_icu.append((occupied/percentage)-occupied)
    #     else:
    #         total_icu.append(0)

    # ICUdata['Total_ICU_Beds_Available']=total_icu
    # icudates=pd.date_range('2020-01-01', inpdates['collection_date'].iloc[-1])
    # ICUdata['dates']=icudates

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()
    dates=df['date']
    dates.tolist()
    df['death']
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

    df['dates_f'] = d_dates
    df['dates_s'] = f_dates

    df['RAverageHosp']=df['hospitalizedCurrently'].rolling(window=7, min_periods=1).mean()
    df['RAverageICU']=df['inIcuCurrently'].rolling(window=7, min_periods=1).mean()
    df['RAverageVent']=df['onVentilatorCurrently'].rolling(window=7, min_periods=1).mean()

    g=figure(title=f"COVID-19 Hospitalization Data in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

    # g.line(x='dates', y='Total_Inpatient_Beds_Available', source=inpdata, line_color='yellow', line_width=2.5, legend_label='Total Inpatient Beds')
    # g.line(x='dates', y='Total_ICU_Beds_Available', source=ICUdata, line_color='gray', line_width=2.5, legend_label='Total ICU Beds')

    g.line(x='dates_f', y='hospitalizedCurrently', source=df, line_color='navy', line_width=2.5, legend_label='Currently Hospitalized')
    g.line(x='dates_f', y='RAverageHosp', source=df, line_color='blue', line_width=2.5, legend_label='Currently Hospitalized Rolling Average')

    g.line(x='dates_f', y='inIcuCurrently', source=df, line_color='maroon', line_width=2.5, legend_label='Currently in ICU')
    g.line(x='dates_f', y='RAverageICU', source=df, line_color='red', line_width=2.5, legend_label='Currently in ICU Rolling Average')

    g.line(x='dates_f', y='onVentilatorCurrently', source=df, line_color='violet', line_width=2.5, legend_label='Currently on Ventilator')
    g.line(x='dates_f', y='RAverageVent', source=df, line_color='purple', line_width=2.5, legend_label='Currently on Ventilator Rolling Average')

    hover = HoverTool()
    hover.tooltips=[
        ('Dates', '@dates_s'),
        ('Currently Hospitalized', '@hospitalizedCurrently'),
        ('In ICU', '@inIcuCurrently'),
        ('On Ventilator', '@onVentilatorCurrently')
    #     ('Available ICU Beds', '@Total_ICU_Beds_Available'),
    #     ('Available Inpatient Beds', '@Total_Inpatient_Beds_Available')
    ]

    g.legend.location = "top_left"
    g.legend.click_policy="hide"

    g.legend.label_text_font_size = '8pt'
    g.legend.background_fill_alpha = 0.35

    g.add_tools(hover)
    save(g)

#Testing Data
def testing():
    df=pd.read_json('https://covidtracking.com/api/v1/us/daily.json')

    testfile = 'templates/testing/US_covid-19_testing.html'
    output_file(testfile)
    print(testfile)

    date1 = ('2020-01-29')
    date2 = (str(date.today()))
    date_range=pd.date_range(date1, date2).to_pydatetime().tolist()

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

    df['dates_f']=d_dates
    df['dates_s']=f_dates

    df['PosAverage']=df['positiveIncrease'].rolling(window=7, min_periods=1).mean()
    df['TotAverage']=df['totalTestResultsIncrease'].rolling(window=7, min_periods=1).mean()
    df['NegAverage']=df['negativeIncrease'].rolling(window=7, min_periods=1).mean()

    p = figure(x_axis_type='datetime', title=f'COVID-19 Testing Data in the US', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

    p.vbar_stack(['positiveIncrease', 'negativeIncrease'], x='dates_f', width=43200000, 
        color=['red', 'blue'], source=df, legend_label=['Positive Results', 'Negative Results'])

    p.line(x='dates_f', y='PosAverage', source=df, line_color='maroon', line_width=2.5, legend_label='Positive Results Rolling Average')
    p.line(x='dates_f', y='NegAverage', source=df, line_color='navy', line_width=2.5, legend_label='Negative Results Rolling Average')
    p.line(x='dates_f', y='TotAverage', source=df, line_color='black', line_width=2.5, legend_label='Total Results Rolling Average')
    
    p.legend.location = "top_left"
    p.legend.click_policy="hide"

    hover = HoverTool()
    hover.tooltips = [
        ('Dates', '@dates_s'),
        ('New Positive Tests', '@positiveIncrease'),
        ('New Negative Tests', '@negativeIncrease'),
        ('Total Tests Performed', '@totalTestResultsIncrease')
    ]

    p.legend.label_text_font_size = '8pt'
    p.legend.background_fill_alpha = 0.35

    p.add_tools(hover)
    save(p)
 

positivityrate()
deathrate()
dailydeaths()
dailypositives()
googlemobility()
hospital()
testing()