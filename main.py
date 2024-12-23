# -*- coding: utf-8 -*-
"""main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pz7s3PkkO-ltpRb2VB6CeoYr_2BaANhv
"""

# Liberías
import pandas as pd
import numpy as np
import os

# Montar google
from google.colab import drive
drive.mount('/content/drive')

# Agrega la ruta del notebook al sistema (llega a la carpeta)
import sys
sys.path.append(os.path.abspath('/content/drive/My Drive/Colab Notebooks/Modelos/Statistics/'))

# Actualiza el módulo de clases para capturar cambios
from importlib import reload
import testing
reload(testing)
from testing import Test

# Genera una serie de 100 números con distribución normal
# Media = 2.5 y desviación estándar = 3.2
np.random.seed(0)  # Fijamos la semilla para reproducibilidad
data = np.random.normal(loc=2.5, scale=3.2, size=50)
data = pd.DataFrame(data, columns=['data'], index=range(1,51))
# print(data)

# Shapiro
test = Test(data)
test.shapiro_wilk('data', 0.05)

# Kolmogorov-Smirnov
test = Test(data)
test.kolmogorov_smirnov('data', 0.05)

# Anderson-Darling
test = Test(data)
test.anderson_darling('data')

# Jarque-Vera
test = Test(data)
test.jarque_bera('data', 0.05 )

# D'Agostino_Pearson
test = Test(data)
test.dagostino_pearson('data', 0.05)

# Lilliefors