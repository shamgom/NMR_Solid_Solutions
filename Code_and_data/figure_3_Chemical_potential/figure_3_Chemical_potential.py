import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil
import subprocess
import re
from scipy.interpolate import make_interp_spline, BSpline

wdir = os.getcwd()+'/'

# List of compositions for which to calculate the chemical potentials
xlist = [ '0.0625', '0.1250', '0.1875', '0.2500', '0.3125', '0.3750', '0.4375', '0.5000', '0.5625', '0.6250', '0.6870', '0.7500', '0.8125', '0.8750', '0.9375']

xlist = np.array(xlist)
print(xlist)
print(type(xlist))

dfT  = pd.read_csv(wdir+'/TEMPERATURES', header=None, delim_whitespace=True)
T = dfT.to_numpy(dtype=float)
print(T)

nx = len(xlist)
nT = len(T)
print('nx=',nx,'nT=',nT)

mumatrix = np.zeros((nx,nT))
print(mumatrix)

countx = 0
for x in xlist:
    print('Doing',x)
    x = str(x)
    os.makedirs(wdir+x, exist_ok=True)
    shutil.copyfile(wdir+'INGC_template',wdir+x+'/'+'INGC')
    shutil.copyfile(wdir+'TEMPERATURES',wdir+x+'/'+'TEMPERATURES')
    shutil.copyfile(wdir+'XSPEC',wdir+x+'/'+'XSPEC')
    shutil.copyfile(wdir+'sod_gcstat.sh',wdir+x+'/'+'sod_gcstat.sh')
    os.chdir(wdir+x)

    with open('INGC') as f:
        newtext=f.read().replace('xvalue',x)
    with open('INGC', "w") as f:
        f.write(newtext)

#    subprocess.call("sod_gcstat.sh")
#    We do not call sod_gcstat.sh here, in order to avoid errors creating the figure, but
#    it has to be called in order to create the files probabilities.dat inside each 
#    directory corresponding to the composition x
#    Note that sod_gcstat.sh needs access to the canocical calculations of the 16 compositions, since
#    it does: 
#
#cp ../can/n00/OUTSOD OUTSOD_00
#.
#.
#.
#cp ../can/n16/OUTSOD OUTSOD_16
#
#cp ../can/n00/ENERGIES ENERGIES_00
#.
#.
#.
#cp ../can/n16/ENERGIES ENERGIES_16
#
#cp ../can/n00/SPECTRA SPECTRA_00
#.
#.
#.
#cp ../can/n16/SPECTRA SPECTRA_16
#
# Once it has copied all these files, it can then run:
# gcstatsod


    with open(wdir+x+'/probabilities.dat') as f:
        lines = f.readlines()

    mu = []
    T  = []
    countT = 0
    for line in lines:
        line = line.lstrip().rstrip()
        line_sp = re.split(r'\s+',line)       
        if (len(line_sp) > 2) and line_sp[2] == 'mu':
           aux = float(line_sp[4])+750.4277
           mu.append(str(float(line_sp[4])+750.4277))
           mumatrix[countx][countT] = aux
           print('x=',x,'countT=',countT)
           countT+=1
        if (len(line_sp) > 1) and line_sp[0] == 'Temperature:':
           T.append(line_sp[3])
    countx+=1

# Write the file x_mu.dat, which has the data for this x
    myfile=wdir+x+'/x_mu.dat'
    ## If file exists, delete it ##
    if os.path.isfile(myfile):
        os.remove(myfile)
    else:    ## Show an error ##
        print("Error: %s file not found" % myfile)

    xmufile = open(wdir+x+'/x_mu.dat','a')
    xmufile.write('   x  '+'       T    '+'               mu   '+'\n')
    for i in range(len(T)):
        xmufile.write(x+'  '+str(T[i])+'  '+str(mu[i])+'\n')
    xmufile.close()




# Plot all the x_mu.dat files
xnew = np.linspace(0, 1, 1000)

fs = 20  # fontsize
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(11, 8))

plt.xlim(0,1)
plt.axhline(0, ls='--', color='black')

mumatrix = np.swapaxes(mumatrix,0,1)
print(mumatrix)

k=3
t=50
 
xlist = np.array(xlist).astype(float)
lsdashes =[ '(5, 20)', '(5, 15)', '(5, 10)', '(5, 5)']
for temp in range(nT):
    label = u"$\it{T}=$"+str(dfT[0][temp])+' K'
    plt.xticks(fontsize=fs)
    plt.yticks(fontsize=fs)
    # Do a spline
    spl1 = make_interp_spline(xlist, mumatrix[temp], k=k)  # type: BSpline
    power_smooth1 = spl1(xnew)
    plt.plot(xnew, power_smooth1, lw=3.0, label=label, linestyle='--', dashes=(temp*2+2,2))

plt.legend(fontsize=fs)
plt.xlabel(u"$\it{x}$", fontsize=fs)
plt.ylabel(u"$\it{\u03bc}$-$\it{\u03bc}$$_\mathrm{ref}$ (eV)", fontsize=fs)

axs.text(300, 5.15, r'Grand Canonical', fontsize=fs-2, color='b')

os.chdir(wdir)
plt.savefig('figure_3_Chemical_potential.png')
plt.savefig('figure_3_Chemical_potential.pdf', format='pdf')
plt.savefig('figure_3_Chemical_potential.tiff', format='tiff')
plt.show()
