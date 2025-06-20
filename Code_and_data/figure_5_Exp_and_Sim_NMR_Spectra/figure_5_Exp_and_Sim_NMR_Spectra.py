import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# x125/ x250/ x375/ x500/ x625/ x750/ x875/ 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

fs = 14  # fontsize
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 8))

#######################################################################################
# Experimental
df1 = pd.read_csv('exp_data_x125.csv', delimiter=';', names=['expx','expspec']) 
df2 = pd.read_csv('exp_data_x250.csv', delimiter=';', names=['expx','expspec']) 
df3 = pd.read_csv('exp_data_x375.csv', delimiter=';', names=['expx','expspec']) 
df4 = pd.read_csv('exp_data_x500.csv', delimiter=';', names=['expx','expspec']) 
df5 = pd.read_csv('exp_data_x625.csv', delimiter=';', names=['expx','expspec']) 
df6 = pd.read_csv('exp_data_x750.csv', delimiter=';', names=['expx','expspec']) 
df7 = pd.read_csv('exp_data_x875.csv', delimiter=';', names=['expx','expspec']) 
df8 = pd.read_csv('exp_data_x999.csv', delimiter=';', names=['expx','expspec']) 

specmax1 = df1['expspec'].max()
scale = 1 / specmax1 
df1['expspec'] = df1['expspec'] * scale
specmax2 = df2['expspec'].max()
scale = 1 / specmax2 
df2['expspec'] = df2['expspec'] * scale
specmax3 = df3['expspec'].max()
scale = 1 / specmax3 
df3['expspec'] = df3['expspec'] * scale
specmax4 = df4['expspec'].max()
scale = 1 / specmax4 
df4['expspec'] = df4['expspec'] * scale
specmax5 = df5['expspec'].max()
scale = 1 / specmax5 
df5['expspec'] = df5['expspec'] * scale
specmax6 = df6['expspec'].max()
scale = 1 / specmax6 
df6['expspec'] = df6['expspec'] * scale
specmax7 = df7['expspec'].max()
scale = 1 / specmax7 
df7['expspec'] = df7['expspec'] * scale
specmax8 = df8['expspec'].max()
scale = 1 / specmax8 
df8['expspec'] = df8['expspec'] * scale

expx1= df1["expx"]
expy1= df1["expspec"]
expx2= df2["expx"]
expy2= df2["expspec"]+1
expx3= df3["expx"]
expy3= df3["expspec"]+2
expx4= df4["expx"]
expy4= df4["expspec"]+3
expx5= df5["expx"]
expy5= df5["expspec"]+4
expx6= df6["expx"]
expy6= df6["expspec"]+5
expx7= df7["expx"]
expy7= df7["expspec"]+6
expx8= df8["expx"]
expy8= df8["expspec"]+7


axs[0].plot(expx1, expy1)
axs[0].plot(expx2, expy2)
axs[0].plot(expx3, expy3)
axs[0].plot(expx4, expy4)
axs[0].plot(expx5, expy5)
axs[0].plot(expx6, expy6)
axs[0].plot(expx7, expy7)
axs[0].plot(expx8, expy8)

axs[0].xaxis.set_minor_locator(AutoMinorLocator(2))

# End Experimental
#######################################################################################



#######################################################################################
# Canonical
df1can = pd.read_csv('ave_spectra_x125_can.dat', delimiter=r"\s+") 
df2can = pd.read_csv('ave_spectra_x250_can.dat', delimiter=r"\s+") 
df3can = pd.read_csv('ave_spectra_x375_can.dat', delimiter=r"\s+") 
df4can = pd.read_csv('ave_spectra_x500_can.dat', delimiter=r"\s+") 
df5can = pd.read_csv('ave_spectra_x625_can.dat', delimiter=r"\s+") 
df6can = pd.read_csv('ave_spectra_x750_can.dat', delimiter=r"\s+") 
df7can = pd.read_csv('ave_spectra_x875_can.dat', delimiter=r"\s+") 
df8can = pd.read_csv('ave_spectra_x999_can.dat', delimiter=r"\s+") 

