# spcovid19
A Python project that visualizes COVID-19 data at the federal and state/county level. Includes graphs (bokeh) and maps (folium).

main.py - Main file; generates all graphs and maps in their respective folders.

loopgenerator.py - deprecated

codegenerator.py - meant to generate functions to paste into flask file; generates each state's webpage.

mainpagemap.py - generates map displayed on entry page.

usgenerator.py - generates all graphs for national data.

execute.py - used on AWS server as a single file to run all necessary commands to update data daily with cron

County level data is from the <i>New York Times</i> GitHub database (https://github.com/nytimes/covid-19-data).

Mobility Data is from Google:
Google LLC "Google COVID-19 Community Mobility Reports".
https://www.google.com/covid19/mobility/ Accessed: 07.19.2020.


All other data is pulled from the <i>The Atlantic</i>'s COVID Data Tracking Project (https://covidtracking.com/data/api).

All Python, HTML and CSS code is my intellectual property, and may not be used without permission.
