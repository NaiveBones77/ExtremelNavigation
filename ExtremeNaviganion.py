import numpy as np


def calculateSelfRecognition(t:np.ndarray, axis):
    return 0

def calculateFunc(X:np.ndarray, D2:np.ndarray):
    vec = np.array(X[0], X[1])
    d2 = D2[0]
    phi = X[2]
    alfa2 = D2[1]

    A = np.array([
        [np.cos(phi), -np.sin(phi)],
        [np.sin(phi), np.cos(phi)]
    ])


    d2js = np.array([
        [d2*np.cos(alfa2)],
        [d2*np.sin(alfa2)]
    ])

    vec2 = vec + A.dot(d2js)

    alfa1 = np.pi + np.arctan2(vec2[1], vec2[0])

    deltad = np.abs(np.sqrt(np.linalg.norm(vec2)) - d2)

    func = deltad / 1

    return func