print(df1can)
specmax1 = df1can['873.0'].max()
scale = 1 / specmax1 
df1can['873.0'] = df1can['873.0'] * scale
specmax2 = df2can['873.0'].max()
scale = 1 / specmax2 
df2can['873.0'] = df2can['873.0'] * scale
specmax3 = df3can['873.0'].max()
scale = 1 / specmax3 
df3can['873.0'] = df3can['873.0'] * scale
specmax4 = df4can['873.0'].max()
scale = 1 / specmax4 
df4can['873.0'] = df4can['873.0'] * scale
specmax5 = df5can['873.0'].max()
scale = 1 / specmax5 
df5can['873.0'] = df5can['873.0'] * scale
specmax6 = df6can['873.0'].max()
scale = 1 / specmax6 
df6can['873.0'] = df6can['873.0'] * scale
specmax7 = df7can['873.0'].max()
scale = 1 / specmax7 
df7can['873.0'] = df7can['873.0'] * scale
specmax8 = df8can['873.0'].max()
scale = 1 / specmax8 
df8can['873.0'] = df8can['873.0'] * scale


expx1can = df1can["x"]
expy1can = df1can["873.0"]
expx2can = df2can["x"]
expy2can = df2can["873.0"]+1
expx3can = df3can["x"]
expy3can = df3can["873.0"]+2
expx4can = df4can["x"]
expy4can = df4can["873.0"]+3
expx5can = df5can["x"]
expy5can = df5can["873.0"]+4
expx6can = df6can["x"]
expy6can = df6can["873.0"]+5
expx7can = df7can["x"]
expy7can = df7can["873.0"]+6
expx8can = df8can["x"]
expy8can = df8can["873.0"]+7

axs[1].plot(expx1can, expy1can)
axs[1].plot(expx2can, expy2can)
axs[1].plot(expx3can, expy3can)
axs[1].plot(expx4can, expy4can)
axs[1].plot(expx5can, expy5can)
axs[1].plot(expx6can, expy6can)
axs[1].plot(expx7can, expy7can)
axs[1].plot(expx8can, expy8can)
axs[1].xaxis.set_minor_locator(AutoMinorLocator(2))
# End Canonical
#######################################################################################

#######################################################################################
# Grand Canonical
df1gc = pd.read_csv('ave_spectra_x125.dat', delimiter=r"\s+") 
df2gc = pd.read_csv('ave_spectra_x250.dat', delimiter=r"\s+") 
df3gc = pd.read_csv('ave_spectra_x375.dat', delimiter=r"\s+") 
df4gc = pd.read_csv('ave_spectra_x500.dat', delimiter=r"\s+") 
df5gc = pd.read_csv('ave_spectra_x625.dat', delimiter=r"\s+") 
df6gc = pd.read_csv('ave_spectra_x750.dat', delimiter=r"\s+") 
df7gc = pd.read_csv('ave_spectra_x875.dat', delimiter=r"\s+") 
df8gc = pd.read_csv('ave_spectra_x999.dat', delimiter=r"\s+") 

print(df1gc)
specmax1 = df1gc['873.0'].max()
scale = 1 / specmax1 
df1gc['873.0'] = df1gc['873.0'] * scale
specmax2 = df2gc['873.0'].max()
scale = 1 / specmax2 
df2gc['873.0'] = df2gc['873.0'] * scale
specmax3 = df3gc['873.0'].max()
scale = 1 / specmax3 
df3gc['873.0'] = df3gc['873.0'] * scale
specmax4 = df4gc['873.0'].max()
scale = 1 / specmax4 
df4gc['873.0'] = df4gc['873.0'] * scale
specmax5 = df5gc['873.0'].max()
scale = 1 / specmax5 
df5gc['873.0'] = df5gc['873.0'] * scale
specmax6 = df6gc['873.0'].max()
scale = 1 / specmax6 
df6gc['873.0'] = df6gc['873.0'] * scale
specmax7 = df7gc['873.0'].max()
scale = 1 / specmax7 
df7gc['873.0'] = df7gc['873.0'] * scale
specmax8 = df8gc['873.0'].max()
scale = 1 / specmax8 
df8gc['873.0'] = df8gc['873.0'] * scale


