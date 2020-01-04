#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:58 2019

@author: tkhacker
"""

import pandas as pd
import numpy as np

path_guardado_bin = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle"
df = pd.read_pickle(path_guardado_bin)
df = df.reset_index()

df2 = df.set_index('id')

primero = df.loc[1035]
segundo = df.iloc[1035]

primero2 = df2.loc[1035]
segundo2 = df2.iloc[1035]

###
df3 = pd.DataFrame(np.array([[7, 5], 
                             [8, 9], 
                             [9, 2]]), 
columns=['nota1', 'disciplina'],
index=['Pepito', 'Juanita', 'Maria'])

primero3 = df3.loc['Pepito']
pepito_disciplina_nota1 = df3.loc['Pepito', ['disciplina', 'nota1']]
las2 = df3.loc[['Pepito', 'Maria'], ['disciplina']]
filtrado_bol = df3.loc[[True, False, True]]
segundo3 = df3.iloc['Pepito']

notas_mayores_7 = df3['nota1'] > 7
notas_mayores_7 = df3.loc[df3['nota1'] > 7] [df3['disciplina'] > 7]

df3.loc[df3['disciplina'] < 7, 'disciplina'] = 7


df3.loc['Pepito'] = 10

#Establecer valores a una columna
df3.loc[:, 'disciplina'] = 7

#Añadir columna promedio nota1 y disciplina (MAL HECHO)
df3['promedio'] = np.average(df3.loc[:])

df3['promedio'] = (df3['nota1'] + df3['disciplina']) / (df3.columns.size - 1)