# Pruebas Estadísticas y Teorema Central del Límite

## Descripción General

Este repositorio contiene scripts y notebooks para la implementación de pruebas estadísticas y la exploración del Teorema Central del Límite (TCL). A través de estos materiales, se busca proporcionar una comprensión detallada y aplicada de técnicas estadísticas fundamentales para el análisis de datos.

Los códigos implementan de manera práctica diversas pruebas de normalidad, como Shapiro-Wilk, Kolmogorov-Smirnov, y otras, permitiendo evaluar si un conjunto de datos sigue una distribución normal. Además, se explora el TCL mediante simulaciones con distribuciones no normales, mostrando cómo las medias muestrales tienden a distribuirse de forma normal a medida que aumenta el tamaño de la muestra.

---

## Estructura del Proyecto

```
Statistics/
│
├── main.py             # Script principal con las implementaciones de pruebas de normalidad.
├── tcl.py              # Script dedicado a la demostración del Teorema Central del Límite (TCL).
├── testing.py          # Módulo con funciones para realizar pruebas estadísticas personalizadas.
├── /data               # Carpeta para datos generados o utilizados en los ejemplos.
└── README.md           # Documentación del repositorio.
```

---

## Descripción de Funcionalidades

### 1. **Pruebas de Normalidad**

Este conjunto de pruebas estadísticas permite verificar la normalidad de una muestra de datos. Se implementan las siguientes pruebas:

- **Shapiro-Wilk**: Evaluación de si una muestra proviene de una distribución normal.
- **Kolmogorov-Smirnov**: Prueba que compara la distribución empírica de los datos con una distribución de referencia.
- **Anderson-Darling**: Una prueba más robusta para la normalidad que otorga mayor peso a las colas de la distribución.
- **Jarque-Bera**: Prueba que evalúa la asimetría y curtosis de los datos, comparándolos con los valores esperados para una distribución normal.
- **D'Agostino-Pearson**: Prueba que se enfoca en la asimetría y la curtosis de los datos.

Cada prueba proporciona un valor estadístico y un valor p, con lo que el usuario puede tomar decisiones sobre si rechazar o no la hipótesis nula de normalidad.

#### Ejemplo de uso:
```python
from testing import Test

# Crear objeto Test para aplicar las pruebas sobre la columna 'data'
test = Test(data)
test.shapiro_wilk('data', 0.05)
```

### 2. **Exploración del Teorema Central del Límite (TCL)**

El script `tcl.py` demuestra cómo, mediante simulaciones, el TCL se manifiesta incluso en distribuciones no normales. A través de la generación de muestras de diferentes tamaños, se observa que las medias muestrales tienden a seguir una distribución normal, independientemente de la distribución original de los datos.

Las simulaciones incluyen la generación de una serie con distribución Beta y el cálculo de la media de varias muestras de tamaños crecientes, lo que permite observar cómo las distribuciones de las medias se aproximan a la normalidad conforme aumenta el tamaño de las muestras.

#### Ejemplo de visualización:
```python
from tcl import graficar

# Visualizar el comportamiento de las distribuciones muestrales para diferentes tamaños
graficar(serie, filas=2, columnas=4)
```

### 3. **Visualización de Resultados**

Se incluye la visualización de los datos y las simulaciones mediante histogramas y curvas de densidad de Kernel (KDE). Estos gráficos permiten analizar cómo cambian las distribuciones a medida que varían los tamaños de muestra y la cantidad de muestras tomadas.

#### Ejemplo de visualización:
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Visualizar la distribución de una muestra
sns.histplot(data=serie, kde=True, bins=35, color='orange')
plt.show()
```

---

## Requisitos

### Librerías
Este repositorio utiliza las siguientes bibliotecas:

- **NumPy**: Para la generación de números aleatorios y operaciones matemáticas.
- **Pandas**: Para la manipulación y organización de los datos.
- **Matplotlib** y **Seaborn**: Para la creación de gráficos y visualizaciones.

### Instalación
Para instalar las dependencias necesarias, puedes usar el siguiente comando:

```bash
pip install numpy pandas matplotlib seaborn
```
