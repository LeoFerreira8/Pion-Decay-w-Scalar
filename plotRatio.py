from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)

plt.rc('xtick',labelsize=25)
plt.rc('ytick',labelsize=25)

xaxis = genfromtxt('MassXAxis3.dat')
yaxis = genfromtxt('CouplingYAxis3.dat')
data0=genfromtxt('GammaDecayRatioData20.dat')

levels = np.arange(0.28, 10, 0.05)
#Reescalonando
xaxis=xaxis/1e6
data0=data0*1e4

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, data0,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Ratio $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma])/\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^- [\gamma]) (\delta=0)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Branching Ratio $(\times 10^{-4}$)",fontsize=25)
plt.grid()

mycontour=[1.233]

smplot=plt.contour(xaxis, yaxis,data0,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(R_{e/\mu}= 1.233 \times 10^{-4}$)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()

xaxis = genfromtxt('MassXAxis3.dat')
yaxis = genfromtxt('CouplingYAxis3.dat')
datapi2=genfromtxt('GammaDecayRatioData2Pi2.dat')

levels = np.arange(0.46, 10, 0.05)
#Reescalonando
xaxis=xaxis/1e6
datapi2=datapi2*1e4

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, datapi2,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Ratio $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma])/\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^- [\gamma]) (\delta=\pi/2,\, 3\pi/2)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Branching Ratio $(\times 10^{-4}$)",fontsize=25)
plt.grid()

mycontour=[1.233]

smplot=plt.contour(xaxis, yaxis,datapi2,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(R_{e/\mu}= 1.233 \times 10^{-4}$)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()

xaxis = genfromtxt('MassXAxis3.dat')
yaxis = genfromtxt('CouplingYAxis3.dat')
datapi=genfromtxt('GammaDecayRatioData2Pi.dat')

levels = np.arange(0.62, 10, 0.05)
#Reescalonando
xaxis=xaxis/1e6
datapi=datapi*1e4

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis, datapi,levels)

#plt.xlim(600,1000)
#plt.ylim(-1,1)
ax1.set_ylabel(r"$g_\phi/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$M_\phi$ (TeV)",fontsize=30)
ax1.set_title(r'Ratio $\Gamma(\pi^-\rightarrow{} \bar{\nu} e^- [\gamma])/\Gamma(\pi^-\rightarrow{} \bar{\nu} \mu^- [\gamma]) (\delta=\pi)$',fontsize=36)

cbar=fig1.colorbar(theplot)
cbar.ax.set_ylabel(r"Branching Ratio $(\times 10^{-4}$)",fontsize=25)
plt.grid()

mycontour=[1.233]

smplot=plt.contour(xaxis, yaxis,datapi,mycontour,colors='r',linewidths=3,linestyles='dashed')
proxy=[smplot.collections[0]]

plt.legend(proxy,[r'Experimental mean value''\n'r'$(R_{e/\mu}= 1.233 \times 10^{-4}$)'],fontsize=22,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()
