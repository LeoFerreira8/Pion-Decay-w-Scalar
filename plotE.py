from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('MassXAxis.dat')
yaxis = genfromtxt('CouplingYAxis.dat')
data0=genfromtxt('GammaDecayEData20.dat')

levels = np.arange(0.71, 5, 0.05)
#Reescalonando
xaxis=xaxis/1e6
data0=data0*1e18

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data0,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma]) (\delta=0)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-18}$ MeV)",fontsize=25)
plt.grid()

mycontour=[3.11]

smplot=plt.contour(xaxis, yaxis,data0,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 3.11 \times 10^{-18}$ MeV)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()

plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('MassXAxis.dat')
yaxis = genfromtxt('CouplingYAxis.dat')
data2=genfromtxt('GammaDecayEData2Pi2.dat')

levels = np.arange(1.15, 5, 0.05)
#Reescalonando
xaxis=xaxis/1e6
data2=data2*1e18

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data2,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma]) (\delta=\pi/2,\,3\pi/2)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-18}$ MeV)",fontsize=25)
plt.grid()

mycontour=[3.11]

smplot=plt.contour(xaxis, yaxis,data2,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 3.11 \times 10^{-18}$ MeV)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()

plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('MassXAxis.dat')
yaxis = genfromtxt('CouplingYAxis.dat')
datapi=genfromtxt('GammaDecayEData2Pi.dat')

levels = np.arange(1.5, 5, 0.05)
#Reescalonando
xaxis=xaxis/1e6
datapi=datapi*1e18

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, datapi,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma]) (\delta=\pi)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-18}$ MeV)",fontsize=25)
plt.grid()

mycontour=[3.11]

smplot=plt.contour(xaxis, yaxis,datapi,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 3.11 \times 10^{-18}$ MeV)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()