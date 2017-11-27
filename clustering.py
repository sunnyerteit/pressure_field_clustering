"""
Test heatmap 3D-plot.
"""
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
import numpy as np
from sklearn.cluster import SpectralClustering
import random
from sklearn.preprocessing import normalize

with open('pressure.csv', 'rb') as f:
    reader = csv.reader(f)
    TEMP_LIST = list(reader)

X_DATA = []
Y_DATA = []
Z_DATA = []
P_DATA = []

DATA = []

for i in TEMP_LIST:
    DATA.append([int(i[0]), float(i[1]), float(
        i[2]), float(i[3]), float(i[4])])
    if random.random() > 0.90:
        X_DATA.append(float(i[1]))
        Y_DATA.append(float(i[2]))
        Z_DATA.append(float(i[3]))
        P_DATA.append(float(i[4]))

X_ARRAY = np.asarray(X_DATA)
Y_ARRAY = np.asarray(Y_DATA)
Z_ARRAY = np.asarray(Z_DATA)
P_ARRAY = np.asarray(P_DATA)

# DATA_ARRAY_TEMP = np.transpose(np.stack((Y_ARRAY, P_ARRAY)))
DATA_ARRAY_TEMP = P_ARRAY.reshape(-1, 1)
DATA_ARRAY_TEMP = np.transpose(np.stack((X_ARRAY, Y_ARRAY, Z_ARRAY, P_ARRAY)))
DATA_ARRAY = np.transpose(np.stack((X_ARRAY, Y_ARRAY, Z_ARRAY, P_ARRAY)))

N_ARRAY = normalize(DATA_ARRAY, axis=0)
print N_ARRAY[0]

print 'SPECTRAL'

SPECTRAL = SpectralClustering(n_clusters=2, eigen_solver='arpack', affinity="nearest_neighbors", n_init=100, n_jobs=-1)

SPECTRAL.fit(N_ARRAY)

LABELS = SPECTRAL.labels_

COLORS = ['b', 'r']

FIG = plt.figure()
AX = FIG.add_subplot(211, projection='3d')
AX2 = FIG.add_subplot(212, projection='3d')


for i in range(len(DATA_ARRAY)):
    if LABELS[i] == 0:
        AX.scatter(DATA_ARRAY[i][0], DATA_ARRAY[i][1], DATA_ARRAY[i][2], c=COLORS[LABELS[i]])
    else:
        AX2.scatter(DATA_ARRAY[i][0], DATA_ARRAY[i][1], DATA_ARRAY[i][2], c=COLORS[LABELS[i]])

plt.show()
