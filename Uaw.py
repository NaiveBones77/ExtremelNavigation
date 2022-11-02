import numpy as np
from DistanceVector import DistVector
import copy


class Uaw:

    def init_azline(self):
        x = self.coords[0] + np.cos(self.Az) * np.linspace(0, 12, 40)
        y = self.coords[1] + np.sin(self.Az) * np.linspace(0, 12, 40)
        z = self.coords[2] + np.linspace(0, 0, 40)
        self.azline[0] = x
        self.azline[1] = y
        self.azline[2] = z
        self.ort[0] = x[4] - x[0]
        self.ort[1] = y[4] - y[2]


    def __init__(self, x0, y0, z0, Az, Beta, Theta, ThetaDel, Gamma):
        self.count = 150
        self.matrixDist = []
        self.coords = np.array([x0, y0, z0])
        self.azline = np.zeros(shape=(3, 40))
        self.ort = np.array([0, 0, 0], dtype=np.float)
        self.distances = []
        self.Beta = Beta
        self.Theta = Theta
        self.Gamma = Gamma
        self.ThetaDel = ThetaDel
        self.Az = Az
        self.init_azline()
        self.init_distances2()

    def init_distances(self):
        angles = np.linspace(self.Az - self.Beta, self.Az + self.Beta, self.count)
        objs = [DistVector(self.coords, ang) for ang in angles]
        for angle in angles:
            a = copy.deepcopy(DistVector(self.coords, angle))
            self.distances.append(a)

    def init_distances2(self):
        Azimuth = np.linspace(self.Az - self.Beta, self.Az + self.Beta, self.count)
        Theta = np.linspace(self.Theta - self.ThetaDel, self.Theta + self.ThetaDel, self.count)
        for th in Theta:
            row = []
            for az in Azimuth:
                row.append(DistVector(self.coords, az, th))
            self.matrixDist.append(list(row))






