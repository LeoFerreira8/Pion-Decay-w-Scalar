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
import math as m
plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('DataRatioxlog.dat')
yaxis = genfromtxt('DataRatioylog.dat')
data=genfromtxt('dataRatio0log.dat')

#Reescalonando
xaxis = 10**(xaxis)/1e6
yaxis = 10**(yaxis)
#xaxis=xaxis/1e6

experimental=2.52806
levels1=[0,2.3,6.18,11.83,19.33]

fig1, ax1 = plt.subplots(figsize=(18,12))

#smplot=plt.scatter(12.6324,0.000803837,s=200,c='k',marker='^',zorder=10)
plt.contour(xaxis,yaxis, data,levels1,colors=["g","r","b","y"])
theplot=plt.contourf(xaxis,yaxis,data,levels1,alpha=0.6, colors=["r","b","y","g"])
#ax1.plot(xaxis,np.zeros(len(xaxis)),color='r',linewidth=2)
ax1.set_yscale('log')
ax1.set_xscale('log')

#plt.xlim(1,20)
#plt.ylim(-1,20)

ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Allowed region $(\delta=0)$',fontsize=36)
plt.minorticks_on()
plt.grid()

#proxy=[smplot]
#proxy1=[plt.Rectangle((0,0),1,1,fc=fc.get_facecolor()[0])
#       for fc in theplot.collections]
#proxy=np.append(proxy,proxy1)

proxy=[plt.Rectangle((0,0),1,1,fc=fc.get_facecolor()[0])
       for fc in theplot.collections]

plt.legend(proxy,[r'$1\sigma$',r'$2\sigma$',r'$3\sigma$','$4\sigma$'],fontsize=28,loc='upper left',framealpha=0.9,fancybox=True)

plt.show()

data=genfromtxt('dataRatioPi2log.dat')

fig1, ax1 = plt.subplots(figsize=(18,12))

plt.contour(xaxis,yaxis, data,levels1,colors=["g","r","b","y"])
theplot=plt.contourf(xaxis,yaxis,data,levels1,alpha=0.6, colors=["r","b","y","g"])
#ax1.plot(xaxis,np.zeros(len(xaxis)),color='r',linewidth=2)
ax1.set_yscale('log',nonposy='clip')
ax1.set_xscale('log',nonposx='clip')


#plt.xlim(1,0)
#plt.ylim(0.0001,20)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Allowed region $(\delta=\pi/2,\,3\pi/2)$',fontsize=36)
plt.minorticks_on()
plt.grid()

proxy1=[plt.Rectangle((0,0),1,1,fc=fc.get_facecolor()[0])
       for fc in theplot.collections]
proxy=proxy1

plt.legend(proxy,[r'$1\sigma$',r'$2\sigma$',r'$3\sigma$','$4\sigma$'],fontsize=28,loc='upper left',framealpha=0.9,fancybox=True)

plt.show()

data=genfromtxt('dataRatioPilog.dat')

fig1, ax1 = plt.subplots(figsize=(18,12))

plt.contour(xaxis,yaxis, data,levels1,colors=["g","r","b","y"])
theplot=plt.contourf(xaxis,yaxis,data,levels1,alpha=0.6, colors=["r","b","y","g"])
#ax1.plot(xaxis,np.zeros(len(xaxis)),color='r',linewidth=2)
ax1.set_yscale('log')
ax1.set_xscale('log')

#ax1.clabel(theplot,inline=True, fontsize=14)
#plt.xlim(10,40)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Allowed region $(\delta=\pi)$',fontsize=36)
plt.minorticks_on()
plt.grid()

proxy1=[plt.Rectangle((0,0),1,1,fc=fc.get_facecolor()[0])
       for fc in theplot.collections]
proxy=proxy1

plt.legend(proxy,[r'$1\sigma$',r'$2\sigma$',r'$3\sigma$','$4\sigma$'],fontsize=28,loc='upper left',framealpha=0.9,fancybox=True)

plt.show()
