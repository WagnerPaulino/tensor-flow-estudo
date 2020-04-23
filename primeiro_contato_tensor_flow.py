import tensorflow as tf
import numpy as np


myGraph = tf.Graph()
# Constroi um grafo simples e faz a soma de seus valores
x1 = tf.constant(1)
x2 = tf.constant(2)
z = tf.add(x1, x2)
# Controi uma matriz de 3 colunas e 2 linhas com valores 0
a = tf.zeros((2, 3))

print(x1.numpy())
print(x2.numpy())
print(z.numpy())
print(a.numpy())