#Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
#Esercizio:
# Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# Verifica il tipo di dato dell'array e stampa il risultato.
# Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# Stampa la forma dell'array


import numpy as np

arr = np.arange(10,50)

print("Array iniziale:", arr)

print("Tipo di dato iniziale:", arr.dtype)

array_float = arr.astype(np.float64)

print("Forma dell array:", arr.shape)

