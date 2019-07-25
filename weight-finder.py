import numpy as np
import os
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()
    for line in lines:
        disp = line.split()
        print(disp)
