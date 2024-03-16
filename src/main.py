'''This program is part of Zhu Jingjing's graduation thesis,
   aimed at generating automated path planning for micro and nano fibers on non-flat surfaces
   (in this case, part of a cylinder, mimicking human bones),
   thereby fabricating highly controllable scaffolds.  '''


import math
import numpy as np

def cylinder_m(Length, interval, r, h, ang_c, Z_up, F, f):
    x = math.sqrt(r ** 2 - (r - h) ** 2)
    print('Chord length is ' + str(2 * x))

    Z0 = -(r - h)
    X0 = 0
    n = 2 * math.asin((2 * x) / (2 * r))
    ang_n = n / ang_c
    b_ang = (90 * math.pi) / 180 + (n / 4)
    s_ang = math.pi / 2 - (n / 4)
    print('For ' + str(ang_c) + ' segments, each segment length on the circular surface is ' + str(ang_n * r))

    X_C = []
    Z_C = []

    for i in np.arange(b_ang, s_ang, -ang_n):
        Z = (r * math.sin(i) + Z0) - h
        X = r * math.cos(i) + X0
        X_C.append(X)
        Z_C.append(Z)

    RX_C = list(reversed(X_C))
    RZ_C = list(reversed(Z_C))
    Y_C = np.arange(0, Length, interval)
    print('Total iterations for Y: ' + str(len(Y_C)) + '\n')

    L_i = 0

    while L_i < len(Y_C):
        for XX, ZZ in zip(X_C if L_i % 2 == 0 else RX_C, Z_C if L_i % 2 == 0 else RZ_C):
            f.write(f'G1 X{XX} Y{Y_C[L_i]} Z{ZZ + Z_up} F{F}\n')
        L_i += 1

    for X_i in np.arange(0, len(X_C), 1):
        for YY in Y_C if X_i % 2 == 0 else reversed(Y_C):
            f.write(f'G1 X{X_C[X_i]} Y{YY} Z{Z_C[X_i] + Z_up} F{F}\n')


# Open file for writing
file = open(r'C:\Users\dell\Desktop\cylinder.txt', 'w')
F = 800  # Speed
r = 35  # Radius
Z = 0  # Initial Z height
h = 10  # Cylinder cutting height
L = 26  # Cylinder length
xianc = 48.98  # Chord length
interval = 0.5  # Interval
layers = 10  # Number of layers
Z_up = 3  # Initial Z offset

for i in range(layers):
    cylinder_m(L, interval, r, h, 11.59, Z_up, F, file)
    Z_up += 1
    file.write(f"G1 X{xianc / 4} Y{L - 1} Z{Z + 1} F{F}\n")
    file.write(f"G1 X-{xianc / 4 + 2} Y{L - 1} Z{Z + 1} F{F}\n")

file.close()
print("Processing complete. Press Enter to exit.")
   
