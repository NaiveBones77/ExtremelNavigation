from Wall import Wall
import numpy as np

class Room:
    def __init__(self, walls):
        self.walls = walls

    def add_wall(self, w):
        self.walls.append(w)


