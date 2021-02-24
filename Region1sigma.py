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
data1=genfromtxt('dataRatioPi2.dat')
data2=genfromtxt('dataRatioPi.dat')

U = np.array([[0. + 0.8233423346336566, 
  0. + 0.5480031021810003, 
  0. + 0.147648230602334], 
    [0. + (-0.3870607187509474 + 
      0.8324662155306966*(0. - 0.10564847372300273)), 
      0. + (0.5815358974302447 + 
      0.5540758070878027*(0. - 0.10564847372300273)), 
  0.7076993712022076], 
    [0. + (0.3964643741876437 + 
      0.8324662155306966*(0. - 0.10314261970688936)), 
      0. + (-0.5956643350075612 + 
      0.5540758070878027*(0. - 0.10314261970688936)), 
  0.690913598071423]])

me = 0.5109989461
mmu = 105.6583745

def func(ml,m,n):
    f = (2/3)*(U[n,0]+U[n,1]+U[n,2])*0.97420*(((2.16+4.67)/139.57061**2)*(ml/(80.379*1e3)**2))*(m*1e6)**2
    return f

ftildivf=139.57061**2/(2.16+4.67)

levels = [0,2.3]
#Reescalonando
xaxis=xaxis/1e6
interpolate = 1

#xaxis=np.linspace(xaxis[0],xaxis[-1],num=interpolate*len(inxaxis))
#yaxis=np.linspace(yaxis[0],yaxis[-1],num=interpolate*len(inyaxis))
#data = scipy.ndimage.zoom(data, interpolate)
#data1 = scipy.ndimage.zoom(data1, interpolate)
#data2 = scipy.ndimage.zoom(data2, interpolate)

fig1, ax1 = plt.subplots(figsize=(18,12))
#theplotf=plt.contourf(xaxis,yaxis,data,levels,alpha=0.2,colors='b')
theplot=plt.contour(xaxis,yaxis,data,levels,alpha=1,colors='b',linewidths=2,linestyles='dashed')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='b',linewidth=2,linestyle='dashed',alpha=0.2)

#theplot1f=plt.contourf(xaxis,yaxis,data1,levels,alpha=0.2,colors='r')
theplot1=plt.contour(xaxis,yaxis,data1,levels,alpha=1,colors='r',linewidths=2,linestyles='dashed')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='r',linewidth=2,linestyle='dashed',alpha=0.2)

#theplot2f=plt.contourf(xaxis,yaxis,data2,levels,alpha=0.2,colors='g')
theplot2=plt.contour(xaxis,yaxis,data2,levels,alpha=1,colors='g',linewidths=2,linestyles='dashed')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='g',linewidth=2,linestyle='dashed',alpha=0.2)

#smplot=plt.scatter(7.5503e2,-55.6085,s=200,c='k',marker='^')

#plt.xlim(1,20)
plt.ylim(-1,15)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Allowed region ($1\sigma$)',fontsize=36)
ax1.grid(True)

#proxy=[plt.Rectangle((0,0),1,1,fc=theplot.collections[0].get_facecolor()[0]),plt.Rectangle((0,0),1,1,fc=theplot1.collections[0].get_facecolor()[0]),plt.Rectangle((0,0),1,1,fc=theplot2.collections[0].get_facecolor()[0])]
proxy = []

proxy.append(theplot.collections[0])
    
proxy.append(theplot1.collections[0])
    
proxy.append(theplot2.collections[0])

plt.legend(proxy,[r'$\delta=0$',r'$\delta=\pi/2,3\pi/2$',r'$\delta=\pi$'],fontsize=28,loc='upper left',framealpha=0.4,fancybox=True)

plt.show()

datapartial = np.minimum(data,data1)
datatotal = np.minimum(datapartial,data2)

fig1, ax1 = plt.subplots(figsize=(18,12))
theplotf=plt.contourf(xaxis,yaxis,datatotal,levels,alpha=0.2,colors='b')
theplot = plt.contour(xaxis,yaxis,datatotal,levels,alpha=1,colors='b',linewidths=3,linestyles='dashed')
theplotcont = plt.plot(xaxis,func(me,xaxis,0),color='k',linewidth=2, label=r'$\Gamma_e = \Gamma_e^{SM}$')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='k',linewidth=2)
plt.plot(xaxis,func(mmu,xaxis,1),color='purple',label=r'$\Gamma_\mu = \Gamma_\mu^{SM}$')

