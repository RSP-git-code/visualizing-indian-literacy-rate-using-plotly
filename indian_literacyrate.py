#Importing various libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import json
import pprint
import numpy as np
#Drawing Map in Map:
import plotly.io as pio
#India Map:
indian_states=json.load(open("C:\\Users\\RIYA\\OneDrive\\Desktop\\VS Code Quickstart\\Mapping in Python\\states_india.geojson",'r',encoding='utf-8'))
pprint.pprint((indian_states['features'][1]))
#Id : for mapping each state
state_id_map={}
for feature in indian_states['features']:
    feature['id']=feature['properties']['state_code']
    state_id_map[feature['properties']['st_nm']]=feature['id']
print(state_id_map)
df=pd.read_excel(r'C:\Users\RIYA\OneDrive\Desktop\literacyrate_data.xlsx')
# Remove rows with NaN values in the 'State' or 'Average' columns
df = df.dropna(subset=['State', 'Average'])
print(df.head())
#Appending id column in excel:
df['id'] = df['State'].apply(lambda x: state_id_map.get(x))

print(df['Average'])
# #Reading headers of the excel table
# print(df.head())
#Chloropeth:
fig=px.choropleth(df,locations='id',geojson=indian_states,color='Average',scope='asia',hover_name='State')

#Indian Map:
fig.update_geos(fitbounds="locations",visible=False)

#Title:
#title_x= alignment of title in X axis,title_y= alignment of title in Y axis
#monospace:each character has same width or horizontal space
fig.update_layout(title_text='Literacy Rate across states in India',title_x=0.5 ,title_y=1,font=dict(family="Comic Sans Ms, monospace", size=18, color="RebeccaPurple"))
fig.show()