expx1gc = df1gc["x"]
expy1gc = df1gc["873.0"]
expx2gc = df2gc["x"]
expy2gc = df2gc["873.0"]+1
expx3gc = df3gc["x"]
expy3gc = df3gc["873.0"]+2
expx4gc = df4gc["x"]
expy4gc = df4gc["873.0"]+3
expx5gc = df5gc["x"]
expy5gc = df5gc["873.0"]+4
expx6gc = df6gc["x"]
expy6gc = df6gc["873.0"]+5
expx7gc = df7gc["x"]
expy7gc = df7gc["873.0"]+6
expx8gc = df8gc["x"]
expy8gc = df8gc["873.0"]+7

axs[2].plot(expx1gc, expy1gc)
axs[2].plot(expx2gc, expy2gc)
axs[2].plot(expx3gc, expy3gc)
axs[2].plot(expx4gc, expy4gc)
axs[2].plot(expx5gc, expy5gc)
axs[2].plot(expx6gc, expy6gc)
axs[2].plot(expx7gc, expy7gc)
axs[2].plot(expx8gc, expy8gc)
axs[2].xaxis.set_minor_locator(AutoMinorLocator(2))

# End Grand Canonical
#######################################################################################

axs[0].set_title('Experiment', fontsize=fs-2)
axs[1].set_title('Canonical', fontsize=fs-2)
axs[2].set_title('Grand Canonical', fontsize=fs-2)

axs[0].text(0.41, 1.05, '(a)', transform=axs[0].transAxes, fontsize=fs)
axs[1].text(0.41, 1.05, '(b)', transform=axs[1].transAxes, fontsize=fs)
axs[2].text(0.41, 1.05, '(c)', transform=axs[2].transAxes, fontsize=fs)

axs[0].axes.yaxis.set_visible(False)
axs[1].axes.yaxis.set_visible(False)
axs[2].axes.yaxis.set_visible(False)

axs[0].set_xlim([-625.0, -675.0])
axs[1].set_xlim([-625.0, -675.0])
axs[2].set_xlim([-625.0, -675.0])
axs[0].tick_params(axis='x', labelsize=fs-2)
axs[1].tick_params(axis='x', labelsize=fs-2)
axs[2].tick_params(axis='x', labelsize=fs-2)

color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
axs[0].text(-625, 7.1, r'$x$=1.000', fontsize=fs-4,  color=color[7])
axs[0].text(-625, 6.1, r'$x$=0.875', fontsize=fs-4,  color=color[6])
axs[0].text(-625, 5.1, r'$x$=0.750', fontsize=fs-4,  color=color[5])
axs[0].text(-625, 4.1, r'$x$=0.625', fontsize=fs-4,  color=color[4])
axs[0].text(-625, 3.1, r'$x$=0.500', fontsize=fs-4,  color=color[3])
axs[0].text(-625, 2.1, r'$x$=0.375', fontsize=fs-4,  color=color[2])
axs[0].text(-625, 1.1, r'$x$=0.250', fontsize=fs-4,  color=color[1])
axs[0].text(-625, 0.1, r'$x$=0.125', fontsize=fs-4,  color=color[0])

axs[0].text(-617, 3.5, r'NMR intensity (a.u.)', fontsize=fs,  color='black', rotation='vertical')
axs[1].text(-635, -1.1, '$^{119}$Sn $\delta_{\mathrm{iso}}$ (ppm)', fontsize=fs,  color='black')

plt.savefig('figure_5_Exp_and_Sim_NMR_Spectra.png')
plt.savefig('figure_5_Exp_and_Sim_NMR_Spectra.tiff', format='tiff')
plt.savefig('figure_5_Exp_and_Sim_NMR_Spectra.pdf', format='pdf')
plt.show()
