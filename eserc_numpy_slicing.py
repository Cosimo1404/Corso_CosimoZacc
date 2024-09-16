# Esercizio su NumPy Slicing
# Consegna:
# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
# Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
# Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
# Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
# Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
# Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
# Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

import numpy as np

arr = np.random.randint(10, 51, size=20)

print(arr[1:11])

print(arr[-5:])

print(arr[6:15])

print("Ogni terzo elemento dell'array:", arr[::3])

arr[5:10] = 99

print(arr)





