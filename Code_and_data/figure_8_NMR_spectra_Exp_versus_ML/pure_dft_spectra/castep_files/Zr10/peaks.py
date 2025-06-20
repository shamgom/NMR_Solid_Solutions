#for m in *.magres; do for Sn in `grep -H 'ms Sn' $m`; do echo $Sn; done; done

import glob
import os
import sys
import numpy as np
import re

xmin = -680
xmax = -620
npoints = 601 

def iso(T):
    return (T[0][0] + T[1][1] + T[2][2]) / 3

def e(magres_file_path):
    e = 0
    castep_file_path = '.'.join([magres_file_path.split('.')[0],"castep"])
    with open(castep_file_path, 'r') as cfile:
        for line in cfile.readlines():
            if line.strip().startswith("Total energy corrected for finite basis set"):
                e = line.split()[8]
    return e

magres_file_list = sys.argv[1:]
all_tensors = []
es = []
for magres_file in magres_file_list:
    tensors = []
    with open(magres_file, 'r') as magres:
        for line in magres.readlines():
            if line.startswith("ms Sn"):
                tensor = [ float(x) for x in line.split()[-9:] ]
                tensor = np.array(tensor).reshape((3,3))
                tensors.append(tensor)
    all_tensors.append(tensors)
    es.append(e(magres_file))
all_tensors = np.array(all_tensors)

sigma_isos = []
for s,structure in enumerate(list(all_tensors)):
    sigma_isos.append([])
    for T,tensor in enumerate(list(structure)):
        sigma_isos[s].append(iso(tensor))
sigma_isos = np.array(sigma_isos)
delta_isos = np.subtract(2596.5232,sigma_isos)
#delta_isos = np.subtract(sigma_isos,2596.5232)
print("Structure,Energy,Nucleus,delta_iso")
energiesFile = open("ENERGIES","w")
spectraFile = open("PEAKS","w")
INBROAD = open("INBROAD","w")
for s in range(len(magres_file_list)):
    energiesFile.write(es[s]+'\n')
    for d in range(len(delta_isos[s])):
        spectraFile.write(str(delta_isos[s][d])+' ')
        print("{:02d},{},Sn{:02d},{}".format(s+1,es[s],d+1,delta_isos[s][d]))
    spectraFile.write('\n')


INBROAD.write('# nconfs \n')
INBROAD.write(str(len(magres_file_list))+'\n')
INBROAD.write('# peaks \n')
INBROAD.write(str(len(delta_isos[0]))+'\n')
INBROAD.write('# xmin \n')
INBROAD.write(str(xmin)+'\n')
INBROAD.write('# xmax \n')
INBROAD.write(str(xmax)+'\n')
INBROAD.write('# npoints \n')
INBROAD.write(str(npoints)+'\n')
INBROAD.write('# broadening (sigma) \n')
INBROAD.write('0.85 \n')

xdatfile = open("XSPEC","w")
for i in range(npoints):
    xdatfile.write(str((xmin+i*(xmax-xmin)/(npoints-1)))+'\n')





"""
# Write the DATA files with the information about the cell parameters
magres_file_list = sys.argv[1:]
all_tensors = []
es = []
for magres_file in magres_file_list:
    tensors = []
    with open(magres_file, 'r') as magres:
        for line in magres.readlines():
            if line.startswith("lattice"):
                tensor = [ float(x) for x in line.split()[-9:] ]
                tensor = np.array(tensor).reshape((3,3))
                tensors.append(tensor)
    all_tensors.append(tensors)
    es.append(e(magres_file))
all_tensors = np.array(all_tensors)
"""

cell_params = np.zeros([1,3],dtype=float)

xdatfile = open("DATA","w")
xdatfile.write(str(4)+'\n')
print(type(cell_params))
print(cell_params)
for magres_file in magres_file_list:
    with open(magres_file, 'r') as magres:
        for line in magres.readlines():
            line = line.lstrip().rstrip()
            line_sp = re.split(r'\s+' , line)
            if line_sp[0] == "lattice":
            #if line.startswith("lattice"):
                xdatfile.write(line_sp[1]+' '+line_sp[5]+' '+line_sp[9]+' '+str(float(line_sp[1])*float(line_sp[5])*float(line_sp[9]))+'\n')

#for i in range():
#xdatfile.write(str(cell_params[0])+' '+str(cell_params[1])+' '+str(cell_params[2])+' \n')

#2
#60.5303 471.827005
#60.5864 471.649461
#60.5879 471.605946
