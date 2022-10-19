import math

import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Room import Room
from Uaw import Uaw
from Simulation import *
from ExtremeNaviganion import *


figure = plt.figure()
ax = figure.add_subplot(projection='3d')

w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])

walls = [w1, w2, w3, w4, w5, w6]
room = Room(walls)

uaw = Uaw(0, 0, 4, 0, Beta=1.47)

t = calculateCloud(uaw, walls)

calculateFunc(np.array([0, 0, 0]), t[0][0])

for w in room.walls:
    ax.plot_surface(w.X, w.Y, w.Z, rstride=1, cstride=1,
                    cmap='Blues')

ax.plot(uaw.azline[0], uaw.azline[1], zs = 4, zdir ='z')
ax.plot(uaw.distances[0].x, uaw.distances[0].y, zs = 4, zdir ='z')
ax.plot(uaw.distances[149].x, uaw.distances[149].y, zs = 4, zdir ='z')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


plt.show()
