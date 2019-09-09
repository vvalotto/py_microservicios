import matplotlib.pyplot as plt
import numpy as np


def bernoulli():
    plt.figure()
    dist = np.random.binomial(1, 0.6, 10000)/0.5
    plt.hist(dist, 2, normed=1)
    plt.show()


def binomial():
    plt.figure()
    dist = np.random.binomial(100, 0.6, 10000)/0.01
    plt.hist(dist, 100, normed=1)
    plt.show()


def uniforme():
    plt.figure()
    uniforme_bajo = 0.25
    uniforme_alto = 0.8
    uniform = np.random.uniform(uniforme_bajo, uniforme_alto, 10000)
    plt.hist(uniform, 50, normed=1)
    plt.show()

if __name__ == "__main__":
    bernoulli()
    binomial()
    uniforme()