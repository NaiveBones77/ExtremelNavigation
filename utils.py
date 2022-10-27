import numpy as np


def plotDispRoom():

    disp = np.load('second.npy', allow_pickle=True)
    vals = disp[:, 0]
    cond = disp[:, 1]
    a = np.zeros(shape=(disp.shape[0], 4))
    for i in range(disp.shape[0]):
        tmp = cond[i]
        tmp.append(vals[i])
        a[i] = np.array(tmp)

    minindex = vals.argmin()

    b = a[a[:, 0] == -1.]
    print(disp.shape)

plotDispRoom()