import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# x125/ x250/ x375/ x500/ x625/ x750/ x875/ 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

fs = 12  # fontsize
lw = 3  # fontsize
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(5, 8))

space = 0

#######################################################################################
# DFT
df1gc = pd.read_csv('ave_spectra_x125.dat', delimiter=r"\s+") 
df2gc = pd.read_csv('ave_spectra_x250.dat', delimiter=r"\s+") 
df3gc = pd.read_csv('ave_spectra_x375.dat', delimiter=r"\s+") 
df4gc = pd.read_csv('ave_spectra_x500.dat', delimiter=r"\s+") 
df5gc = pd.read_csv('ave_spectra_x625.dat', delimiter=r"\s+") 
df6gc = pd.read_csv('ave_spectra_x750.dat', delimiter=r"\s+") 
df7gc = pd.read_csv('ave_spectra_x875.dat', delimiter=r"\s+") 
df8gc = pd.read_csv('ave_spectra_x999.dat', delimiter=r"\s+") 

print(df1gc)
specmax1 = df1gc['Infinity'].max()
scale = 1 / specmax1 
df1gc['Infinity'] = df1gc['Infinity'] * scale
specmax2 = df2gc['Infinity'].max()
scale = 1 / specmax2 
df2gc['Infinity'] = df2gc['Infinity'] * scale
specmax3 = df3gc['Infinity'].max()
scale = 1 / specmax3 
df3gc['Infinity'] = df3gc['Infinity'] * scale
specmax4 = df4gc['Infinity'].max()
scale = 1 / specmax4 
df4gc['Infinity'] = df4gc['Infinity'] * scale
specmax5 = df5gc['Infinity'].max()
scale = 1 / specmax5 
df5gc['Infinity'] = df5gc['Infinity'] * scale
specmax6 = df6gc['Infinity'].max()
scale = 1 / specmax6 
df6gc['Infinity'] = df6gc['Infinity'] * scale
specmax7 = df7gc['Infinity'].max()
scale = 1 / specmax7 
df7gc['Infinity'] = df7gc['Infinity'] * scale
specmax8 = df8gc['Infinity'].max()
scale = 1 / specmax8 
df8gc['Infinity'] = df8gc['Infinity'] * scale


expx1gc = df1gc["x"]
expy1gc = df1gc["Infinity"]
expx2gc = df2gc["x"]
expy2gc = df2gc["Infinity"]+1
expx3gc = df3gc["x"]
expy3gc = df3gc["Infinity"]+2
expx4gc = df4gc["x"]
expy4gc = df4gc["Infinity"]+3
expx5gc = df5gc["x"]
expy5gc = df5gc["Infinity"]+4
expx6gc = df6gc["x"]
expy6gc = df6gc["Infinity"]+5
expx7gc = df7gc["x"]
expy7gc = df7gc["Infinity"]+6
expx8gc = df8gc["x"]
expy8gc = df8gc["Infinity"]+7

axs.plot(expx1gc, expy1gc, color='black', lw=lw)
axs.plot(expx2gc, expy2gc, color='black', lw=lw)
axs.plot(expx3gc, expy3gc, color='black', lw=lw)
axs.plot(expx4gc, expy4gc, color='black', lw=lw)
axs.plot(expx5gc, expy5gc, color='black', lw=lw)
axs.plot(expx6gc, expy6gc, color='black', lw=lw)
axs.plot(expx7gc, expy7gc, color='black', lw=lw)
axs.plot(expx8gc, expy8gc, color='black', lw=lw)
axs.xaxis.set_minor_locator(AutoMinorLocator(2))
# End DFT
#######################################################################################


#######################################################################################
# ML p20
df1can = pd.read_csv('ave_spectra_x125_ml_p20.dat', delimiter=r"\s+") 
df2can = pd.read_csv('ave_spectra_x250_ml_p20.dat', delimiter=r"\s+") 
df3can = pd.read_csv('ave_spectra_x375_ml_p20.dat', delimiter=r"\s+") 
df4can = pd.read_csv('ave_spectra_x500_ml_p20.dat', delimiter=r"\s+") 
df5can = pd.read_csv('ave_spectra_x625_ml_p20.dat', delimiter=r"\s+") 
df6can = pd.read_csv('ave_spectra_x750_ml_p20.dat', delimiter=r"\s+") 
df7can = pd.read_csv('ave_spectra_x875_ml_p20.dat', delimiter=r"\s+") 
df8can = pd.read_csv('ave_spectra_x999_ml_p20.dat', delimiter=r"\s+") 

