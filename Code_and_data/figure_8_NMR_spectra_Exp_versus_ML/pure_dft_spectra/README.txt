This directory creates part of the files needed to create figure 8, in particular, the spectra calculated with pure DFT data, with no
ML performed.
The process starts with the program:

get_struct_Ene_NMR_from_CASTEP_files.py

It reads the output files from CASTEP, which are located in different directories, on for each number of Zr atoms in the system.
The information is put in a series of files that will be read by SOD, such as:

ENERGIES
PEAKS
XSPEC
INP2S
DATA

These files are placed in each directory.

Then, these files will be used, but inside the directory:

sod_files

The script cp_ENERGIES_SPECTRA_DATA.sct copies the relevant files inside the different directories in the sod_files directory. Note
that the files in the sod_files directory are placed in directories that are not named as a function of the number of Zr, but of Sn atoms, i.e.,
n00 is the system with 0 Sn atoms (therefore 16 Zr), n01 is the system with 1 Sn atom (therefore 15 Zr), etc.

Once we have the files in the nXX directories, we can calculate the average spectra for each composition, nXX, using the canonical ensemble.
To do that we run the script:

generate_spectra_using_sodgc.sct

This script goes to all the directories, one by one. The files OUTSOD and TEMPERATURES must be placed in each one before running the script. The rest of the files 
needed are the ones that were copied by the script cp_ENERGIES_SPECTRA_DATA.sct.

Once the x*/ave_spectra_*dat are created, they are copied to where they will be used to create the figure:

cp x*/ave_spectra_*dat ../../../create_figure/.


