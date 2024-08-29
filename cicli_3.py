#scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di ciascuno delle liste

#inserisci il dei numeri ####aiutato da GPT

numeri = input('Inserisci una lista di numeri')
numeri = list(map(int, numeri.split()))
print('i quadrati dei numeri sono:') #i quadrati dei numeri sono:
for  numero in numeri:
    print(numero**2) #risultato 