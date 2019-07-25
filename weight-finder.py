import numpy as np
import os
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()
    n_disp = len(lines)
    n_coords = len(lines[0].split())
    for line in lines:
        disp = line.split()
        
