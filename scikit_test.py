"""
Multiple linear regression.
"""
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

def heat_map(x_value, y_value, z_value):
    "Prints out linear heatmap."
    return x_value + y_value + z_value

# Define points in space.
X_POINTS = np.linspace(0, 10, num=11, endpoint=True)
Y_POINTS = np.linspace(0, 10, num=11, endpoint=True)
Z_POINTS = np.linspace(0, 10, num=11, endpoint=True)

# Empty lists.
X_DATA = []
Y_DATA = []
Z_DATA = []
P_DATA = []

# Point and pressure vectors.
for i in X_POINTS:
    for j in Y_POINTS:
        for k in Z_POINTS:
            X_DATA.append(i)
            Y_DATA.append(j)
            Z_DATA.append(k)
            P_DATA.append(heat_map(i, j, k) + 5)

# Convert to numpy.
X_ARRAY = np.asarray(X_DATA)
Y_ARRAY = np.asarray(Y_DATA)
Z_ARRAY = np.asarray(Z_DATA)
P_ARRAY = np.asarray(P_DATA)

# Add input to X.
POINTS_ARRAY = np.column_stack((X_ARRAY, Y_ARRAY, Z_ARRAY))

# Convert to polynomial.
POLY = PolynomialFeatures(degree=2)
POLY_FIT = POLY.fit_transform(POINTS_ARRAY)

# Regression.
REG = linear_model.LinearRegression()
REG.fit(POLY_FIT, P_ARRAY)

print POLY_FIT
print POLY.get_feature_names()
print REG.coef_
print REG.intercept_