print(df1can)
specmax1 = df1can['Infinity'].max() + space
scale = 1 / specmax1 
df1can['Infinity'] = df1can['Infinity'] * scale
specmax2 = df2can['Infinity'].max() + space
scale = 1 / specmax2 
df2can['Infinity'] = df2can['Infinity'] * scale
specmax3 = df3can['Infinity'].max() + space
scale = 1 / specmax3 
df3can['Infinity'] = df3can['Infinity'] * scale
specmax4 = df4can['Infinity'].max() + space
scale = 1 / specmax4 
df4can['Infinity'] = df4can['Infinity'] * scale
specmax5 = df5can['Infinity'].max() + space
scale = 1 / specmax5 
df5can['Infinity'] = df5can['Infinity'] * scale
specmax6 = df6can['Infinity'].max() + space
scale = 1 / specmax6 
df6can['Infinity'] = df6can['Infinity'] * scale
specmax7 = df7can['Infinity'].max() + space
scale = 1 / specmax7 
df7can['Infinity'] = df7can['Infinity'] * scale
specmax8 = df8can['Infinity'].max() + space
scale = 1 / specmax8 
df8can['Infinity'] = df8can['Infinity'] * scale


expx1can = df1can["x"]
expy1can = df1can["Infinity"]
expx2can = df2can["x"]
expy2can = df2can["Infinity"]+1
expx3can = df3can["x"]
expy3can = df3can["Infinity"]+2
expx4can = df4can["x"]
expy4can = df4can["Infinity"]+3
expx5can = df5can["x"]
expy5can = df5can["Infinity"]+4
expx6can = df6can["x"]
expy6can = df6can["Infinity"]+5
expx7can = df7can["x"]
expy7can = df7can["Infinity"]+6
expx8can = df8can["x"]
expy8can = df8can["Infinity"]+7

axs.plot(expx1can, expy1can, color='red', lw=lw)
axs.plot(expx2can, expy2can, color='red', lw=lw)
axs.plot(expx3can, expy3can, color='red', lw=lw)
axs.plot(expx4can, expy4can, color='red', lw=lw)
axs.plot(expx5can, expy5can, color='red', lw=lw)
axs.plot(expx6can, expy6can, color='red', lw=lw)
axs.plot(expx7can, expy7can, color='red', lw=lw)
axs.plot(expx8can, expy8can, color='red', lw=lw)
axs.xaxis.set_minor_locator(AutoMinorLocator(2))
# End ML
#######################################################################################

axs.text(-650, 8.1, r'100% DFT  ', fontsize=fs,  color='black', weight='bold')
axs.text(-650, 7.8, r' 20% DFT / 80% ML', fontsize=fs,  color='red', weight='bold')

axs.text(-630.1, 7.1, r'$x$=1.000', fontsize=fs-2,  color='black')
axs.text(-630.1, 6.1, r'$x$=0.875', fontsize=fs-2,  color='black')
axs.text(-630.1, 5.1, r'$x$=0.750', fontsize=fs-2,  color='black')
axs.text(-630.1, 4.1, r'$x$=0.625', fontsize=fs-2,  color='black')
axs.text(-630.1, 3.1, r'$x$=0.500', fontsize=fs-2,  color='black')
axs.text(-630.1, 2.1, r'$x$=0.375', fontsize=fs-2,  color='black')
axs.text(-630.1, 1.1, r'$x$=0.250', fontsize=fs-2,  color='black')
axs.text(-630.1, 0.1, r'$x$=0.125', fontsize=fs-2,  color='black')

axs.set_xlim([-630.0, -670.0])
axs.axes.yaxis.set_visible(False)

axs.text(-627, 3.5, r'NMR intensity (a.u.)', fontsize=fs,  color='black', rotation='vertical')
axs.text(-643, -1.2, '$^{119}$Sn $\delta_{\mathrm{iso}}$ (ppm)', fontsize=fs,  color='black')

plt.savefig('figure_8_NMR_spectra_Exp_versus_ML.png')
plt.savefig('figure_8_NMR_spectra_Exp_versus_ML.tiff', format='tiff')
plt.savefig('figure_8_NMR_spectra_Exp_versus_ML.pdf', format='pdf')
plt.show()
