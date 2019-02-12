
# coding: utf-8

# In[1]:


import json
import mysql.connector 
from mysql.connector import errorcode
from mysql.connector import connection
import datetime 
import time
import plotly.plotly as py
import plotly.graph_objs as go 
import plotly
from plotly.offline import *
import MySQLdb
import pandas as pd


# In[2]:


cnx = connection.MySQLConnection(
  host="localhost",
  user="Alexi",
  password="DaB4I?!hUL?",
  database= "Oli_db")
    

print("Data")


# In[3]:


conn = MySQLdb.connect(host="localhost", user="foo", passwd="bar", db="oli_db")
cursor = conn.cursor()
cursor.execute('SELECT timestamp,timestamp_format, `active_Power_Supply`,`active_Power_Demand` FROM oli_36');

rows = cursor.fetchall()
str(rows)#[0:300]


# In[4]:


df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'timestamp', 1: 'timestamp_format', 2: 'active_Power_Supply', 3: 'active_Power_Demand' }, inplace=True);
#timestamp_format = datetime.datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')
#df['timestamp_format'] = df['timestamp_format'].astype(String)

#timestamp_for = datetime.strptime(timestamp_format,"%Y-%m-%d %H:%M:%S")
#print(dt_obj)
#df['timestamp_formats'] = datetime.strftime(timestamp_for,"%Y-%m-%d %H:%M:%S")
#print(timestamp_format)


# In[5]:



def to_unix_time(dt):
    epoch =  datetime.datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

trace1 = go.Scatter(
            x=df['timestamp_format'],
            y=df['active_Power_Supply'],
            line = dict(color = ('rgb(0, 128, 0)'),
            width = 4),
            name='active_Power_Supply')

trace2 = go.Scatter(
            x=df['timestamp_format'],
            y=df['active_Power_Demand'],
            line = dict(color = ('rgb(154,205,50)'),
            width = 3),
            name='active_Power_Demand')
data = [trace1,trace2]

layout = go.Layout(title='Oli_36-Graphic_Plot from Database',
    xaxis = dict(title='Time-Date',
                   range = [to_unix_time(datetime.datetime(2019, 2, 11)),
                            to_unix_time(datetime.datetime(2019, 2, 12))]
    ),yaxis=dict(type='log',title='Power_Supply/Demand' ),)

fig = go.Figure(data = data, layout = layout)

plotly.offline.plot(fig, filename='Databas.html')

