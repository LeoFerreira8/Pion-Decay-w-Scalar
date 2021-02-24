# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:24:18 2020
Region Plot

@author: Léo
"""

from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('DataRatiox.dat')
yaxis = genfromtxt('DataRatioy.dat')
data=genfromtxt('dataRatio0.dat')

#Reescalonando
xaxis=xaxis/1e6
experimental=2.52806
levels=np.arange(0,60,60/60)
interpolate = 1

inxaxis=np.linspace(xaxis[0],xaxis[-1],num=interpolate*len(xaxis))
inyaxis=np.linspace(yaxis[0],yaxis[-1],num=interpolate*len(yaxis))
indata = scipy.ndimage.zoom(data, interpolate)

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(inxaxis,inyaxis,indata,levels)
#plt.scatter(23.9996,-0.039393,s=80,c='r',marker='^')

#plt.xlim(10,40)
#plt.ylim(-0.1,0.1)
ax1.set_ylabel(r"$g/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi\,$ (TeV)",fontsize=30)
ax1.set_title(r'$\chi^2$ Distribution $(\delta=0)$',fontsize=36)
cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"$\chi^2$ Value (2 d.o.f)",fontsize=25)
plt.grid()

plt.show()
