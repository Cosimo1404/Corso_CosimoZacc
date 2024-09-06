# Esercizio 1 (Facile): Scrivi una funzione chiamata area triangolo che prenda in input 
# la base e l'altezza di un triangolo e restituisca la sua area. fare la
# stessa cosa con quadrato e rettagolo e rendere ripetibile salvando in una lista
# tutti i risultati

def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato * lato

def area_rettangolo(base, altezza):
    return base * altezza

aree = [] #per salvare i risultati

while True:
    print("Scegli una forma geometrica:")
    print("1. Triangolo")
    print("2. Quadrato")
    print("3. Rettangolo")
    print("4. Esci")

    scelta = input("Inserisci il numero della tua scelta: ")

    if scelta == "1": #triangolo
        base = int(input("Inserisci la base del triangolo: "))
        altezza = int(input("Inserisci l'altezza del triangolo: "))
        area = area_triangolo(base, altezza)
        aree.append(area)
        print(f"L'area del triangolo è: {area}")

    elif scelta == "2": #quadrato
        lato = int(input("Inserisci il lato del quadrato: "))
        area = area_quadrato(lato)
        aree.append(area)
        print(f"L'area del quadrato è: {area}")

    elif scelta == "3": #rettangolo
        base = int(input("Inserisci la base del rettangolo: "))
        altezza = int(input("Inserisci l'altezza del rettangolo: "))
        area = area_rettangolo(base, altezza)
        aree.append(area)
        print(f"L'area del rettangolo è: {area}")

    elif scelta == "4": #esce dal ciclo
        print("Grazie! Ecco tutte le aree calcolate:", aree)
        break

    else:
        print("Scelta non valida. Riprova.")
 






