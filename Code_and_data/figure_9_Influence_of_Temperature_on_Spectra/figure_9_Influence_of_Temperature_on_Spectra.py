import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# x125/ x250/ x375/ x500/ x625/ x750/ x875/ 

fs = 10  # fontsize
fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(13, 8))

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


axs[0].plot(expx1, expy1, label='x125')
axs[0].plot(expx2, expy2, label='x250')
axs[0].plot(expx3, expy3, label='x250')
axs[0].plot(expx4, expy4, label='x250')
axs[0].plot(expx5, expy5, label='x250')
axs[0].plot(expx6, expy6, label='x250')
axs[0].plot(expx7, expy7, label='x250')
axs[0].plot(expx8, expy8, label='x250')
# End Experimental
#######################################################################################

#######################################################################################
# Grand Canonical 300
df1gc = pd.read_csv('ave_spectra_x125.dat', delimiter=r"\s+") 
df2gc = pd.read_csv('ave_spectra_x250.dat', delimiter=r"\s+") 
df3gc = pd.read_csv('ave_spectra_x375.dat', delimiter=r"\s+") 
df4gc = pd.read_csv('ave_spectra_x500.dat', delimiter=r"\s+") 
df5gc = pd.read_csv('ave_spectra_x625.dat', delimiter=r"\s+") 
df6gc = pd.read_csv('ave_spectra_x750.dat', delimiter=r"\s+") 
df7gc = pd.read_csv('ave_spectra_x875.dat', delimiter=r"\s+") 
df8gc = pd.read_csv('ave_spectra_x999.dat', delimiter=r"\s+") 

Temp = '300.0'
print(df1gc)
specmax1 = df1gc[Temp].max()
scale = 1 / specmax1 
df1gc[Temp] = df1gc[Temp] * scale

specmax2 = df2gc[Temp].max()
scale = 1 / specmax2 
df2gc[Temp] = df2gc[Temp] * scale

specmax3 = df3gc[Temp].max()
scale = 1 / specmax3 
df3gc[Temp] = df3gc[Temp] * scale

specmax4 = df4gc[Temp].max()
scale = 1 / specmax4 
df4gc[Temp] = df4gc[Temp] * scale

specmax5 = df5gc[Temp].max()
scale = 1 / specmax5 
df5gc[Temp] = df5gc[Temp] * scale

specmax6 = df6gc[Temp].max()
scale = 1 / specmax6 
df6gc[Temp] = df6gc[Temp] * scale

specmax7 = df7gc[Temp].max()
scale = 1 / specmax7 
df7gc[Temp] = df7gc[Temp] * scale

specmax8 = df8gc[Temp].max()
scale = 1 / specmax8 
df8gc[Temp] = df8gc[Temp] * scale


expx1gc = df1gc["x"]
expy1gc = df1gc[Temp]
               
expx2gc = df2gc["x"]
expy2gc = df2gc[Temp]+1
               
expx3gc = df3gc["x"]
expy3gc = df3gc[Temp]+2
               
expx4gc = df4gc["x"]
expy4gc = df4gc[Temp]+3
               
expx5gc = df5gc["x"]
expy5gc = df5gc[Temp]+4
               
expx6gc = df6gc["x"]
expy6gc = df6gc[Temp]+5
               
expx7gc = df7gc["x"]
expy7gc = df7gc[Temp]+6
               
expx8gc = df8gc["x"]
expy8gc = df8gc[Temp]+7

axs[1].plot(expx1gc, expy1gc, label='x125')
axs[1].plot(expx2gc, expy2gc, label='x250')
axs[1].plot(expx3gc, expy3gc, label='x250')
axs[1].plot(expx4gc, expy4gc, label='x250')
axs[1].plot(expx5gc, expy5gc, label='x250')
axs[1].plot(expx6gc, expy6gc, label='x250')
axs[1].plot(expx7gc, expy7gc, label='x250')
axs[1].plot(expx8gc, expy8gc, label='x250')
# End Grand Canonical
#######################################################################################



