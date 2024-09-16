# L'obiettivo di questo esercizio è generare un set di dati di serie temporali utilizzando NumPy, analizzarli con pandas e 
# visualizzare i risultati usando Matplotlib. Gli studenti dovranno eseguire le seguenti operazioni:

#1_ Generazione dei Dati: Utilizzare NumPy per generare una serie temporale di 365 giorni di dati, simulando il numero di visitatori giornalieri in
# un parco. Assumere che il numero medio di visitatori sia 2000 con una deviazione standard di 500. Inoltre, aggiungere un trend crescente nel
# tempo per simulare l'aumento della popolarità del parco.
#2_ Creazione del DataFrame: Creare un DataFrame pandas con le date come indice e il numero di visitatori come colonna.
#3_Analisi dei Dati: Calcolare il numero medio di visitatori per mese e la deviazione standard.
#4_ Visualizzazione dei Dati:
#  Creare un grafico a linee del numero di visitatori giornalieri.
# Aggiungere al grafico la media mobile a 7 giorni per mostrare la
# tendenza settimanale.
# Creare un secondo grafico che mostri la media mensile dei visitatori.


import numpy as np
import pandas as pd

# 1. generazione dei dati
np.random.seed(42)  # fissiamo il seed per la riproducibilità in modo tale che riprodica ogni volta la stessa sequenxa di numeir casuali

date = pd.date_range(start="2023-01-01", periods=365) # creiamo 365 giorni consecutivi a partire dal 1° gennaio 2023

visitatori_base = np.random.normal(loc=2000, scale=500, size=365) #generuamo i dati dei visitatori: media 2000 con una deviazione standard di 500

# aggiungere un trend crescente nel tempo per simulare l'aumento della popolarità del parco.
trend = np.linspace(0, 1000, 365)  # Trend che aumenta fino a 1000 visitatori in più. start/stop/num(la funzione genera 365 num equdistanti da 0 a 1000 )
visitatori_con_trend = visitatori_base + trend

# 2. Creazione del DataFrame
df_visitatori = pd.DataFrame({"Data": date, "Visitatori": visitatori_con_trend})
df_visitatori.set_index("Data", inplace=True) #mettiamo la data come indice

print("Prime 5 righe del DataFrame:\n", df_visitatori.head()) # Visualizzare i primi 5 dati

# 3. Analisi dei dati
media_mensile = df_visitatori.resample('M').mean()  #Calcolare il numero medio di visitatori per mese ### df_visitatori. resample('M).mean() raggruppa i dati giornalieri in intervalli mensili. 'M' sta per mese. .mean()calcola la media dei visitatoi per ogni mese
dev_standard_mensile = df_visitatori.resample('M').std()

print("\nNumero medio di visitatori per mese:")
print(media_mensile)

print("\nDeviazione standard del numero di visitatori per mese:")
print(dev_standard_mensile)

date = pd.date_range(start="2023-01-01", periods=365) #creiamo 365 giorni consecutivi a partire d 1 gennaio 23

visitatori_base = np.random.normal(loc=2000, scale=500, size=365) # generiamo i dati dei visitatori: media di 2000 con deviazione standard di 500

trend = np.linspace(0, 1000, 365)  # Aggiungiamo un trend crescente (es. popolarità del parco in crescita) simulando un incremento graduale
visitatori_con_trend = visitatori_base + trend # Trend che aumenta fino a 1000 visitatori in più

# 2. Creazione del DataFrame
df_visitatori = pd.DataFrame({"Data": date, "Visitatori": visitatori_con_trend})
df_visitatori.set_index("Data", inplace=True)

# Visualizzare i primi 5 dati
print("Prime 5 righe del DataFrame:\n", df_visitatori.head())

# 3. Analisi dati

# Calcolare il numero medio di visitatori per mese
media_mensile = df_visitatori.resample('M').mean()
dev_standard_mensile = df_visitatori.resample('M').std()

print("\nNumero medio di visitatori per mese:")
print(media_mensile)

print("\nDeviazione standard del numero di visitatori per mese:")
print(dev_standard_mensile)
