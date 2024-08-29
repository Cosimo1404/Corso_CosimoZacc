username_corretto = 'Cosimo'
password_corretta = '12345'

#verifica credenziali
username = input('Inserisci username')
password = input('Inserisci password')

if username == username_corretto and password == password_corretta:
    print('Credenziali corrette')

    #scelta domanda segreta
    print('Scegli domanda segrete')
    print('1.Qual è il tuo colore preferito?')
    print('2.Qual è il tuo animale preferito?')

    scelta = input('Inserisci il numero della tua scelta')
    if scelta == '1':
        risposta = input('Qual è il tuo colore preferito?')
        print('Hai scelto il colore', risposta, 'come risposta alla domanda segreta')
    elif scelta == '2':
        risposta = input ('Qual è il tuo animale preferito?')
        print('Hai scelto il colore', risposta , 'come risposta alla domanda segreta')
    else:
        print('Scelta non valida')
else:
    print('Nome utente o password errate')

