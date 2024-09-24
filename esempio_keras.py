# Esercizio: Classificazione di Cifre Scritte a Mano con Keras

# In questo esercizio, costruiremo e addestreremo un semplice modello di rete neurale utilizzando Keras per classificare le
# cifre scritte a mano del dataset MNIST. 

# Questo dataset contiene immagini in scala di grigi di cifre da 0 a 9, dimensionate a 28x28 pixel.

# Obiettivi:
# Caricare e preprocessare il dataset MNIST.
# Costruire un modello sequenziale con strati densi.
# Compilare il modello specificando ottimizzatore, funzione di
# perdita e metriche.
# Addestrare il modello sui dati di addestramento.
# Valutare le prestazioni del modello sui dati di test.
# Utilizzare il modello per fare predizioni su nuove immagini.

'''# Importare le librerie necessarie
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Caricare il dataset MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Visualizzare alcune immagini di esempio dal set di addestramento
plt.figure(figsize=(7,7))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Etichetta: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()

# Preprocessare i dati
# Normalizzare i valori dei pixel a un intervallo [0, 1]
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Ridimensionare i dati per adattarli al modello (se necessario)
# Nel caso del modello sequenziale con Flatten, non è necessario reshape

# Convertire le etichette in vettori one-hot
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Costruire il modello sequenziale
model = Sequential()
# Appiattire le immagini 28x28 in vettori di 784 elementi
model.add(Flatten(input_shape=(28, 28)))
# Aggiungere uno strato denso con 128 neuroni e attivazione ReLU
model.add(Dense(128, activation='relu'))
# Strato di output con 10 neuroni (uno per classe) e attivazione softmax
model.add(Dense(10, activation='softmax'))

# Compilare il modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Stampare un riepilogo del modello
model.summary()

# Addestrare il modello
history = model.fit(x_train, y_train,
                    epochs=5,
                    batch_size=32,
                    validation_split=0.1)

# Valutare il modello sui dati di test
test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nAccuratezza sul set di test:', test_acc)

# Fare predizioni sul set di test
predictions = model.predict(x_test)

# Funzione per visualizzare l'immagine e la predizione
def plot_image_prediction(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], np.argmax(true_label[i]), img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    
    plt.imshow(img, cmap='gray')

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    
    plt.xlabel(f"Pred: {predicted_label} ({100*np.max(predictions_array):.2f}%)\nTrue: {true_label}", color=color)

# Visualizzare alcune immagini con le loro predizioni
num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
plt.figure(figsize=(10, 10))
for i in range(num_images):
    plt.subplot(num_rows, num_cols, i+1)
    plot_image_prediction(i, predictions, y_test, x_test)
plt.tight_layout()
plt.show()

# Grafico della perdita
plt.plot(history.history['loss'],
label='Perdita Training')
plt.plot(history.history['val_loss']
, label='Perdita Validazione')
plt.xlabel('Epoca')
plt.ylabel('Perdita')
plt.legend()
plt.title('Andamento della Perdita')
plt.show()'''

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Visualizzazione di un esempio
plt.imshow(X_train[0], cmap='gray')
plt.title(f'Etichetta: {y_train[0]}')
plt.show()

# Normalizzazione dei dati (valori da 0-255 a 0-1)
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
#astype('float32') converte i valori dei pixel in numeri in virgola mobile.
# / 255 normalizza i valori dei pixel da 0-255 (intero) a 0-1 (float).

# Reshape dei dati (da 28x28 a vettore di 784 elementi)
X_train = X_train.reshape(-1, 28*28) 
X_test = X_test.reshape(-1, 28*28)
#reshape(-1, 28*28) trasforma ciascuna immagine da 28x28 pixel in un array di 784 elementi. 
#Il parametro -1 dice a Python di calcolare automaticamente il numero di immagini


# Conversione delle etichette in formato one-hot encoding
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
#Le etichette delle cifre (0-9) vengono convertite in vettori one-hot. 
# Un vettore one-hot ha tutti gli elementi a zero tranne uno, che corrisponde alla classe della cifra.
#to_categorical converte ogni etichetta (ad esempio, 5) in un vettore come [0, 0, 0, 0, 0, 1, 0, 0, 0, 0].



# Creazione del modello sequenziale
model = Sequential()

# Aggiunta dello strato Flatten per appiattire le immagini 28x28 in vettori di 784 elementi
model.add(Flatten(input_shape=(28*28,)))

# Aggiunta di uno strato denso con 128 neuroni e funzione di attivazione ReLU
model.add(Dense(128, activation='relu'))

# Aggiunta di uno strato di output con 10 neuroni (uno per ogni cifra) e attivazione softmax
model.add(Dense(10, activation='softmax'))
#Flatten: Appiattisce le immagini 28x28 in vettori di 784 elementi.
# Dense(128, activation='relu'): Strato completamente connesso con 128 neuroni e funzione di attivazione ReLU.
# Dense(10, activation='softmax'): Strato di output con 10 neuroni per le 10 cifre (0-9), attivazione softmax per la classificazione.



# Compilazione del modello
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
#optimizer='adam': Adam è un ottimizzatore efficiente per addestrare reti neurali.
# loss='categorical_crossentropy': Funzione di perdita usata per problemi di classificazione multi-classe.
# metrics=['accuracy']: L'accuratezza sarà monitorata durante l'addestramento.


# Addestramento del modello
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
#epochs=5: L'addestramento durerà per 5 epoche (passaggi attraverso i dati).
# batch_size=32: Ogni aggiornamento dei pesi avviene dopo aver processato 32 esempi.


# Valutazione del modello sui dati di test
test_loss, test_acc = model.evaluate(X_test, y_test)
#model.evaluate() restituisce la perdita e l'accuratezza sui dati di test.

print(f'Accuratezza sul set di test: {test_acc}')




# Fare predizioni sul set di test
predizioni = model.predict(X_test)

# Predire la classe della prima immagine
classe_predetta = np.argmax(predizioni[0])
print(f'La classe predetta per la prima immagine è: {classe_predetta}')
#model.predict() genera le predizioni.
# np.argmax() restituisce l'indice della classe con la probabilità più alta.

# Visualizzazione della prima immagine
plt.imshow(X_test[0].reshape(28, 28), cmap='gray')
plt.title(f'Classe reale: {np.argmax(y_test[0])}, Classe predetta: {classe_predetta}')
plt.show()

