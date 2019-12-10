#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:24:08 2019

@author: tkhacker
"""

import numpy as np
from scipy import misc
from matplotlib import pyplot as plt
import pandas as pd

#1
vector_ceros = np.zeros(10)

#2
vector_ceros_uno = np.zeros(10)
vector_ceros_uno[4] = 1

#3
vector_50_elementos = np.arange(0, 51, 1)
vector_50_elementos = vector_50_elementos[::-1]

#4
matrix = np.arange(0,9,1).reshape(3,3)

#5
arreglo = [1,2,0,0,4,0]


#6
identity_matrix = np.identity(3)

#7
random_matrix = np.random.random(27).reshape(3,3,3)

#8
matrix_2 = np.random.random(100).reshape(10,10)
numero_mayor = np.max(matrix_2)
numero_menor = np.min(matrix_2)

#9
mapache = misc.face()


#10
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
mylist_series = pd.Series(mylist)
myarr_series = pd.Series(myarr)
mydict_series = pd.Series(mydict)

#11
ser = pd.Series(mydict) 
df = ser.reset_index()
# Transformar la serie en dataframe y hacer una columna indice

#12
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
df2 = pd.DataFrame(ser1)
df2['numbers'] = ser2

#13
res1 = ser1 * ser2
results = ser1.where(ser2)


#14


#15
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser_value_counts = ser.value_counts(sort=True, ascending=False)

#16
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
ser_value_counts_2 = ser.value_counts(sort=True, ascending=False).head(2)
ser_value_counts_2 = ser_value_counts_2.reset_index()

def check(x):
    if x in ser_value_counts_2['index'].array:
        return x
    else:
        return 0
ser = ser.apply(check)


#17
ser = pd.Series(np.random.randint(1, 10, 35))
temp_array = ser.values
df = pd.DataFrame(temp_array.reshape(7,5))

#18
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
vocales = ser[pos]

#19
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
#Vertical
df = pd.DataFrame(np.column_stack((ser1.array, ser2.array)))
#Horizontal
df = pd.DataFrame(np.row_stack((ser1.array, ser2.array)))

#20
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
df = pd.DataFrame(frutas)
df['pesos'] = pesos
df = df.groupby(0).median()

#21
path='/home/tkhacker/git/py-garcia-jose-i/examen/data.csv'
columnas = ['crim', 'zn', 'tax']

archivo_importado = pd.read_csv(
        path,
        usecols = columnas)
