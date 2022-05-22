import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Leemos fichero
df = pd.read_csv('USA_Housing.csv')

# Lista con el nombre de las columnas
columnas = df.columns

# Cantidad de filas
n = df.shape[0]

# Observamos que no hay datos vacíos, en el caso de que los hubiera tenemos que ajustar nuestro dataframe
print(df.isnull().sum())

x = sns.pairplot(df)

