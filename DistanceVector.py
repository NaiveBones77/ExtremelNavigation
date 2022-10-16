import numpy as np
import copy

class DistVector:
    coords = np.array([0, 0, 0])
    azline = np.zeros(shape=(3, 40))
    ort = np.array([0, 0, 0], dtype=np.float)
    def __init__(self, coords, Az):
        self.coords = coords
        self.Az = Az
        self.x = self.coords[0] + np.cos(self.Az) * np.linspace(0, 12, 40)
        self.y = self.coords[1] + np.sin(self.Az) * np.linspace(0, 12, 40)
        self.z = self.coords[2] + np.linspace(0, 0, 40)
        self.azline = copy.deepcopy(self.azline)
        self.azline[0] = self.x
        self.azline[1] = self.y
        self.azline[2] = self.z
        self.ort = copy.deepcopy(self.ort)
        self.ort[0] = self.x[4] - self.x[0]
        self.ort[1] = self.y[4] - self.y[2]
        self.ort[2] = 0