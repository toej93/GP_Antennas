#!/bin/python

#Translate XF output into readable AraSim input. Jorge Torres, Sep 2017.

import math
import itertools
import sys
import shutil
import numpy
import glob

input_file = "pattern.uan"#+str(n) #Name of the input file
output_file ="evol_antenna_model.dat"
patt = open(output_file, "w+")
patt.write(" Theta "+'\t'+" Phi "+'\t'+" Gain(dB)     "+'\t'+"   Gain     "+'\t'+"    Phase(deg)"+'\n')#Header
with open(input_file, 'r') as f:
    for _ in xrange(17):
        next(f)
    for line in f:
        line = line.strip()
        columns = line.split()
        theta = float(columns[0]) #particle ID (encoded)
        #Check if particles are inside the 5mx5m square
        phi = float(columns[1]) #In cm
        t_gain = float(columns[2])
        p_gain = float(columns[3])
        t_phase = float(columns[4])
        p_phase = float(columns[5])
      #  gain_tot = float(t_gain+p_gain)
        patt.write(str(theta)+' \t '+str(phi)+' \t '+str(t_gain)+'     \t   '+str(t_gain)+'     \t    '+str(t_phase)+'\n')
f.close()
patt.close()
        
 
