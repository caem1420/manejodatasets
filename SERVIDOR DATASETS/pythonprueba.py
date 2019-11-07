# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:13:57 2019

@author: Carlos Escobar
"""

import pandas as pd
import statistics
import sys 

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import numpy as np


import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=Warning)
    import imp
    
    
    
data = pd.read_csv("./uploads/"+sys.argv[1]);


                           
#separar el dataset en dos partes por target
datosenfermedad = data[data.target == 1]; #personas con enfermedad cardiaca
datosnoenfermedad =data[data.target == 0];#personas sin enfermedad cardiaca
data.columns = ['edad', 'sexo', 'tipo_dolor_pecho', 'presion_sanguinia_descanso', 'colesterol', 'azucar_ayunas', 'ecg_descanso', 'frecuencia_cardiaca_max',
       'angina_inducida_por_ejercicio', 'st_depresion', 'st_subida', 'num_major_vessels', 'thalassemia', 'objetivo'];


datosenfermedad.columns = ['edad', 'sexo', 'tipo_dolor_pecho', 'presion_sanguinia_descanso', 'colesterol', 'azucar_ayunas', 'ecg_descanso', 'frecuencia_cardiaca_max',
       'angina_inducida_por_ejercicio', 'st_depresion', 'st_subida', 'num_major_vessels', 'thalassemia', 'objetivo'];
                           
datosenfermedad['sexo'][datosenfermedad['sexo'] == 0] = 'mujer'
datosenfermedad['sexo'][datosenfermedad['sexo'] == 1] = 'hombre'

datosenfermedad['tipo_dolor_pecho'][datosenfermedad['tipo_dolor_pecho'] == 0] = 'angina tipica'
datosenfermedad['tipo_dolor_pecho'][datosenfermedad['tipo_dolor_pecho'] == 1] = 'angina atipica'
datosenfermedad['tipo_dolor_pecho'][datosenfermedad['tipo_dolor_pecho'] == 2] = 'dolor sin angina'
datosenfermedad['tipo_dolor_pecho'][datosenfermedad['tipo_dolor_pecho'] == 3] = 'sin sintoma'


datosenfermedad['azucar_ayunas'][datosenfermedad['azucar_ayunas'] == 0] = 'menor de 120mg/ml'
datosenfermedad['azucar_ayunas'][datosenfermedad['azucar_ayunas'] == 1] = 'mayor a 120mg/ml'


datosenfermedad['ecg_descanso'][datosenfermedad['ecg_descanso'] == 0] = 'normal'
datosenfermedad['ecg_descanso'][datosenfermedad['ecg_descanso'] == 1] = 'anomalia onda ST-T'
datosenfermedad['ecg_descanso'][datosenfermedad['ecg_descanso'] == 2] = 'Hipertrofia izquierda'


datosenfermedad['angina_inducida_por_ejercicio'][datosenfermedad['angina_inducida_por_ejercicio'] == 0] = 'no'
datosenfermedad['angina_inducida_por_ejercicio'][datosenfermedad['angina_inducida_por_ejercicio'] == 1] = 'si'


datosenfermedad['st_subida'][datosenfermedad['st_subida'] == 0] = 'ascenso'
datosenfermedad['st_subida'][datosenfermedad['st_subida'] == 1] = 'plano'
datosenfermedad['st_subida'][datosenfermedad['st_subida'] == 2] = 'bajando'


datosnoenfermedad.columns = ['edad', 'sexo', 'tipo_dolor_pecho', 'presion_sanguinia_descanso', 'colesterol', 'azucar_ayunas', 'ecg_descanso', 'frecuencia_cardiaca_max',
       'angina_inducida_por_ejercicio', 'st_depresion', 'st_subida', 'num_major_vessels', 'thalassemia', 'objetivo'];
                           
datosnoenfermedad['sexo'][datosnoenfermedad['sexo'] == 0] = 'mujer'
datosnoenfermedad['sexo'][datosnoenfermedad['sexo'] == 1] = 'hombre'

datosnoenfermedad['tipo_dolor_pecho'][datosnoenfermedad['tipo_dolor_pecho'] == 0] = 'angina tipica'
datosnoenfermedad['tipo_dolor_pecho'][datosnoenfermedad['tipo_dolor_pecho'] == 1] = 'angina atipica'
datosnoenfermedad['tipo_dolor_pecho'][datosnoenfermedad['tipo_dolor_pecho'] == 2] = 'dolor sin angina'
datosnoenfermedad['tipo_dolor_pecho'][datosnoenfermedad['tipo_dolor_pecho'] == 3] = 'sin sintoma'


datosnoenfermedad['azucar_ayunas'][datosnoenfermedad['azucar_ayunas'] == 0] = 'menor de 120mg/ml'
datosnoenfermedad['azucar_ayunas'][datosnoenfermedad['azucar_ayunas'] == 1] = 'mayor a 120mg/ml'


datosnoenfermedad['ecg_descanso'][datosnoenfermedad['ecg_descanso'] == 0] = 'normal'
datosnoenfermedad['ecg_descanso'][datosnoenfermedad['ecg_descanso'] == 1] = 'anomalia onda ST-T'
datosnoenfermedad['ecg_descanso'][datosnoenfermedad['ecg_descanso'] == 2] = 'Hipertrofia izquierda'


datosnoenfermedad['angina_inducida_por_ejercicio'][datosnoenfermedad['angina_inducida_por_ejercicio'] == 0] = 'no'
datosnoenfermedad['angina_inducida_por_ejercicio'][datosnoenfermedad['angina_inducida_por_ejercicio'] == 1] = 'si'


datosnoenfermedad['st_subida'][datosnoenfermedad['st_subida'] == 0] = 'ascenso'
datosnoenfermedad['st_subida'][datosnoenfermedad['st_subida'] == 1] = 'plano'
datosnoenfermedad['st_subida'][datosnoenfermedad['st_subida'] == 2] = 'bajando'

                             
print("Conteo de genero")


ax = sns.countplot(x='sexo', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Genero', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo de genero', fontsize=18)
plt.show()

print("El numero de hombres es")
print(len(datosenfermedad[datosenfermedad.sexo == "hombre"]))

print("El numero de mujeres es")
print(len(datosenfermedad[datosenfermedad.sexo == "mujer"]))


ax = sns.countplot(x='tipo_dolor_pecho', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Tipo dolor pecho', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo de Tipo dolor pecho', fontsize=18)
plt.show()


print("el conteo de angina tipica es:")
print(len(datosenfermedad[datosenfermedad.tipo_dolor_pecho == "angina tipica"]))

print("el contedo de angina atipica es:")
print(len(datosenfermedad[datosenfermedad.tipo_dolor_pecho == "angina atipica"]))

print("el conteo de dolor sin angina es:")
print(len(datosenfermedad[datosenfermedad.tipo_dolor_pecho == "dolor sin angina"]))

print("el contedo de sin sintoma es:")
print(len(datosenfermedad[datosenfermedad.tipo_dolor_pecho == "sin sintoma"]))


ax = sns.lineplot(data=datosenfermedad.presion_sanguinia_descanso)
ax.set_ylabel('Presion sanguinia en descanso', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Presion Sanguinia en descanso', fontsize=18)
plt.show()

temporalpresion_sanguinia_descanso = [];
temporalcolesterol = [];
for i, row in datosenfermedad.iterrows():
    temporalpresion_sanguinia_descanso.append(row["presion_sanguinia_descanso"]);
    temporalcolesterol.append(row["colesterol"])
temporalpresion_sanguinia_descanso.sort();
temporalcolesterol.sort();

print("la presion mas baja fue de", temporalpresion_sanguinia_descanso[0])

print("la presion mas alta fue de", temporalpresion_sanguinia_descanso[len(temporalpresion_sanguinia_descanso)-1])



ax = sns.lineplot(data=datosenfermedad.colesterol,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Personas con colesterol', fontsize=18)
plt.show()

print("El colesterol mas alto es: ", temporalcolesterol[len(temporalcolesterol)-1])
print ("el colesterol mas bajo fue de:", temporalcolesterol[0]);



ax = sns.countplot(x='azucar_ayunas', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Azucar en la sangre en ayunas', fontsize=18)
plt.show()


ax = sns.countplot(x='ecg_descanso', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo ECG en descanso', fontsize=18)
plt.show()


ax = sns.lineplot(data=datosenfermedad.frecuencia_cardiaca_max,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Frecuencia cardiaca maxima', fontsize=18)
plt.show()


ax = sns.countplot(x='angina_inducida_por_ejercicio', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Angina inducida por ejercicio', fontsize=18)
plt.show()

ax = sns.lineplot(data=datosenfermedad.st_depresion,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Depresion ST', fontsize=18)
plt.show()

ax = sns.countplot(x='st_subida', data=datosenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo ST ', fontsize=18)
plt.show()



print("DAtos personas sin enfermdad ")




                             
print("Conteo de genero")


ax = sns.countplot(x='sexo', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Genero', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo de genero', fontsize=18)
plt.show()

print("El numero de hombres es")
print(len(datosnoenfermedad[datosnoenfermedad.sexo == "hombre"]))

print("El numero de mujeres es")
print(len(datosnoenfermedad[datosnoenfermedad.sexo == "mujer"]))


ax = sns.countplot(x='tipo_dolor_pecho', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Tipo dolor pecho', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo de Tipo dolor pecho', fontsize=18)
plt.show()


print("el conteo de angina tipica es:")
print(len(datosnoenfermedad[datosnoenfermedad.tipo_dolor_pecho == "angina tipica"]))

print("el contedo de angina atipica es:")
print(len(datosnoenfermedad[datosnoenfermedad.tipo_dolor_pecho == "angina atipica"]))

print("el conteo de dolor sin angina es:")
print(len(datosnoenfermedad[datosnoenfermedad.tipo_dolor_pecho == "dolor sin angina"]))

print("el contedo de sin sintoma es:")
print(len(datosnoenfermedad[datosnoenfermedad.tipo_dolor_pecho == "sin sintoma"]))


ax = sns.lineplot(data=datosnoenfermedad.presion_sanguinia_descanso)
ax.set_ylabel('Presion sanguinia en descanso', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Presion Sanguinia en descanso', fontsize=18)
plt.show()

temporalpresion_sanguinia_descanso = [];
temporalcolesterol = [];
for i, row in datosnoenfermedad.iterrows():
    temporalpresion_sanguinia_descanso.append(row["presion_sanguinia_descanso"]);
    temporalcolesterol.append(row["colesterol"])
temporalpresion_sanguinia_descanso.sort();
temporalcolesterol.sort();

print("la presion mas baja fue de", temporalpresion_sanguinia_descanso[0])

print("la presion mas alta fue de", temporalpresion_sanguinia_descanso[len(temporalpresion_sanguinia_descanso)-1])



ax = sns.lineplot(data=datosnoenfermedad.colesterol,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Personas con colesterol', fontsize=18)
plt.show()

print("El colesterol mas alto es: ", temporalcolesterol[len(temporalcolesterol)-1])
print ("el colesterol mas bajo fue de:", temporalcolesterol[0]);



ax = sns.countplot(x='azucar_ayunas', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Azucar en la sangre en ayunas', fontsize=18)
plt.show()


ax = sns.countplot(x='ecg_descanso', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo ECG en descanso', fontsize=18)
plt.show()


ax = sns.lineplot(data=datosnoenfermedad.frecuencia_cardiaca_max,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Frecuencia cardiaca maxima', fontsize=18)
plt.show()


ax = sns.countplot(x='angina_inducida_por_ejercicio', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Angina inducida por ejercicio', fontsize=18)
plt.show()

ax = sns.lineplot(data=datosnoenfermedad.st_depresion,linewidth=2)
ax.set_ylabel('Valores', fontsize=12)
ax.set_xlabel('Conteo', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo Depresion ST', fontsize=18)
plt.show()

ax = sns.countplot(x='st_subida', data=datosnoenfermedad, alpha=0.9, edgecolor=('white'), linewidth=2)
ax.set_ylabel('Conteo', fontsize=12)
ax.set_xlabel('Valores', fontsize=12)
ax.grid(b=True, which='major', color='grey', linewidth=0.2)
plt.title('Conteo ST ', fontsize=18)
plt.show()







# Compute the correlation matrix
corr = data.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure


# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})