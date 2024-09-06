# Esercizio 3 (Difficile): Sviluppa una funzione chiamata comprimi_stringa che prenda in
# input una stringa e restituisca una versione "compressa" di essa. La compressione dovrebbe
# funzionare in questo modo: per ogni gruppo consecutivo di caratteri identici nella
# stringa, la funzione dovrebbe aggiungere il carattere seguito dal numero di volte che 
# appare consecutivamente.
# Per esempio, la stringa "aaabbc" dovrebbe diventare "a3b2c1". Se la "compressione" non
# riduce la lunghezza della stringa, la funzione dovrebbe semplicemente restituire la
# stringa originale.


def verifica_stringa_vuota(funzione):
    def wrapper(s):
        if not s:  # controlls se la stringa è vuota
            print("Errore: Hai inserito una stringa vuota.")
            return ""
        return funzione(s)  # ritorna alla funzione originale se la stringa non è vuota
    return wrapper


@verifica_stringa_vuota
def comprimi_stringa():
    s = input("Inserisci una stringa da comprimere: ")

    if not s:
        return s
    
    stringa_compressa = []
    conteggio = 1

    for i in range(1, len(s)):       # Scorriamo la stringa a partire dal secondo carattere
        if s[i] == s[i - 1]: # se il carattere corrente è uguale a quelo analizz prima, aumentiamo il conteggio
            conteggio += 1
        else:           # aggiungiamo il carattere e il conteggio alla stringa compressa
            stringa_compressa.append(s[i - 1] + str(conteggio))
            conteggio = 1  # azzeriamo il conteggio per il nuovo carattere

    stringa_compressa.append(s[-1] + str(conteggio)) # aggiungiamo l ultimo carattere al conteggio

    stringa_compressa = ' '.join(stringa_compressa) # trsformiamo la lista in una stringa

    return stringa_compressa    # restituire la stringa compressa

print(comprimi_stringa())