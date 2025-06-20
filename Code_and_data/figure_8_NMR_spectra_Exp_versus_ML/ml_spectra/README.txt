This directory creates part of the files needed to create figure 8, in particular, the spectra calculated with ML
The process starts with the program:

generate_spectra_using_sodgc.sct

It reads the files in each nXX:

ENERGIES
PEAKS
XSPEC
INP2S
DATA

It then creates the SPECTRA files, which will be then also processed by the generate_spectra_using_sodgc.sct program, and 
the x*/ave_spectra_*dat created, they copied to where they will be used to create the figure, with names that are different to those
of the files created using DFT-obtained peaks, for instance:

cp x125/ave_spectra_x125.dat ../create_figure/ave_spectra_x125_ml_p20.dat

