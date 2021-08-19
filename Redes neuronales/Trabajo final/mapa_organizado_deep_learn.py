# Mapa Auto Organizado

#%%
# Importando Librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
# Importando Sets de Datos
dataset = pd.read_csv('BASE_DATOS.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#%%
# Escalado de Categorias
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

#%%
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
frauds = np.concatenate((mappings[(5,7)], mappings[(4,8)]), axis = 0)
frauds = sc.inverse_transform(frauds)






