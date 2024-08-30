#esercizio 4

#inserisci numeri
input_numeri =input('inserisci dei numeri separati da spazi')
numeri = list(map(int, input_numeri.split()))

#numero massimo
if len(numeri) == 0:
    for numero in numeri:
           print('vuoto')
else:
        numero_massimo = numeri[0]
        for numero in numeri:
                if numero > numero_massimo:
                        numero_massimo = numero

#quanti numeri nella lista?
conteggio = 0
while  conteggio < (numeri):
            conteggio += 1

#manca l'ultimo punto 