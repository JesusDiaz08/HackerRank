# -*- coding: utf-8 -*-
"""
Created on Sun May  6 17:15:15 2018

@author: kaimo
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def line():
    x = np.arange(11)
    line, = plt.plot(10*x,"o-")

def rectangle(tam):
    redim = tam/10
    tam /= 20;
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    ax1.add_patch(patches.RegularPolygon(
            (tam, tam),     # (x,y)
            4,              # number of vertices
            redim-.1,       # radius
            orientation=np.pi/4,
            )
    )

def paint_line_parab():
    x = np.arange(11)
    y = x*x
    parab, = plt.plot(x,y,'o-')
    line()
    plt.xlabel("X")
    plt.ylabel("Y")

def line_3D():
    fig = plt.figure()
    sub = fig.add_subplot(1,1,1,projection='3d')
    t = np.linspace(0,4*np.pi,50)
    x = np.cos(t)
    y = np.sin(t)
    z = np.tan(t)
    sub.plot(x,y,z)
    
line_3D()