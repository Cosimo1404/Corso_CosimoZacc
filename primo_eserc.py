# Pandas
# Esercizio 1: Analisi Esplorativa dei Dati

# Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
# usando pandas.

# Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
# un gruppo di persone: Nome, Età, Città e Salario. 

# Caricare i dati in un DataFrame autogenerandoli casualmente .
# Visualizzare le prime e le ultime cinque righe del DataFrame.
# Visualizzare il tipo di dati di ciascuna colonna.
# Calcolare statistiche descrittive di base per le colonne numeriche (media,
# mediana, deviazione standard).
# Identificare e rimuovere eventuali duplicati.

import pandas as pd
import numpy as np

nomi = ['Cosimo', 'Paolo', 'Giorgio', 'Chiara', 'Davide', 'Federica']
città = ['Roma', 'Milano', 'Napoli', 'Torino', 'Bologna', 'Firenze']

num_persone = 3

df = pd.DataFrame({
    'nome': np.random.choice(nomi, num_persone),
    'eta': np.random.randint(20, 60, num_persone),  # eta tra 20 e 60 anni
    'citta': np.random.choice(città, num_persone),
    'salario': np.random.randint(2000, 5000, num_persone)  # salario tra 2000 e 5000 
})

media = df[['eta', 'salario']].mean()
mediana = df[['eta', 'salario']].median()
dev_std = df[['eta', 'salario']].std()

duplicati = df.drop_duplicates

print("Prime cinque righe del DataFrame:\n", df.head())
print("\nUltime cinque righe del DataFrame:\n", df.tail())
print("\nTipi di dati di ciascuna colonna:\n", df.dtypes)
print('\nMedia:',media)
print('\nMediana:', mediana)
print('\nDeviazione standard;', dev_std)
