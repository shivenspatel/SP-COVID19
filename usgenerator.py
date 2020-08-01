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

googleorigin=pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")

def main():
    df = pd.read_csv('https://covidtracking.com/api/v1/us/daily.csv')

    positivity_rate = []
    for p, t in zip(df['positive'], df['totalTestResults']):
        if t == 0:
            positivity_rate.append(0)
        else:
            positivity_rate.append(p/t)

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

    pr=figure(title="COVID-19 Positivity Rate in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    pr.line(x='dates_f', y='PosRate', source=df, line_color='navy', line_width=2.5, legend_label='Positivity Rate')
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

    prfile='templates/positivityrate/US_covid-19_positivityrate.html'
    output_file(prfile)
    pr.add_tools(prhover)
    print(prfile)
    save(pr)

    dr=figure(title="COVID-19 Death Rate in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    dr.line(x='dates_f', y='DeaRate', source=df, line_color='navy', line_width=2.5, legend_label='Death Rate')
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

    drfile='templates/deathrate/US_covid-19_deathrate.html'
    output_file(drfile)
    dr.add_tools(drhover)
    print(drfile)
    save(dr)

    d=figure(title="COVID-19 Daily New Deaths in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
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

    dfile='templates/newdeaths/US_covid-19_newdeaths.html'
    output_file(dfile)
    d.add_tools(dhover)
    print(dfile)
    save(d)

    p=figure(title="COVID-19 Daily New Cases in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
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

    pfile='templates/newcases/US_covid-19_newpositive.html'
    output_file(pfile)
    p.add_tools(phover)
    print(pfile)
    save(p)

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

    h=figure(title="COVID-19 Hospitalization Data in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

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

    hfile = 'templates/hospital/US_covid-19_hospital.html'
    output_file(hfile)
    print(hfile)
    save(h)

    t = figure(x_axis_type='datetime', title='COVID-19 Testing Data in the US', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")

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

    tfile = 'templates/testing/US_covid-19_testing.html'
    output_file(tfile)
    print(tfile)
    save(t)
main()

def compare():
    df = pd.read_csv('https://covidtracking.com/api/v1/states/current.csv')

    df = df.drop([3, 8, 12, 27, 42, 50])

    df = df.reset_index()
    
    df['statename']=["Alaska","Alabama","Arkansas","Arizona","California","Colorado",
                    "Connecticut","Delaware","Florida","Georgia","Hawaii","Iowa","Idaho","Illinois",
                    "Indiana","Kansas","Kentucky","Louisiana","Massachusetts","Maryland","Maine",
                    "Michigan","Minnesota","Missouri","Mississippi","Montana","North Carolina","North Dakota",
                    "Nebraska","New Hampshire","New Jersey","New Mexico","Nevada","New York",
                    "Ohio","Oklahoma","Oregon","Pennsylvania",
                    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
                    "Virginia","Vermont","Washington","Wisconsin","West Virginia","Wyoming"]

    df.sort_values(by='statename',ascending=True,inplace=True)

    df['population']=[4833722, 735132, 6626624, 2959373, 38332521, 5268367, 3596080, 925749, 19552860, 9992167, 1404054, 
                    1612136, 12882135, 6570902, 3090416, 2893957, 4395295, 4625470, 1328302, 5928814, 6692824, 9895622, 
                    5420380, 2991207, 6044171, 1015165, 1868516, 2790136, 1323459, 8899339, 2085287, 19651127, 9848060, 
                    723393, 11570808, 3850568, 3930065, 12773801, 1051511, 4774839, 844877, 6495978, 26448193, 2900872, 
                    626630, 8260405, 6971406, 1854304, 5742713, 582658]

    casespo=[]
    casespostr=[]
    for cases, population in zip(df['positive'], df['population']):
        cpo=((cases*100000)/population)
        casespo.append(cpo)
        casespostr.append(str(int(cpo)))

    df['casespo']=casespo
    df['casespostr']=casespostr

    deathspo=[]
    deathspostr=[]
    for deaths, population in zip(df['death'], df['population']):
        dpo=((deaths*100000)/population)
        deathspo.append(dpo)
        deathspostr.append(str(int(dpo)))

    df['deathspo']=deathspo
    df['deathspostr']=deathspostr

    df = df.sort_values('death')

    g=figure(title="COVID-19 Total Deaths in Each State", sizing_mode='stretch_both', 
    width=350, y_range=df['state'], tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")

    g.hbar(y='state', right='death', source=df, color='red', height=0.75, left=0)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@statename'),
        ('Deaths', '@death')
    ]

    g.add_tools(hover)

    output_file('templates/compare/deathscompare.html')
    save(g)

    df = df.sort_values('deathspo')

    cp=figure(title="COVID-19 Total Deaths per 100K Citizens in Each State", sizing_mode='stretch_both', 
    width=350, y_range=df['state'], tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")

    cp.hbar(y='state', right='deathspo', source=df, color='red', height=0.75, left=0)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@statename'),
        ('Deaths per 100K', '@deathspostr')
    ]

    cp.add_tools(hover)

    output_file('templates/compare/deathspocompare.html')
    save(cp)

    df = df.sort_values('positive')

    d=figure(title="COVID-19 Total Cases in Each State", sizing_mode='stretch_both', 
    width=350, y_range=df['state'], tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")

    d.hbar(y='state', right='positive', source=df, color='navy', height=0.75, left=0)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@statename'),
        ('Cases', '@positive')
    ]

    d.add_tools(hover)

    output_file('templates/compare/casescompare.html')
    save(d)

    df = df.sort_values('casespo')

    dp=figure(title="COVID-19 Cases per 100K Residents in Each State", sizing_mode='stretch_both', width=350, 
          y_range=df['state'], tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")

    dp.hbar(y='state', right='casespo', source=df, color='navy', height=0.75, left=0)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@statename'),
        ('Cases per 100K', '@casespostr')
    ]

    dp.add_tools(hover)

    output_file('templates/compare/casespocompare.html')
    save(dp)

compare()