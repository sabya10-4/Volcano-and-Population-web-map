# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 21:34:01 2020

@author: sada0419
"""


import folium
map=folium.Map(location=[50.708611, -105.179628],zoom_start=3)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location = [50.01001,-105.5433], popup = "Hi. I am a Marker" , icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("map1.html")