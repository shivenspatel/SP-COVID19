#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from datetime import datetime
import urllib.request as request
import json 
from operator import truediv 
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from datetime import date

output_file('C:\\Shiven\\Python\\Projects\\COVID-19\\templates\\tx_covid-19_positivityrate.html')


# In[2]:


data=pd.read_json('https://covidtracking.com/api/v1/states/tx/daily.json')
df=pd.DataFrame(data)


# In[ ]:





# In[3]:


positive_increase=df['positiveIncrease']
positive_increase.tolist()


# In[4]:


test_increase=df['totalTestResultsIncrease']
test_increase.tolist()


# In[5]:


dates=df['date']
dates.tolist()


# In[6]:


positive=df['positive']
positive.tolist()

h_currently=df['hospitalizedCurrently']
h_currently.tolist()

deaths=df['deathIncrease']
deaths.tolist()


# In[7]:


date1 = ('2020-01-29')
date2 = (str(date.today()))
date_range=pd.date_range(date1, date2).to_pydatetime().tolist()


# In[8]:


rate=[]
for p, t in zip(positive_increase, test_increase):
    if t==0:
        rate.append(0)
    else:
        rate.append(p/t)


# In[9]:


m_dates = []
for item in dates:
    m_dates.append(str(item))


# In[10]:


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


# In[11]:


t_deaths=df['death']
t_deaths.tolist()

t_pos=df['positive']
t_pos.tolist()


# In[12]:


df2=pd.DataFrame({'Date':d_dates,'Rate':rate, 'Deaths':deaths, 'Tests':test_increase, 
                  'Positive':positive_increase, 'Currently_Hospitalized':h_currently, 
                  'Date_String':f_dates, 'Total_Positive':t_pos, 'Total_Deaths':t_deaths})
df2.set_index('Date_String', inplace=True)
df3 = df2[str(date.today()):'2020-03-02']


# In[ ]:





# In[13]:


df2.to_excel('C:\Shiven\Python\Projects\COVID-19\States\TX\df2.xlsx', index = False, header=True)


# In[14]:


g=figure(title="COVID-19 Positivity Rate in Texas (Shiven Patel)", x_axis_type='datetime')
g.line(x='Date', y='Rate', source=df3, line_color='navy', line_width=2.5)

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
show(g)


# In[ ]:




