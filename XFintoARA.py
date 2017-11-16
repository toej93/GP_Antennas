#!/bin/python

#Translate XF output into readable AraSim input. Jorge Torres, Nov 2017.
#You need to have all your XF output files in the same foler, with the standard name dipole_freq_MHz.uan

#Translate XF output into readable AraSim input. Jorge Torres, Sep 2017.

import math
import itertools
import sys
import shutil
import numpy
import glob

freq_min = 100 #Initial frequency
freq_max = 1000 #Final frequency
freq_step = 20 #Step between frequencies
freq = freq_min #Define the dynamical variable frequency
output_file ="evol_antenna_model.dat" #Name of the output file, the one that goes into AraSim
patt = open(output_file, "w")# Open file to write on it
input_file = "pattern.uan"#+str(n) #Name of the input file
output_file ="evol_antenna_model.dat"
patt = open(output_file, "w+")
while (freq<=freq_max): 
    input_file = "/Users/neutrino/Dropbox/GP_Antennas/OSU_internal/Dipole_FreqSweep/dipole_"+str(freq)+"_MHz.uan" #+str(n) #Name of the input file. Need to modify with your directory path
    print(input_file) #Prints the name of the input file
    patt.write("freq : "+str(freq)+".00 MHz"+'\n'+"SWR : 1.965000"+'\n')#Header for each iteration
    if(freq==freq_min):
        patt.write(" Theta "+'\t'+" Phi "+'\t'+" Gain(dB)     "+'\t'+"   Gain     "+'\t'+"    Phase(deg)"+'\n')#Header
    with open(input_file, 'r') as f:
        for _ in xrange(17): 
            next(f) #Skips the first 17 lines of the XF file, which are useless for us.
        for line in f:
                line = line.strip() #Identify lines.
                columns = line.split() #Identify columns.
#Here I identify the veriables with their respective columns in the XF file
                theta = int(columns[0])
                phi = int(columns[1]) 
                dB_t_gain = float(columns[2])
                t_gain = math.pow(10,dB_t_gain/10)
                dB_p_gain = float(columns[3])
                p_gain = math.pow(10,dB_p_gain/10)
                t_phase = float(columns[4])
                p_phase = float(columns[5])
                #  gain_tot = float(t_gain+p_gain)
                patt.write(str(theta)+' \t '+str(phi)+' \t '+str(dB_t_gain)+'     \t   '+str(t_gain)+'     \t    '+str(t_phase)+'\n') #Write data on the new file
    freq+=freq_step
#Close everything
f.close()
patt.close()
        
 
