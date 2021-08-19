import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from keras import optimizers
import time

np.random.seed(16)

df = pd.read_csv("ejempProfe/NotasBio.csv",names = ['cl', 'ea','pc','EL','SO','SI','sexoM','sexoF',
                                         'jalado','aprobado','sobresaliente','resultado'])

# Obtener información de los datos
print(df.info())
print('')

# Resumen estadístico de los datos
print(df.describe())
print('')


# Mirar las primeras 10 filas de datos
print(df.head(10))
print('')

marker_shapes = ['.', '^', '*']

# Graficar la relación entre la PC y el EA
for i, resultados in enumerate(df['resultado'].unique()):
    if i == 0:
        ax = df[df['resultado'] == resultados].plot.scatter(x='pc', y='ea', marker=marker_shapes[i], s=100,title="Aprobados vs jalados por carreras", label=resultados, figsize=(10,7))
    else:
        df[df['resultado'] == resultados].plot.scatter(x='pc', y='ea', marker=marker_shapes[i], s=100, title="Aprobados vs jalados por carreras", label=resultados, ax=ax)

plt.show()
plt.clf()
##Reemplazando el campo resultado por un valor numérico
#df['resultado'] = df['resultado'].replace('APROBADO', 0)
#df['resultado'] = df['resultado'].replace('JALADO', 0)
#df['resultado'] = df['resultado'].replace('SOBRESALIENTE', 0)
#
#       
## Gráfica del histograma de la práctica calificada 1
##df['pc'].plot.hist(title='Histograma de las notas de la PC1')
##plt.show()
#
## Vamos a generar el vector X de entrada y normalizar sus datos
#
#X = df.loc[:, ['cl','pc','ea','EL','SO','SI','sexoM','sexoF']]
#X['cl']=X['cl']/20
#X['pc']=X['pc']/20
#X['ea']=X['ea']/20
## Vector y con la salida deseada
#y = df.loc[:,['jalado','aprobado','sobresaliente']]
#
## Se conforman los patrones de entrenamiento:
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#print(X)
#
#model = Sequential()
## Layer 1
#model.add(Dense(units=7, activation='sigmoid', input_dim=8))
## Output Layer
#model.add(Dense(units=3, activation='sigmoid'))
#
#print(model.summary())
#print('')
#
#sgd = optimizers.SGD(lr=0.4)
#model.compile(loss='mean_squared_error', optimizer=sgd)
#model.fit(X, y, epochs=3000, verbose=False)
##Se imprime la salida para el enetrenamiento realizado
#print(model.predict(X))
#
##Se genera un patrón nuevo para ver la validación de nuestra red neuronal
#dft = pd.DataFrame({"cl":[0.5, 0.7, 1, 1],  
#                   "pc":[0.3, 0.8, 0.7, 1],  
#                   "ea":[0.2,0.4,0.8, 0.9],
#                   "EL":[0,1,1,1],
#                   "SO":[1,0,0,0],
#                   "SI":[0,0,0,0],
#                   "sexoM":[0,1,1,1],
#                   "sexoF":[1,0,0,0]})
#
#
## Print the DataFrame 
#print(dft)   
#y_test_pred = model.predict(dft)
##Se imprime los resultados de la predicción
#print("Prediccion")
#print(y_test_pred)