#######################################################################################
# Grand Canonical 873
df1gc = pd.read_csv('ave_spectra_x125.dat', delimiter=r"\s+") 
df2gc = pd.read_csv('ave_spectra_x250.dat', delimiter=r"\s+") 
df3gc = pd.read_csv('ave_spectra_x375.dat', delimiter=r"\s+") 
df4gc = pd.read_csv('ave_spectra_x500.dat', delimiter=r"\s+") 
df5gc = pd.read_csv('ave_spectra_x625.dat', delimiter=r"\s+") 
df6gc = pd.read_csv('ave_spectra_x750.dat', delimiter=r"\s+") 
df7gc = pd.read_csv('ave_spectra_x875.dat', delimiter=r"\s+") 
df8gc = pd.read_csv('ave_spectra_x999.dat', delimiter=r"\s+") 

Temp = '873.0'
print(df1gc)
specmax1 = df1gc[Temp].max()
scale = 1 / specmax1 
df1gc[Temp] = df1gc[Temp] * scale

specmax2 = df2gc[Temp].max()
scale = 1 / specmax2 
df2gc[Temp] = df2gc[Temp] * scale

specmax3 = df3gc[Temp].max()
scale = 1 / specmax3 
df3gc[Temp] = df3gc[Temp] * scale

specmax4 = df4gc[Temp].max()
scale = 1 / specmax4 
df4gc[Temp] = df4gc[Temp] * scale

specmax5 = df5gc[Temp].max()
scale = 1 / specmax5 
df5gc[Temp] = df5gc[Temp] * scale

specmax6 = df6gc[Temp].max()
scale = 1 / specmax6 
df6gc[Temp] = df6gc[Temp] * scale

specmax7 = df7gc[Temp].max()
scale = 1 / specmax7 
df7gc[Temp] = df7gc[Temp] * scale

specmax8 = df8gc[Temp].max()
scale = 1 / specmax8 
df8gc[Temp] = df8gc[Temp] * scale


expx1gc = df1gc["x"]
expy1gc = df1gc[Temp]
               
expx2gc = df2gc["x"]
expy2gc = df2gc[Temp]+1
               
expx3gc = df3gc["x"]
expy3gc = df3gc[Temp]+2
               
expx4gc = df4gc["x"]
expy4gc = df4gc[Temp]+3
               
expx5gc = df5gc["x"]
expy5gc = df5gc[Temp]+4
               
expx6gc = df6gc["x"]
expy6gc = df6gc[Temp]+5
               
expx7gc = df7gc["x"]
expy7gc = df7gc[Temp]+6
               
expx8gc = df8gc["x"]
expy8gc = df8gc[Temp]+7

axs[2].plot(expx1gc, expy1gc, label='x125')
axs[2].plot(expx2gc, expy2gc, label='x250')
axs[2].plot(expx3gc, expy3gc, label='x250')
axs[2].plot(expx4gc, expy4gc, label='x250')
axs[2].plot(expx5gc, expy5gc, label='x250')
axs[2].plot(expx6gc, expy6gc, label='x250')
axs[2].plot(expx7gc, expy7gc, label='x250')
axs[2].plot(expx8gc, expy8gc, label='x250')
# End Grand Canonical
#######################################################################################

#######################################################################################
# Grand Canonical Infinity
df1gc = pd.read_csv('ave_spectra_x125.dat', delimiter=r"\s+") 
df2gc = pd.read_csv('ave_spectra_x250.dat', delimiter=r"\s+") 
df3gc = pd.read_csv('ave_spectra_x375.dat', delimiter=r"\s+") 
df4gc = pd.read_csv('ave_spectra_x500.dat', delimiter=r"\s+") 
df5gc = pd.read_csv('ave_spectra_x625.dat', delimiter=r"\s+") 
df6gc = pd.read_csv('ave_spectra_x750.dat', delimiter=r"\s+") 
df7gc = pd.read_csv('ave_spectra_x875.dat', delimiter=r"\s+") 
df8gc = pd.read_csv('ave_spectra_x999.dat', delimiter=r"\s+") 

Temp = 'Infinity'
print(df1gc)
specmax1 = df1gc[Temp].max()
scale = 1 / specmax1 
df1gc[Temp] = df1gc[Temp] * scale

specmax2 = df2gc[Temp].max()
scale = 1 / specmax2 
df2gc[Temp] = df2gc[Temp] * scale

