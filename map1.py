# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:34:01 2020

@author: sada0419
"""


import folium
import pandas as pd

#Read file to a dataframe
data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
ele = list(data['ELEV'])

map = folium.Map(location=[50.708611, -105.179628],zoom_start=3, tiles = 'Stamen Terrain')

fg = folium.FeatureGroup(name="My Map")

for lt,ln,el,nm in zip(lat,lon,ele,name):
    fg.add_child(folium.Marker(location = [lt,ln], popup = nm + " " + str(el) + ' mts' , icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("map1.html")