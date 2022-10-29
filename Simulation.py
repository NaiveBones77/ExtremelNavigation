import math

import numpy as np
from Uaw import Uaw
from Wall import Wall
from Room import Room
from DistanceVector import DistVector
from numpy.random import normal


def run():
    w1 = Wall([-6, 6], [7, 7], [0, 8], Q=[0, 1, 0, -7])
    w2 = Wall([6, 6], [4, 7], [0, 8], Q=[1, 0, 0, -6])
    w3 = Wall([6, 8], [4, 4], [0, 8], Q=[0, 1, 0, -4])
    w4 = Wall([8, 8], [-3, 4], [0, 8], Q=[1, 0, 0, -8])
    w5 = Wall([-6, 8], [-3, -3], [0, 8], Q=[0, -1, 0, -3])
    w6 = Wall([-6, -6], [-3, 7], [0, 8], Q=[-1, 0, 0, -6])

    walls = [w1, w2, w3, w4, w5, w6]
    room = Room(walls)

    uaw = Uaw(1, 1, 4, 0.6, 0.6)

    t = []
    for w in walls:
        vec = w.Q[0] * uaw.ort[0] + w.Q[1] * uaw.ort[1] + w.Q[2] * uaw.ort[2]
        if (vec != 0):
            tmp = w.Q[0] * uaw.azline[0][0] + w.Q[1] * uaw.azline[1][0] + w.Q[2] * uaw.azline[2][0] + w.Q[3]
            tmp = tmp / vec
            a = uaw.azline[0][0] - uaw.ort[0] * tmp, uaw.azline[1][0] - uaw.ort[1] * tmp, uaw.azline[2][0] - uaw.ort[
                2] * tmp
            if ((a[0] <= np.max(w.x) and a[0] >= np.min(w.x)) and (a[1] <= np.max(w.Y) and a[1] >= np.min(w.Y)) and
                    (a[2] <= np.max(w.z) and a[2] >= np.min(w.z))):
                t.append(
                    [uaw.azline[0][0] - uaw.ort[0] * tmp, uaw.azline[1][0] - uaw.ort[1] * tmp,
                     uaw.azline[2][0] - uaw.ort[2] * tmp])


def calculateDist(walls, vec: DistVector):
    t = []
    for w in walls:
        aa = w.Q[0] * vec.ort[0] + w.Q[1] * vec.ort[1] + w.Q[2] * vec.ort[2]
        if (aa != 0):
            tmp = w.Q[0] * vec.azline[0][0] + w.Q[1] * vec.azline[1][0] + w.Q[2] * vec.azline[2][0] + w.Q[3]
            tmp = tmp / aa
            a = vec.azline[0][0] - vec.ort[0] * tmp, vec.azline[1][0] - vec.ort[1] * tmp, vec.azline[2][0] - vec.ort[
                2] * tmp
            if ((a[0] <= np.max(w.x) + 0.1 and a[0] >= np.min(w.x) - 0.1)
                    and (a[1] <= np.max(w.Y) + 0.1 and a[1] >= np.min(w.Y) -0.1)
                    and (a[2] <= np.max(w.z) + 0.1 and a[2] >= np.min(w.z) -0.1)):
                vec_st = np.array([w.x[-1], w.Y[-1]])
                vec_dist = np.array([vec.ort[0], vec.ort[1]])
                c = np.dot(vec_dist, vec_st)/np.linalg.norm(vec_st) / np.linalg.norm(vec_dist)
                ang = np.arccos(np.clip(c, -1, 1))
                if (ang < np.pi / 2):
                    t.append(a)

    return t

def calculateCloud(uaw:Uaw, walls):
    t=[]
    iter = 0
    for dist in uaw.distances:
        t.append(calculateDist3(walls, dist, uaw.Az,))
        iter+=1
        if (iter == 41):
            print('deb')
    return t

def calculateDist2(walls, vec:DistVector, mu =0, std = 0.02):
    t = []
    xyz0 = np.array([vec.coords[0], vec.coords[1]])
    delta = 0.01
    for w in walls:
        vec.ort = vec.ort / np.linalg.norm(vec.ort)
        n = np.array([w.Q[0], w.Q[1], w.Q[2]])
        t0 = - ((np.dot(vec.coords, n)) + w.Q[3]) / np.dot(vec.ort, n)
        if (np.dot(vec.ort, n) != 0 and t0 >= 0 ):

            x = vec.coords[0] + t0*vec.ort[0]
            y = vec.coords[1] + t0*vec.ort[1]
            z = vec.coords[2] + t0*vec.ort[2]

            if ((x <= np.max(w.x) + delta and x >= np.min(w.x) - delta)
                    and (y <= np.max(w.Y) + delta and y >= np.min(w.Y) - delta)
                    and (z <= np.max(w.z) + delta and z >= np.min(w.z) - delta)):
                A = np.array([
                    [np.cos(vec.Az), -np.sin(vec.Az)],
                    [np.sin(vec.Az), np.cos(vec.Az)]
                ])
                xyz0 = A.dot(xyz0)
                xyz = A.dot(np.array([x, y]))
                #dist = np.linalg.norm([x, y, z]) + normal(mu, std)
                #dist = np.sqrt((x - vec.coords[0])**2 + (y - vec.coords[1])**2 + (z - vec.coords[2])**2) + normal(mu, std)
                dist = np.sqrt((xyz[0] - xyz0[0])**2 + (xyz[1] - xyz0[1])**2) + normal(mu, std)
                t.append(np.array([dist, vec.Az]))
    if len(t) > 1:
        t.pop()
    return t

def calculateDist3(walls, vec:DistVector, Az =0, mu =0, std = 0.02):
    t = []
    index = 0
    A = np.array([
        [np.cos(Az), -np.sin(Az), 0],
        [np.sin(Az), np.cos(Az), 0],
        [0, 0, 1]
    ])
    vec.coords = A.dot(vec.coords)
    #vec.ort = A.dot(vec.ort)
    delta = 0.01
    for w in walls:
        vec.ort = vec.ort / np.linalg.norm(vec.ort)
        n = A.dot(np.array([w.Q[0], w.Q[1], w.Q[2]]))
        t0 = - ((np.dot(vec.coords, n)) + w.Q[3]) / np.dot(vec.ort, n)
        if (np.dot(vec.ort, n) != 0 and t0 >= 0 ):
            x = vec.coords[0] + t0*vec.ort[0]
            y = vec.coords[1] + t0*vec.ort[1]
            z = vec.coords[2] + t0*vec.ort[2]


            leftPoint = np.array([w.x[0], w.Y[0], w.z[0]])
            rightPoint = np.array([w.x[-1], w.Y[-1], w.z[-1]])

            leftPoint = A.dot(leftPoint)
            rightPoint = A.dot(rightPoint)

            bounds = np.stack((leftPoint, rightPoint))

            if ( (x <= np.max(bounds[:, 0]) + delta and x >= np.min(bounds[:, 0]) - delta)
            and (y <= np.max(bounds[:, 1]) + delta and y >= np.min(bounds[:, 1]) - delta) and
                 ( z <= np.max(bounds[:, 2])+ delta and z >= np.min(bounds[:, 2]) - delta)):
                dist = np.sqrt((x - vec.coords[0]) ** 2 + (y - vec.coords[1]) ** 2
                               + (z - vec.coords[2]) ** 2)
                t.append(np.array([dist, vec.Az]))
    if len(t) > 1:
         t.pop()
    return t
