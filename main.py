import math

import numpy as np
import matplotlib.pyplot as plt
from Wall import Wall
from Room import Room
from Uaw import Uaw
from Simulation import *
from ExtremeNaviganion import *
from utils import *

#figure = plt.figure(figsize=plt.figaspect(2.))
figure = plt.figure()

w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])
w7 = Wall([-6, 8], [-3, 7], [8, 8], Q=[0, 0, 1, -8])
w8 = Wall([-6, 8], [-3, 7], [0, 0], Q=[0, 0, 1, 0])

walls = [w1, w2, w3, w4, w5, w6, w7, w8]
room = Room(walls)

#ax = figure.add_subplot(2, 1, 1)

Theta = np.deg2rad(0)
ThetaDel = np.deg2rad(30)

uaw = Uaw(0, 0, 4, np.deg2rad(0), Beta=1.47, Theta=Theta, ThetaDel=ThetaDel, Gamma=np.deg2rad(10))
#uaw1 = Uaw(0.5, 0.5, 4, np.deg2rad(7), Beta=1.47, Theta=Theta, ThetaDel=ThetaDel)

t = calculateCloud2(uaw, walls)
#t1 = calculateCloud(uaw1, walls)

# plotRoomWith2Distances(t, t1, [0, 0, np.deg2rad(0)], ax=ax)
#dispMap = calculateFunc(t, t1, axis=1, ax=ax)
#np.save('fourth.npy', dispMap)
# disp = calculateSelfRecognition(t, 1, ax)
#plotDispRoom()

ax = figure.add_subplot( projection='3d')

for w in room.walls:
    ax.plot_surface(w.X, w.Y, w.Z, rstride=1, cstride=1,
                    cmap='Blues')

ax.plot(uaw.azline[0], uaw.azline[1], zs=4, zdir='z')
ax.plot(uaw.matrixDist[0][0].x, uaw.matrixDist[0][0].y, zs=uaw.matrixDist[0][0].z)
ax.plot(uaw.matrixDist[0][-1].x, uaw.matrixDist[0][-1].y, zs=uaw.matrixDist[0][-1].z)
ax.plot(uaw.matrixDist[-1][0].x, uaw.matrixDist[-1][0].y, zs=uaw.matrixDist[-1][0].z)
ax.plot(uaw.matrixDist[-1][-1].x, uaw.matrixDist[-1][-1].y, zs=uaw.matrixDist[-1][-1].z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
