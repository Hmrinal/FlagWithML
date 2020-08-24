# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:35:30 2020

@author: Mrinal
"""


import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((0,1), width=12, height=2, facecolor='green', edgecolor='grey') 
b = patch.Rectangle((0,3), width=12, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0,5), width=12, height=2, facecolor='#FF9933', edgecolor='grey')

m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

#chakra

radius=0.8
py.plot(6,4, marker='o', markerfacecolor='#000088ff',markersize=9.5)
chakra = py.Circle((6,4),radius,color='#000088ff',fill=False,linewidth=7)
n.add_artist(chakra)


py.show()