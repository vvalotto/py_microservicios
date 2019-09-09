import math  # This library is needed for the power operation


def media(muestra):  # Definition header for the mean function
    total = 0
    for elemento in muestra:
        total = total + elemento
    return total / len(muestra)


def varianza(muestra):  # Definition header for the mean function
    total = 0
    la_media = media(muestra)
    for elemento in muestra:
        total = total + (math.pow(elemento - la_media, 2))
    return total / len(muestra)


mi_muestra1 = [2., 10., 3., 6., 4., 6., 10.]  # We create the data set
mi_muestra2 = [1., -100., 15., -100., 21.]
print("Variance of first set:" + str(varianza(mi_muestra1)))
print("Variance of second set:" + str(varianza(mi_muestra2)))
