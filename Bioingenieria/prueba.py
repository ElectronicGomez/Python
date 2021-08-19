import pandas as pd
import numpy as np
import datetime
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
from sklearn import metrics
from keras import optimizers

np.random.seed(int(datetime.datetime.now().microsecond))

df = pd.read_csv("heartModified(thalDiv).csv")
print(df.info())
print('')

print(df.describe())
print('')

print(df.head(10))
print('')

#Normalizando datos
X = df.loc[:,['age','sex','cp0','cp1','cp2','cp3','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope0','slope1','slope2','ca','thal1','thal2','thal3']]
X['age'] = (X['age'] - 25)/(80-25)
X['trestbps'] = (X['trestbps'] - 90)/(200-90)
X['chol'] = (X['chol'] - 125)/(570-125)
X['thalach'] = (X['thalach'] - 70)/(205-70)
X['oldpeak'] = (X['oldpeak'] - 0)/(6.2-0)
X['ca'] = (X['ca'] - 0)/(4-0)

#Vector de salida deseada
y = df.loc[:,'target']

# Se conforman los patrones de entrenamiento:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Se crea el modelo
model = Sequential()
model.add(Dense(units=11, activation='sigmoid', input_dim=20))
model.add(Dense(units=11, activation='sigmoid'))
model.add(Dense(units=1, activation='sigmoid'))

#Se entrena el modelo
sgd = optimizers.SGD(lr=0.4)
model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(X, y, epochs=3000, verbose=False)

print("")
print("Training Done")
y_pred = model.predict(X_test)

ac = metrics.accuracy_score(y_test, y_pred.round())
print("accuaracy:",ac)