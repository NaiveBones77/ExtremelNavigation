import numpy as np

class DistVector:
    coords = np.array([0, 0, 0])
    azline = np.zeros(shape=(3, 40))
    ort = np.array([0, 0, 0], dtype=np.float)
    def __init__(self, coords, Az):
        self.coords = coords
        self.Az = Az
        x = self.coords[0] + np.cos(self.Az) * np.linspace(0, 12, 40)
        y = self.coords[1] + np.sin(self.Az) * np.linspace(0, 12, 40)
        z = self.coords[2] + np.linspace(0, 0, 40)
        self.azline[0] = x
        self.azline[1] = y
        self.azline[2] = z
        self.ort[0] = x[4] - x[0]
        self.ort[1] = y[4] - y[2]
        self.ort[2] = 0