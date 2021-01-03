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

#googleorigin=pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")

# Generates US page graphs
def main():
    df = pd.read_csv('https://covidtracking.com/api/v1/us/daily.csv')

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

    pr=figure(title="COVID-19 Positivity Rate in the US", x_axis_type='datetime', sizing_mode='stretch_both', tools=['xpan', 'xwheel_zoom'], active_scroll="xwheel_zoom")
    pr.line(x='dates_f', y='PosRate', source=df, line_color='navy', line_width=2.5, legend_label='7 Day Positivity Rate')
    pr.line(x='dates_f', y='PosRateAvg', source=df, line_color='red', line_width=2.5, legend_label='Positivity Rate Rolling Average')

    prhover = HoverTool()
    prhover.tooltips=[
        ('Date', '@dates_s'),
        ('Deaths', '@deathIncrease'),
        ('Positive Cases', '@positiveIncrease'),
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

# Compare page graphs
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
    print("templates/compare/deathscompare.html")

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
    print("templates/compare/deathspocompare.html")

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
    print("templates/compare/casescompare.html")

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
    print("templates/compare/casespocompare.html")

    statelist=list(df['statename'])

    moderna = pd.read_json("https://data.cdc.gov/resource/b7pe-5nws.json")
    pfizer = pd.read_json("https://data.cdc.gov/resource/saz5-9hgg.json")
    master = pd.DataFrame()

    f_states=[]
    for i in list(pfizer["jurisdiction"]):
        new_state = ''.join(e for e in i if e.isalpha() | e.isspace())
        f_states.append(new_state)

    master["pfizer_state"] = f_states
    master["pfizer_total"] = list(pfizer["total_pfizer_allocation_first_dose_shipments"])
    master["moderna_state"] = list(moderna["jurisdiction"]) 
    master["moderna_total"] = list(moderna["total_moderna_allocation_first_dose_shipments"])

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

    master['population'] = [4833722, 735132, 6626624, 2959373, 38332521, 5268367, 3596080, 925749, 19552860, 9992167, 1404054, 
                    1612136, 12882135, 6570902, 3090416, 2893957, 4395295, 4625470, 1328302, 5928814, 6692824, 9895622, 
                    5420380, 2991207, 6044171, 1015165, 1868516, 2790136, 1323459, 8899339, 2085287, 19651127, 9848060, 
                    723393, 11570808, 3850568, 3930065, 12773801, 1051511, 4774839, 844877, 6495978, 26448193, 2900872, 
                    626630, 8260405, 6971406, 1854304, 5742713, 582658]

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

    p=figure(title="COVID-19 Total Allocated Vaccinations in Each State", sizing_mode='stretch_both', width=350, y_range=list(master["state"]), tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")
    source=ColumnDataSource(master)
    legend=['Pfizer', 'Moderna']
    p.hbar_stack(['pfizer_total', 'moderna_total'], y='state', source=source, legend_label=legend, color=['red','blue'], height=0.75)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@pfizer_state'),
        ('Total', '@total{int}'),
        ('Pfizer', '@pfizer_total{int}'),
        ('Moderna', '@moderna_total{int}')
    ]

    p.legend.location = "bottom_right"
    p.legend.click_policy="hide"
    p.legend.label_text_font_size = '8pt'
    p.legend.background_fill_alpha = 0.35
    p.add_tools(hover)
    output_file('templates/compare/totvax.html')
    save(p)
    print("templates/compare/totvax.html")

    master.sort_values("total_population", ascending=True, inplace=True)
    master.reset_index(drop=True, inplace=True)

    source2=ColumnDataSource(master)
    m=figure(title="COVID-19 Total Allocated Vaccinations per 100K Citizens in Each State",sizing_mode='stretch_both', width=350, y_range=list(master["state"]), tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")
    m.hbar_stack(['pfizer_population', 'moderna_population'], y='state', source=source2, color=['maroon','navy'], legend_label=legend, height=0.75)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@pfizer_state'),
        ('Total', '@total_population{int}'),
        ('Pfizer', '@pfizer_population{int}'),
        ('Moderna', '@moderna_population{int}')
    ]

    m.legend.location = "bottom_right"
    m.legend.click_policy="hide"
    m.legend.label_text_font_size = '8pt'
    m.legend.background_fill_alpha = 0.35
    m.add_tools(hover)
    output_file('templates/compare/popvax.html')
    save(m)
    print("templates/compare/popvax.html")

    unr = pd.DataFrame()
    unr = pd.read_html("https://www.bls.gov/web/laus/laumstrk.htm", match='State')
    unr = unr[0]
    unr.drop([51, 52, 53], inplace=True)
    unr.drop(columns=['Rank'], inplace=True)
    unr.rename(columns={unr.columns[1]:"Rate"}, inplace=True)
    unr = unr.astype({'State':str, 'Rate':float})
    unr.sort_values("State", inplace=True)
    unr['sa']=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    unr.sort_values("Rate", ascending=False, inplace=True)


    un=figure(title="Unemployment Rate in Each State (Lower is Better)",sizing_mode='stretch_both', width=350, y_range=list(unr["sa"]), tools=['ypan', 'ywheel_zoom'], active_scroll="ywheel_zoom")
    un.hbar(y='sa', right='Rate', source=unr, color='purple', height=0.75, left=0)

    hover = HoverTool()
    hover.tooltips=[
        ('State', '@State'),
        ('Unemplyment Rate', '@Rate%')
    ]

    un.add_tools(hover)
    output_file('templates/compare/unemp.html')
    save(un)
    print("templates/compare/unemp.html")

compare()