plt.legend(fontsize=28,loc='upper left',framealpha=0.4,fancybox=True)

#plt.xlim(1,10)
plt.ylim(-1,15)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Total allowed region ($\delta \in [0,2\pi)$) ($1\sigma$)',fontsize=36)
ax1.grid(True)

plt.show()

X, Y = np.meshgrid(xaxis,yaxis)

F = Y/((X/(80.379*10**-3))**2)

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis,datatotal,levels,alpha=0.2,colors='b')
theplotcont1 = plt.contour(xaxis,yaxis,F,[0.00001,0.0001,0.001,0.01],colors = ['r','orange','y','g'],linewidths=2)
theplotcont = plt.plot(xaxis,func(me,xaxis,0),color='k',linewidth=2, label=r'$\Delta_e = 0$')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='k',linewidth=2)

proxy, labels = ax1.get_legend_handles_labels()
proxy.append(plt.Rectangle((0,0),1,1,fc=theplot.collections[0].get_facecolor()[0]))
for i in range(len(theplotcont1.collections)):
    proxy.append(theplotcont1.collections[i])

ax1.legend(proxy,labels+[r'Allowed region $1\sigma$',r'$\tilde{G}_\eta = 10^{-5}\, G_F$',r'$\tilde{G}_\eta = 10^{-4}\, G_F$',r'$\tilde{G}_\eta = 10^{-3}G_F$',r'$\tilde{G}_\eta = 10^{-2}\, G_F$'],fontsize=28,loc='upper left',framealpha=0.4,fancybox=True)

#plt.xlim(1,10)
plt.ylim(-1,15)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Total allowed region ($\delta \in [0,2\pi)$) ($1\sigma$)',fontsize=36)
ax1.grid(True)

plt.show()

X, Y = np.meshgrid(xaxis,yaxis)

F = Y/((X/(80.379*10**-3))**2)

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis,datatotal,levels,alpha=0.2,colors='b')
theplotcont1 = plt.contour(xaxis,yaxis,F,[0.00001,0.0001,0.001,0.01],colors = ['r','orange','y','g'],linewidths=2,linestyles='dashed')
theplotcont = plt.plot(xaxis,func(me,xaxis,0),color='k',linewidth=2, label=r'$\Gamma_e = \Gamma_e^{SM}$')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='k',linewidth=2)

proxy, labels = ax1.get_legend_handles_labels()
proxy.append(plt.Rectangle((0,0),1,1,fc=theplot.collections[0].get_facecolor()[0]))
for i in range(len(theplotcont1.collections)):
    proxy.append(theplotcont1.collections[i])

ax1.legend(proxy,labels+[r'Allowed region $1\sigma$'],fontsize=28,loc='upper left',framealpha=0.4,fancybox=True)
ax1.clabel(theplotcont1,inline=1,fontsize=30,manual=[(15,0),(15,1),(15,10),(5,10)])

#plt.xlim(1,10)
plt.ylim(-1,15)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Total allowed region ($\delta \in [0,2\pi)$) ($1\sigma$)',fontsize=36)
ax1.grid(True)

plt.show()

fig1, ax1 = plt.subplots(figsize=(18,12))
theplot=plt.contourf(xaxis,yaxis,datatotal,levels,alpha=0.2,colors='b')
#plt.contour(xaxis,yaxis,datatotal,levels,alpha=1,colors='b',linewidths=3,linestyles='dashed')
ax1.plot(xaxis,np.zeros(len(xaxis)),color='b',linewidth=3,alpha=0.2)

#plt.xlim(1,10)
plt.ylim(-1,15)
ax1.set_ylabel(r"$y_\eta/g^2_W$",fontsize=30)
ax1.set_xlabel(r"$m_\eta$ (TeV)",fontsize=30)
ax1.set_title(r'Total allowed region ($\delta \in [0,2\pi)$) ($1\sigma$)',fontsize=36)
ax1.grid(True)

plt.show()