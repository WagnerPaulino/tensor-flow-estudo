import numpy as np
# %tensorflow_version 2.x
import tensorflow as tf

import tensorflow_hub as hub
import tensorflow_datasets as tfds

# Carrega e separa os dados
train_data, validation_data, test_data = tfds.load(
    name="imdb_reviews", 
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)

# train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
# train_examples_batch
# train_labels_batch

#Baixa um modelo de incorporação de texto pré-treinado
embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding, input_shape=[], 
                           dtype=tf.string, trainable=True)
"""
Primeira camada: Mapeada a frase dentro de um vetor de incorporação, Dividindo-a em tokens
Segunda camada: Esse vetor de saída de comprimento fixo é canalizado através de uma camada totalmente conectada com 16 unidades ocultas.
Terceira camada: Camada com um simples nó de saida que usa a função de ativação sigmoid
"""
model = tf.keras.Sequential([
  hub_layer,
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dense(1),
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Treina o modelo pegando por vez 512 amostra
# Monitora a perda e a precisão nas 10000 amostras do conjunto de validação
history = model.fit(train_data.shuffle(10000).batch(512),
                    epochs=20,
                    validation_data=validation_data.batch(512),
                    verbose=1)

results = model.evaluate(test_data.batch(512), verbose=2)

for name, value in zip(model.metrics_names, results):
  print("%s: %.3f" % (name, value))
