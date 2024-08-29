
x = True

while x:
    numero=int(input('inserisci numero'))
    for numeri in range (numero, -1, -1):
        print(numeri)
    y=input('continuare? Si/No')
    if y != 'si':
        x = False
    