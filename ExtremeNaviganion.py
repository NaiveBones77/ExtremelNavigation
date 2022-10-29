import numpy as np
from matplotlib import pyplot as plt

def calculateSelfRecognition(t, axis, ax=None):

    # автокорреляционная функция
    disp = []

    # варьируемый параметр из функционала
    vars = np.linspace(-0.5, 0.5)
    if (axis == 2):
        vars = np.linspace(-1.54, 1.54, 150)

    # массив функционалов
    deltaD = np.zeros(shape=(vars.size, 3))
    deltaD[:, axis] = vars

    #Массив для поиска коэффициента знаменателя в уравнении (4)
    angxs = np.zeros(shape= (len(t), 2))
    for i in range(len(t)):
        angxs[i] = np.array([t[i][0][0], t[i][0][1]])

    # делаем перебор по всем возможным вариациям функционала по всему облаку расстояний
    for var in deltaD:
        func = 0
        res = []
        c = 0

        # перебор по каждому расстоянию
        for dist in t:
            deltaX = var[:2]
            deltaX.shape = (2,1)
            phi = var[2]
            alfa2 = dist[0][1]
            d2 = dist[0][0]

            A =  np.array([
                [np.cos(phi), -np.sin(phi)],
                [np.sin(phi), np.cos(phi)]
            ])

            d2js = np.array([
                [d2*np.cos(alfa2)],
                [d2*np.sin(alfa2)]
            ])

            X1js = deltaX + A.dot(d2js)

            alfa1 = np.arctan2(X1js[1], X1js[0])

            d1 = 0

            for elem in angxs:
                if (np.abs(elem[1] - alfa1)  <  0.01):
                    d1 = elem[0]
                    c += 1
                    break
                else:
                    d1 = 0
            if (d1 != 0):
                deltad = np.abs(np.sqrt(np.power(X1js[0], 2) + np.power(X1js[1], 2)) - d1)
            else:
                deltad = 0

            func += deltad

        func /= c
        res.append(func)
        res.append(var)
        disp.append(res)
    x = []
    y = []
    for elem in disp:
        x.append(elem[1][axis])
        y.append(elem[0][0])
    if (ax is not None):
        ax.plot(x, y)
        ax.grid()

    return disp

def calculateFunc(t1, t2, axis, ax=None):

    #Корреляционная функция
    disp = []

    # Массив для поиска коэффициента знаменателя в уравнении (4)
    angxs = np.zeros(shape=(len(t1), 2))
    for i in range(len(t1)):
        angxs[i] = np.array([t1[i][0][0], t1[i][0][1]])

    xspace = np.linspace(-1, 0, 5)
    xspace1 = np.linspace(0, 1, 5)
    xspace = np.concatenate((xspace, xspace1))

    yspace = np.linspace(-1, 0, 5)
    yspace1 = np.linspace(0, 1, 5)
    yspace = np.concatenate((yspace, yspace1))

    phispace = np.linspace(np.deg2rad(-10), 0, 5)
    phispace1 = np.linspace(0, np.deg2rad(10), 5)
    phispace = np.concatenate((phispace, phispace1))


    xx, yy, phi_ = np.meshgrid(xspace, yspace, phispace)
    xyphi = np.stack([xx, yy, phi_])

    for x in xspace:
        for y in yspace:
            for phi in phispace:
                func = 0
                res = []
                c = 0
                for dist in t2:
                    deltaX = np.array([x, y])
                    deltaX.shape = (2, 1)
                    alfa2 = dist[0][1]
                    d2 = dist[0][0]

                    A = np.array([
                        [np.cos(phi), -np.sin(phi)],
                        [np.sin(phi), np.cos(phi)]
                    ])

                    d2js = np.array([
                        [d2 * np.cos(alfa2)],
                        [d2 * np.sin(alfa2)]
                    ])

                    X1js = deltaX + A.dot(d2js)


                    alfa1 = np.arctan2(X1js[1], X1js[0])

                    d1 = 0

                    ind = np.argmin(np.abs(angxs - alfa1)[:, 1])
                    if (np.abs(angxs[ind, 1] - alfa1) < 0.01):
                        d1 = angxs[ind, 0]
                        c += 1

                    # for elem in angxs:
                    #     if (np.abs(elem[1] - alfa1) < 0.01):
                    #         d1 = elem[0]
                    #         c += 1
                    #         break
                    #     else:
                    #         d1 = 0
                    if (d1 != 0):
                        deltad = np.abs(np.sqrt(np.power(X1js[0], 2) + np.power(X1js[1], 2)) - d1)
                    else:
                        deltad = 0

                    func += deltad
                func /= c
                res.append(func)
                res.append([x, y, phi])
                disp.append(res)
        print('End epoch{0}'.format(x))
    x = []
    y = []
    for elem in disp:
        x.append(elem[1][axis])
        y.append(elem[0][0])
    if (ax is not None):
        ax.plot(x, y)
        ax.grid()

    return disp






