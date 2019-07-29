import numpy as np
import os
import sys

lin   = []
harm  = []
cub   = []
quart = []




with open(sys.argv[1]) as file:
    lines = file.readlines()
    n_disp = len(lines)
    n_coords = len(lines[0].split())
    coords = [[] for x in range(n_coords)]
    for n, line in enumerate(lines):
        disp = np.array(line.split()).astype(float)
        totdisp = np.sum(np.abs(disp))
        if totdisp ==0.02:
            quart.append(n)
        elif totdisp==0.015:
            cub.append(n)
        elif totdisp == 0.01:
            harm.append(n)
        elif totdisp == 0.005:
            lin.append(n)
        else:
            if n!=0:
                print(f'what structure is this? {n}')
        for coord in range(n_coords):
            if disp[coord] != 0.0:
                coords[coord].append(n)

#Formatted Output for easy copy+paste

print('Linear')
print('------')
print(len(lin), *lin,'\n\n')

print('Harmonic')
print('--------')
print(len(harm), *harm,'\n\n')

print('Cubic')
print('------')
print(len(cub), *cub,'\n\n')

print('Quartic')
print('-------')
print(len(quart), *quart,'\n\n')


for coord in range(n_coords):
    print(f'Coordinate #{coord}')
    print('----------------')
    print(len(coords[coord]), *coords[coord],'\n\n')




                
