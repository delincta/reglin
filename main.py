# Copyright (c) 2020 Copyright Mathis POTEAU (delincta) All Rights Reserved.
# coding: utf-8

""" On va calucluer une régression linéaire, on va se baser sur la formule:
b = [n(∑xiyi) − (∑xi)(∑yi) ] / [ n(∑xi^2) − (∑xi)^2 ] et a = np.mean(y) − b.mean(x) """



import numpy as np # On importe numpy
import matplotlib.pyplot as plt # On importe pyplot


def coeff(x , y):
    if np.size(x) == np.size(y) :
        n = np.size(x)
    else:
        return 1


    # Moyenne de x et y
    x_moyenne, y_moyenne = np.mean(x), np.mean(y)

    # calculs préléminaires (oui on découpe le calcul pour que ce soit pas dégueu)
    SS_xy = np.sum(y * x) - n * y_moyenne * x_moyenne #[n(∑xiyi) − (∑xi)(∑yi) ]
    SS_xx = np.sum(x*x) - n * x_moyenne * x_moyenne #[ n(∑xi^2) − (∑xi)^2 ]


    # calcul des coeff de régression

    b = SS_xy / SS_xx # calcul de b
    a = y_moyenne - b * x_moyenne # a = np.mean(y) − b.mean(x) """

    return(a, b)




def plot_reg_lin(x, y, b):

    # nuage de points
    plt.scatter(x, y, color = "couleur", marker = "marker", s = 30) # s = size


    y_pred = b[0] + b[1] * x

    # plot
    plt.plot(x, y_pred, color = "g")

    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()


def main():
    # x = np.array([])  val de x
    # y = np.array([]) val de y

    b = coeff(x, y)

    plot_reg_lin(x, y, b)


    print("Estimated coefficients:\na = {}  \nb = {}".format(b[0], b[1]))

if __name__ == "__main__" :
    main()


# FIN !
