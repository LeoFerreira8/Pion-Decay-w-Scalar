from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('MassXAxis2.dat')
yaxis = genfromtxt('CouplingYAxis2.dat')
data=genfromtxt('GammaDecayMuData20test.dat')

levels = np.arange(2, 10, 0.2)
#Reescalonando
xaxis=xaxis/1e6
data=data*1e14

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^- [\gamma]) (\delta=0)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-14}$ MeV)",fontsize=25)
plt.grid()

mycontour=[2.52806]

smplot=plt.contour(xaxis, yaxis,data,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 2.528 \times 10^{-14}$ MeV)'],fontsize=22,loc='upper right',framealpha=0.4,fancybox=True)

plt.show()

xaxis = genfromtxt('MassXAxis2.dat')
yaxis = genfromtxt('CouplingYAxis2.dat')
data=genfromtxt('GammaDecayMuData2Pi2test.dat')

levels = np.arange(1.7, 7.35, 0.2)
#Reescalonando
xaxis=xaxis/1e6
data=data*1e14

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data,levels)

#plt.xlim(1,10)
#plt.ylim(0,100)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^- [\gamma]) (\delta=\pi/2, \, 3\pi/2)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-14}$ MeV)",fontsize=25)
plt.grid()

mycontour=[2.52806]

smplot=plt.contour(xaxis, yaxis,data,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 2.528 \times 10^{-14}$ MeV)'],fontsize=22,loc='upper right',framealpha=0.4,fancybox=True)

plt.show()

xaxis = genfromtxt('MassXAxis2.dat')
yaxis = genfromtxt('CouplingYAxis2.dat')
data=genfromtxt('GammaDecayMuData2Pitest.dat')

levels = np.arange(1.54, 10, 0.2)
#Reescalonando
xaxis=xaxis/1e6
data=data*1e14

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data,levels)

#plt.xlim(1,10)
#plt.ylim(0,100)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Pion decay rate $\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^-[\gamma]) (\delta=\pi)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Decay Rate $(\times 10^{-14}$ MeV)",fontsize=25)
plt.grid()

mycontour=[2.52806]

smplot=plt.contour(xaxis, yaxis,data,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(\Gamma= 2.528 \times 10^{-14}$ MeV)'],fontsize=22,loc='upper right',framealpha=0.4,fancybox=True)

plt.show()