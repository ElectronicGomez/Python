# Modelo Hibrido

#%%
# Part 1 - (Identificando Fraude con MAO)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importando Sets de Datos
dataset = pd.read_csv('BASE_DATOS.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
#%%
# Escalado de Categorias
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Entrenando MAO
from minisom import MiniSom
som = MiniSom(x = 10, y = 10, input_len = 15, sigma = 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)
#%%
# Visualizando Resultados
from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()
#%%
# Encontrando Fraude
mappings = som.win_map(X)
frauds = np.concatenate((mappings[(4,7)], mappings[(6,4)]), axis = 0)
frauds = sc.inverse_transform(frauds)


#%%
# Part 2 - Pasando de Aprendizaje No Supervisado - a Supervisado

# Creando Matriz de Categorias
customers = dataset.iloc[:, 1:].values

# Creando Variable Dependiente
is_fraud = np.zeros(len(dataset))

for i in range(len(dataset)):
    if dataset.iloc[i,0] in frauds:
        is_fraud[i] = 1
#%%
# Escalado de Categorias
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
customers = sc.fit_transform(customers)
#%%
# Part 2 - Creando Red Neuronal

# Importando paquetes
from keras.models import Sequential
from keras.layers import Dense

# Iniciando RNA
classifier = Sequential()

# Capa Input y Primera Capa Oculta
classifier.add(Dense(units = 2, kernel_initializer = 'uniform', activation = 'relu', input_dim = 15))

# Capa Output
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compilando Red
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Encajando Red Neuronal en Set de Entrenamiento
classifier.fit(customers, is_fraud, batch_size = 1, epochs = 2)
#%%
# Prediccion de Fraude Basado en Probabilidad
y_pred = classifier.predict(customers)
y_pred = np.concatenate((dataset.iloc[:, 0:1].values, y_pred), axis = 1)
y_pred = y_pred[y_pred[:, 1].argsort()]