specmax3 = df3gc[Temp].max()
scale = 1 / specmax3 
df3gc[Temp] = df3gc[Temp] * scale

specmax4 = df4gc[Temp].max()
scale = 1 / specmax4 
df4gc[Temp] = df4gc[Temp] * scale

specmax5 = df5gc[Temp].max()
scale = 1 / specmax5 
df5gc[Temp] = df5gc[Temp] * scale

specmax6 = df6gc[Temp].max()
scale = 1 / specmax6 
df6gc[Temp] = df6gc[Temp] * scale

specmax7 = df7gc[Temp].max()
scale = 1 / specmax7 
df7gc[Temp] = df7gc[Temp] * scale

specmax8 = df8gc[Temp].max()
scale = 1 / specmax8 
df8gc[Temp] = df8gc[Temp] * scale


expx1gc = df1gc["x"]
expy1gc = df1gc[Temp]
               
expx2gc = df2gc["x"]
expy2gc = df2gc[Temp]+1
               
expx3gc = df3gc["x"]
expy3gc = df3gc[Temp]+2
               
expx4gc = df4gc["x"]
expy4gc = df4gc[Temp]+3
               
expx5gc = df5gc["x"]
expy5gc = df5gc[Temp]+4
               
expx6gc = df6gc["x"]
expy6gc = df6gc[Temp]+5
               
expx7gc = df7gc["x"]
expy7gc = df7gc[Temp]+6
               
expx8gc = df8gc["x"]
expy8gc = df8gc[Temp]+7

axs[3].plot(expx1gc, expy1gc, label='x125')
axs[3].plot(expx2gc, expy2gc, label='x250')
axs[3].plot(expx3gc, expy3gc, label='x250')
axs[3].plot(expx4gc, expy4gc, label='x250')
axs[3].plot(expx5gc, expy5gc, label='x250')
axs[3].plot(expx6gc, expy6gc, label='x250')
axs[3].plot(expx7gc, expy7gc, label='x250')
axs[3].plot(expx8gc, expy8gc, label='x250')
# End Grand Canonical
#######################################################################################

axs[0].set_title('Experiment', fontsize=fs)
axs[1].set_title('Grand Canonical, T=300 K', fontsize=fs)
axs[2].set_title('Grand Canonical, T=873 K', fontsize=fs)
axs[3].set_title('Grand Canonical, Infinite T', fontsize=fs)

axs[0].set_xlim([-625.0, -675.0])
axs[1].set_xlim([-625.0, -675.0])
axs[2].set_xlim([-625.0, -675.0])
axs[3].set_xlim([-625.0, -675.0])

axs[0].axes.yaxis.set_visible(False)
axs[1].axes.yaxis.set_visible(False)
axs[2].axes.yaxis.set_visible(False)
axs[3].axes.yaxis.set_visible(False)

color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
axs[0].text(-625, 7.1, 'x=1.000', fontsize=fs-2,  color=color[7])
axs[0].text(-625, 6.1, 'x=0.875', fontsize=fs-2,  color=color[6])
axs[0].text(-625, 5.1, 'x=0.750', fontsize=fs-2,  color=color[5])
axs[0].text(-625, 4.1, 'x=0.625', fontsize=fs-2,  color=color[4])
axs[0].text(-625, 3.1, 'x=0.500', fontsize=fs-2,  color=color[3])
axs[0].text(-625, 2.1, 'x=0.375', fontsize=fs-2,  color=color[2])
axs[0].text(-625, 1.1, 'x=0.250', fontsize=fs-2,  color=color[1])
axs[0].text(-625, 0.1, 'x=0.125', fontsize=fs-2,  color=color[0])

axs[0].text(-615, 4, r'NMR intensity (arbitrary units)', fontsize=fs,  color='black', rotation='vertical')
axs[1].text(-670, -1.2,   '$^{119}$Sn $\delta_{\mathrm{iso}}$ (ppm)', fontsize=fs,  color='black')

plt.savefig('figure_9_Influence_of_Temperature_on_Spectra.png')
plt.savefig('figure_9_Influence_of_Temperature_on_Spectra.tiff', format='tiff')
plt.show()

