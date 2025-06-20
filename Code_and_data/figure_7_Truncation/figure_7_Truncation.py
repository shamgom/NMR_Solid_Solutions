import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil
import subprocess
import re
from scipy.interpolate import make_interp_spline, BSpline
import math
import pylab
from scipy.special import gamma
from matplotlib.ticker import FormatStrFormatter


# x125/ x250/ x375/ x500/ x625/ x750/ x875/ 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(6, 8) )

###################################################################################################
# First, panel with probs

wdir = os.getcwd()+'/'

probs2 = pd.read_csv(wdir+'figure_probs.csv', sep = ';', skiprows=1, header=None)
print(probs2)
x2  = probs2.iloc[:,0].to_numpy()
p12 = probs2.iloc[:,1].to_numpy()
p22 = probs2.iloc[:,2].to_numpy()


fs = 12  # fontsize
ps = 40  
ps2 = 45  

label = 'x=0.125'
axs[0].scatter(x2,p12, s=ps2)
#axs.scatter(x2,p12,label="$\it{x}$=0.125", s=ps2)
label = 'x=0.750'
axs[0].scatter(x2,p22, s=ps2)
#axs.scatter(x2,p22,label="$\it{x}$=0.500", s=ps2)
#label = 'x=0.875'
#axs.scatter(x2,p32, s=ps2)

#axs.legend()
#axs[0].legend(frameon=False, loc='upper center', ncol=1, fontsize=fs)

axs[0].set(xlabel='$\it{n}$', ylabel='Probability')

axs[0].yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

#axs[0].ylabel('Probability', fontsize=fs)

#axs.legend(frameon=False, loc='upper center', ncol=3, fontsize=fs)

#plt.xlabel("$\it{n}$", fontsize=fs)
#plt.xticks(rotation=0,fontsize=fs)
#plt.yticks(rotation=0,fontsize=fs)
#plt.ylabel('Probability', fontsize=fs)


color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

N = 16
###########
# x = 0.125
comp = 0.125
ax = pylab.linspace(0, 16, 300)

#y = (N!/(N-n)!n!)(x^n)(1-x)^(N-n)
y = ( gamma(N+1) / ( gamma(N-ax+1) * (gamma(ax+1)) ) ) * (comp**ax) * (1-comp)**(N-ax)

axs[0].plot(ax,y, color=color[0], lw=3)
#pylab.plot(ax, y, ls='-', label='$\Binomial$',   color=color[0], lw=3)
###########
###########
# x = 0.75
comp = 0.75
#y = (N!/(N-n)!n!)(x^n)(1-x)^(N-n)
y = ( gamma(N+1) / ( gamma(N-ax+1) * (gamma(ax+1)) ) ) * (comp**ax) * (1-comp)**(N-ax)

axs[0].plot(ax,y, color=color[1], lw=3)
#pylab.plot(ax, y, ls='-', label='$\Binomial$',   color=color[1], lw=3)
###########

axs[0].text(2.8,  0.25, r'$\it{x}$=0.125', fontsize=fs-2,  color=color[0])
axs[0].text(11.8, 0.25, r'$\it{x}$=0.75' , fontsize=fs-2,  color=color[1])

axs[0].text(-2.9, 0.3, r'a)',   fontsize=fs+2)

#plt.show()




###################################################################################################
# Second, panel with truncation

#fs = 12  # fontsize
#fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))


# full denotes no truncation, t0 
data = []
data.append(pd.read_csv('spectra_0p125_full.dat',skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
data.append(pd.read_csv('spectra_0p125_t0.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
data.append(pd.read_csv('spectra_0p125_t1.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
#data.append(pd.read_csv('spectra_0p125_t2.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
data.append(pd.read_csv('spectra_0p750_full.dat',skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
data.append(pd.read_csv('spectra_0p750_t0.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
data.append(pd.read_csv('spectra_0p750_t1.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))
#data.append(pd.read_csv('spectra_0p750_t2.dat',  skiprows=1, sep='\s+',header=None, names=['x','300.0','873.0','1273.0','1673.0', 'Infinite']))

print(data)
print(type(data))
print(type(data[0]))
print(type(data[1]['873.0']))
print(data[0]['873.0'])
print(data[0]['x'])

scale = 1.0
specmax = []
for i in range(len(data)):
    specmax.append(data[i]['873.0'].max())
    scale = 1 / specmax[i] 
    data[i]['873.0'] = data[i]['873.0'] * scale

color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
axs[1].set_xlim(-640,-670)
axs[1].plot(data[0]['x'], data[2]['873.0'], lw=3, c='red', label='0≤$n$≤4')
axs[1].plot(data[0]['x'], data[0]['873.0'], lw=3, c='black', label='No truncation \n(0≤$n$≤16)')
#axs[1].plot(data[0]['x'], data[0]['873.0'], lw=3, c='black', label='No truncation \n(0≤n≤16)')
#axs[1].text(-651, -0.31,  '$^{119}$Sn $\delta_{iso}$ (ppm)', fontsize=fs,  color='black')


axs[2].set_xlim(-630,-670)
axs[2].plot(data[3]['x'], data[5]['873.0'], lw=3, c='red', label='11≤$n$≤13')
axs[2].plot(data[3]['x'], data[3]['873.0'], lw=3, c='black', label='No truncation \n(0≤$n$≤16)')


axs[1].text(-642,  0.8,    r'$\it{x}$=0.125',                fontsize=fs+0,  color='black')
axs[2].text(-633,  0.8,    r'$\it{x}$=0.750',                fontsize=fs+0,  color='black')
axs[1].axes.yaxis.set_visible(False)
axs[2].axes.yaxis.set_visible(False)
axs[1].axes.xaxis.set_minor_locator(AutoMinorLocator(2))
axs[2].axes.xaxis.set_minor_locator(AutoMinorLocator(2))

#axs[0].text(8, -0.08,  '$\it{n}$', fontsize=fs,  color='black')
#axs[1].set(xlabel='$^{119}$Sn $\delta_{iso} (ppm)$', ylabel='NMR intensity (a.u.)')
axs[1].text(-638.6,  0.089,    r'NMR intensity (a.u.)',                fontsize=fs-2,  color='black', rotation='vertical')
axs[2].text(-628.2,  0.089,    r'NMR intensity (a.u.)',                fontsize=fs-2,  color='black', rotation='vertical')
#axs[1].text(-651, -0.31,  '$^{119}$Sn $\delta_{iso}$ (ppm)', fontsize=fs,  color='black')
#axs[2].text(-645, -0.31,  '$^{119}$Sn $\delta_{iso}$ (ppm)', fontsize=fs,  color='black')
axs[1].text(-651, -0.31,   '$^{119}$Sn $\delta_{\mathrm{iso}}$ (ppm)', fontsize=fs,  color='black')
axs[2].text(-645, -0.31,   '$^{119}$Sn $\delta_{\mathrm{iso}}$ (ppm)', fontsize=fs,  color='black')


axs[1].text(-636, 0.8, r'b)',   fontsize=fs+2)
axs[2].text(-626, 0.8, r'c)',   fontsize=fs+2)

axs[1].legend()
axs[2].legend()

fig.tight_layout()

plt.savefig('figure_7_Truncation.png')
plt.savefig('figure_7_Truncation.tiff', format='tiff')
plt.savefig('figure_7_Truncation.pdf', format='pdf')
plt.show()

