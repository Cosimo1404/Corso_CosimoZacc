# Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.
# Esercizio:
# Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
# Cambia la forma dell'array a una matrice 3x4.
# Genera una matrice 3x4 di numeri casuali tra 0 e 1.
# Calcola e stampa la somma degli elementi di entrambe le matrici.

import numpy as np

arr = np.linspace(0, 1, 12)
print(arr)

matrice_arr = arr.reshape(3, 4)
print(matrice_arr)

random_arr = np.random.rand (3, 4)
print(random_arr)

somma_matrice = np.sum(matrice_arr)
somma_random = np.sum(random_arr)

somma_tot = somma_matrice + somma_random



