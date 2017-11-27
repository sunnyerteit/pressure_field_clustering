"""
Test heatmap 3D-plot.
"""
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
import random
import numpy as np

with open('pressure.csv', 'rb') as f:
    reader = csv.reader(f)
    TEMP_LIST = list(reader)

X_DATA = []
Y_DATA = []
Z_DATA = []
P_DATA = []

DATA = []

for i in TEMP_LIST:
    DATA.append([int(i[0]), float(i[1]), float(i[2]), float(i[3]), float(i[4])])
    if random.random() > 0.93:
        X_DATA.append(float(i[1]))
        Y_DATA.append(float(i[2]))
        Z_DATA.append(float(i[3]))
        P_DATA.append(float(i[4]))



FIG = plt.figure(figsize=(8, 6))
AX = FIG.add_subplot(111, projection='3d')

COLMAP = cm.ScalarMappable(cmap=cm.plasma)
COLMAP.set_array(np.asarray(P_DATA))


YG = AX.scatter(X_DATA, Y_DATA, Z_DATA, c=cm.plasma(np.asarray(P_DATA)/max(P_DATA)))
CB = FIG.colorbar(COLMAP)

AX.set_xlabel('X Label')
AX.set_ylabel('Y Label')
AX.set_zlabel('Z Label')

plt.show()
