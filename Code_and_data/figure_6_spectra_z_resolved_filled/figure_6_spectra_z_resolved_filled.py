import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

# Configuración inicial
fig, axs = plt.subplots(figsize=(9, 6))
fs = 16  # Tamaño de fuente base

# Lista de archivos
data_files = [
    'spectra_0p125_t1.dat',  # 0≤z≤4 (line)
    'ave_spectra_z0.dat',    # z=0 (fill)
    'ave_spectra_z1.dat',    # z=1 (fill)
    'ave_spectra_z2.dat',    # z=2 (fill)
    'ave_spectra_z3.dat'     # z=3 (fill)
]

# Cargar datos
data = []
for file in data_files:
    df = pd.read_csv(file, skiprows=1, sep='\s+', header=None,
                     names=['x','300.0','873.0','1273.0','1673.0','Infinite'])
    data.append(df)

# Estilos y etiquetas
colors = ['black', '#1f77b4', '#2ca02c', '#d62728', '#9467bd']
labels = [
    'Total', 
    'z=0', 
    'z=1', 
    'z=2', 
    'z=3'
]

# 1) Graficar línea global (0≤z≤4)
df0 = data[0]
axs.plot(df0['x'], df0['873.0'], lw=3, linestyle='-', c=colors[0], label=labels[0], zorder=1)

# 2) Rellenar los espectros de z=0 a z=3, en orden de fondo a delante
for idx in range(1, 5):
    df = data[idx]
    # llenar desde baseline=0 hasta la curva
    axs.fill_between(
        df['x'], df['873.0'], 
        color=colors[idx], alpha=0.4, 
        label=labels[idx], 
        zorder=idx+1
    )

# Ajustes del eje X
axs.set_xlim(-670, -640)
axs.invert_xaxis()  # Invertir eje X
axs.xaxis.set_minor_locator(AutoMinorLocator(2))
axs.tick_params(axis='x', labelsize=fs)  # <--- ESTA LÍNEA CAMBIA EL TAMAÑO DE LOS NÚMEROS DEL EJE X

# Etiqueta del eje X
axs.set_xlabel('$^{119}$Sn $\\delta_{\\mathrm{iso}}$ (ppm)', fontsize=fs, labelpad=10)

# Ocultar eje Y y añadir etiqueta manual
axs.yaxis.set_visible(False)
axs.annotate(
    'NMR intensity (a.u.)',
    xy=(-0.01, 0.5),
    xycoords='axes fraction',
    rotation=90,
    fontsize=fs,
    #fontsize=fs-2,
    va='center',
    ha='right'
)

# Leyenda
axs.legend(fontsize=fs, loc='upper left', framealpha=0.8)
#axs.legend(fontsize=fs-2, loc='upper left', framealpha=0.8)

plt.tight_layout()
plt.savefig('figure_6_spectra_z_resolved_filled.png', dpi=300)
plt.savefig('figure_6_spectra_z_resolved_filled.tiff', format='tiff')
plt.savefig('figure_6_spectra_z_resolved_filled.pdf', format='pdf')
plt.show()

