import numpy as np


def plotDispRoom():

    disp = np.load('fourth.npy', allow_pickle=True)
    vals = disp[:, 0]
    cond = disp[:, 1]
    a = np.zeros(shape=(disp.shape[0], 4))
    for i in range(disp.shape[0]):
        tmp = cond[i]
        tmp.append(vals[i])
        a[i] = np.array(tmp)

    minindex = vals.argmin()

    b = np.argmin(a[:, 3])
    print(a[b])

#plotDispRoom()


def plotRoomWith2Distances(t1, t2, shift, ax=None):
    angxs1 = np.zeros(shape=(len(t1), 2))
    angxs2 = np.zeros(shape=(len(t2), 2))
    for i in range(len(t1)):
        angxs1[i] = np.array([t1[i][0][0], t1[i][0][1]])  # for calculateDist2
        angxs2[i] = np.array([t2[i][0][0], t2[i][0][1]])
        #angxs1[i] = np.array([t1[i][0], t1[i][1]])
        #angxs2[i] = np.array([t2[i][0], t2[i][1]])

    X1 = np.array([np.cos(angxs1[:, 1])*angxs1[:, 0], np.sin(angxs1[:, 1])*angxs1[:, 0]])
    X2 = np.array([np.cos(angxs2[:, 1] + shift[2])*angxs2[:, 0] + shift[0], np.sin(angxs2[:, 1] + shift[2])*angxs2[:, 0] + shift[1]] )

    if (ax is not None):
        ax.plot(X1[0, :], X1[1,: ])
        ax.plot(X2[0, :], X2[1,: ])
        ax.grid()
        ax.legend()
    print(X1)

def plotRoomWith2Points(t1, t2, ax=None):
    xy1 = np.zeros(shape=(len(t1), 2))
    xy2 = np.zeros(shape=(len(t2), 2))
    for i in range(len(t1)):
        xy1[i] = np.array([t1[i][0][0], t1[i][0][1]])
        xy2[i] = np.array([t2[i][0][0], t2[i][0][1]])

    if (ax is not None):
        ax.plot(xy1[0, :], xy1[1,: ])
        ax.plot(xy2[0, :], xy2[1,: ])
        ax.grid()
        ax.legend()
    print(xy1)


