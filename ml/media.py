import matplotlib.pyplot as plt


def media(muestra):
    total = 0
    for elemento in muestra:
        total = total + elemento
    return total/len(muestra)


mi_conjunto = [2.,10.,3.,6.,4.,6.,10.]
mi_media = media(mi_conjunto)
plt.plot(mi_conjunto)
plt.plot([mi_media] * 4)
plt.show()