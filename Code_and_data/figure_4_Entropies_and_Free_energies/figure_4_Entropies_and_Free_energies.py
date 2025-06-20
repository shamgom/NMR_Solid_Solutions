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

wdir = os.getcwd()+'/'

n_atoms_fu = 8
################################################################################
# TOP PANEL
data  = pd.read_csv(wdir+'entropies_versus_temperature.csv',      sep = ';')

T     = data.iloc[1:,0]
Sgc   = data.iloc[1:,1]*1000/n_atoms_fu*96.4853
Sc    = data.iloc[1:,2]*1000/n_atoms_fu*96.4853
ideal = data.iloc[1:,3]*1000/n_atoms_fu*96.4853

T     = T.astype(float)
Sgc   = Sgc.astype(float)
Sc    = Sc.astype(float)
ideal = ideal.astype(float)

print(T)
print(Sgc)
print(Sc)
print(ideal)

fs = 12  # fontsize
ps = 40
lw = 4
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(7, 9))

axs[0].text(-90,13.0, r'a)',   fontsize=fs+2)

color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
axs[0].text(310,10.15, r'Grand-canonical', fontsize=fs,  color='black')
axs[0].text(310, 8.50, r'Canonical', fontsize=fs,  color='red')
axs[0].text(310,11.95, r'Correct full-disorder limit', fontsize=fs, color='black')

axs[0].plot(T,Sgc,'-',lw=lw, color='black')
axs[0].legend(frameon=False, loc='upper center', fontsize=fs)

label = 'Canonical'
axs[0].plot(T,Sc,'-', lw=lw, color='red')
axs[0].legend(frameon=False, loc='lower right', fontsize=fs)
plt.xticks(rotation=0,fontsize=fs+2)
plt.yticks(rotation=0,fontsize=fs+2)
axs[0].text(750, 1.5, "$\it{T}$ (K)", fontsize=fs, color='black', ha='center')
axs[0].text(-50, 6.10, "$S_{\\mathrm{mix}}$ (J mol$^{-1}$ K$^{-1}$)", fontsize=fs, color='black', rotation='vertical')


axs[0].plot(T,ideal,'--', lw=lw, color='grey')
axs[0].set_yticks(np.arange(2, 14, 1))
axs[0].set_xlim(100,1400)
axs[0].set_ylim(3,13)
axs[0].tick_params(axis='x', labelsize=fs)
axs[0].tick_params(axis='y', labelsize=fs)


# END TOP PANEL
################################################################################


################################################################################
# BOTTOM PANEL

wdir = os.getcwd()+'/'

enegc   = pd.read_csv(wdir+'enthalpies_and_energies_versus_composition_grandcanonical.txt',      header=None, sep = ';')
enecan  = pd.read_csv(wdir+'enthalpies_and_energies_versus_composition_canonical.txt',      header=None, sep = ';')

T = 873.0

##############################################
# Read the energy files
x       = enegc.iloc[:,0].to_numpy()
energc  = enegc.iloc[:,2].to_numpy()
energc  = (energc - x*energc[-1] - (1-x) * energc[0]) * 96.4853 / n_atoms_fu

xcan    = enecan.iloc[:,0].to_numpy() / 16
enercan = enecan.iloc[:,2].to_numpy()
enercan = (enercan - xcan*enercan[-1] - (1-xcan) * enercan[0]) * 96.4853 / n_atoms_fu
##############################################

print(x)
print(energc)
print(xcan)
print(enercan)

axs[1].set_xlim(0,1)
axs[1].set_ylim(-12.0,4.0)
axs[1].axhline(0, ls='--', color='black')


##################################################################
# Enthalpy
axs[1].scatter(xcan,enercan, color='red', s=ps, zorder=2)
plt.ylabel("$\it{\Delta G}$$_\mathrm{mix}$, $\it{\Delta H}$$_\mathrm{mix}$ (kJ mol$^{-1}$)", fontsize=fs)
plt.xlabel("$\it{x}$ in La$_{2}$(Sn$_{x}$Zr$_{1-x})_{2}$O$_{7}$", fontsize=fs)
plt.xticks(rotation=0,fontsize=fs)
plt.yticks(rotation=0,fontsize=fs)

# Do a spline
xnew = np.linspace(0, 1, 300) 
spl1 = make_interp_spline(x, energc, k=3)  # type: BSpline
power_smooth1 = spl1(xnew)
axs[1].plot(xnew, power_smooth1, lw=3, color='black', zorder=1)


##################################################################
# Free energy
Ggc  = enegc.iloc[:,4].to_numpy()
Ggc  = -(Ggc) * T * 96.4853 / n_atoms_fu
Gcan = enecan.iloc[:,4].to_numpy() * 96.4853 / n_atoms_fu
Gcan = -(Gcan) * T
print(x)
print(Ggc)
print(xcan)
print(Gcan)

axs[1].scatter(xcan,Gcan, s=ps, color='red')
plt.xticks(rotation=0,fontsize=fs)
plt.yticks(rotation=0,fontsize=fs)

# Do a spline
xnew = np.linspace(0, 1, 300) 
spl1 = make_interp_spline(x, Ggc, k=3)  # type: BSpline
power_smooth1 = spl1(xnew)
axs[1].plot(xnew, power_smooth1, lw=3, color='black', zorder=2)

axs[1].text(-0.15, 4.00, r'b)',   fontsize=fs+2)
axs[1].text(0.39, 2.40, r'$\Delta H$$_\mathrm{mix}$ Canonical',       fontsize=fs, color='red')
axs[1].text(0.35, 0.45, r'$\Delta H$$_\mathrm{mix}$ Grand-canonical', fontsize=fs, color='black')
axs[1].text(0.39, -7.5, r'$\Delta G$$_\mathrm{mix}$ Canonical',       fontsize=fs, color='red')
axs[1].text(0.35, -11.1, r'$\Delta G$$_\mathrm{mix}$ Grand-canonical', fontsize=fs, color='black')

# END BOTTOM PANEL
################################################################################
plt.savefig('figure_4_Entropies_and_Free_energies.png')
plt.savefig('figure_4_Entropies_and_Free_energies.tiff', format='tiff')
plt.savefig('figure_4_Entropies_and_Free_energies.pdf', format='pdf')

plt.show()

