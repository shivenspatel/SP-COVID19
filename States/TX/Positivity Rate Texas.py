#!/usr/bin/env python
# coding: utf-8

# In[34]:


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

output_file('tx_covid-19_positivityrate.html')


# In[35]:


data=pd.read_json('https://covidtracking.com/api/v1/states/tx/daily.json')
df=pd.DataFrame(data)


# In[ ]:





# In[36]:


positive_increase=df['positiveIncrease']
positive_increase.tolist()


# In[37]:


test_increase=df['totalTestResultsIncrease']
test_increase.tolist()


# In[38]:


dates=df['date']
dates.tolist()


# In[39]:


positive=df['positive']
positive.tolist()

h_currently=df['hospitalizedCurrently']
h_currently.tolist()

deaths=df['deathIncrease']
deaths.tolist()


# In[40]:


date1 = ('2020-01-29')
date2 = (str(date.today()))
date_range=pd.date_range(date1, date2).to_pydatetime().tolist()


# In[41]:


rate=[]
for p, t in zip(positive_increase, test_increase):
    if t==0:
        rate.append(0)
    else:
        rate.append(p/t)


# In[42]:


m_dates = []
for item in dates:
    m_dates.append(str(item))


# In[43]:


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


# In[44]:


t_deaths=df['death']
t_deaths.tolist()

t_pos=df['positive']
t_pos.tolist()


# In[45]:


df2=pd.DataFrame({'Date':d_dates,'Rate':rate, 'Deaths':deaths, 'Tests':test_increase, 
                  'Positive':positive_increase, 'Currently_Hospitalized':h_currently, 
                  'Date_String':f_dates, 'Total_Positive':t_pos, 'Total_Deaths':t_deaths})
df2.set_index('Date_String', inplace=True)
df3 = df2[str(date.today()):'2020-03-02']


# In[46]:


df4=df3['Rate']

ra=pd.DataFrame()
ra['Average']=df4.rolling(7).mean()
ra['Date'] = df3['Date']
ra.set_index('Date', inplace=True)
print(ra)


# In[47]:


df5=df3.copy()
r_a=ra['Average']
df5['Rolling Average']=ra
df5


# In[48]:


df2.to_excel('C:\Shiven\Python\Projects\COVID-19\States\TX\df2.xlsx', index = False, header=True)


# In[49]:


g=figure(title="COVID-19 Positivity Rate in Texas (Shiven Patel)", x_axis_type='datetime')
g.line(x='Date', y='Rate', source=df5, line_color='navy', line_width=2.5)
g.line(x='Date', y='Rolling Average', source=df5, line_color='gray', line_width=2.5)

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




