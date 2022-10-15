import numpy as np
from Uaw import Uaw
from Wall import Wall
from Room import Room
from DistanceVector import DistVector


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
            tmp = w.Q[0] * vec.coords[0][0] + w.Q[1] * vec.coords[1][0] + w.Q[2] * vec.coords[2][0] + w.Q[3]
            tmp = tmp / vec
            a = vec.coords[0][0] - vec.ort[0] * tmp, vec.coords[1][0] - vec.ort[1] * tmp, vec.coords[2][0] - vec.ort[
                2] * tmp
            if ((a[0] <= np.max(w.x) and a[0] >= np.min(w.x)) and (a[1] <= np.max(w.Y) and a[1] >= np.min(w.Y)) and
                    (a[2] <= np.max(w.z) and a[2] >= np.min(w.z))):
                t.append(
                    [vec.coords[0][0] - vec.ort[0] * tmp, vec.coords[1][0] - vec.ort[1] * tmp,
                     vec.coords[2][0] - vec.ort[2] * tmp])

        return t

def calculateCloud(uaw:Uaw, walls):
    t=[]
    return t
