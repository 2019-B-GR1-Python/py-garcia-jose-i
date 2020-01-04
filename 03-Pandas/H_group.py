#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:20:29 2020

@author: tkhacker
"""

import pandas as pd
import numpy as np
import math

path_guardado_bin = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle"
df = pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')
type(df_agrupado)

for a, b in df_agrupado:
    print(type(a)) #str
    print(type(b)) #Dataframe
    print(b)
    
    
for columna_agrupada, df_completo in df_agrupado:
    print(type(columna_agrupada))
    print(type(df_completo))
    
a = seccion_df['units'].value_counts()
a.empty  

  
def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            contador = 0
            for valor_serie in series:
                valor = int(valor_serie)
                if(math.isnan(valor_serie)):
                    pass
                else:
                    valor = int(valor_serie)
                    contador = contador + 1
                    suma = suma + valor
            promedio = suma / contador
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
            
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        
        lista_df.append(copia)
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

df_valores_llenos = transformar_df(seccion_df)


seccion_df['units'] = seccion_df['units'].fillna(seccion_df['units'].value_counts().reset_index().head(1)['index'][0])


def frecuency(df, column):
    return df[column].fillna(df[column].value_counts().reset_index().head(1)['index'][0])
    
seccion_df['height'] = frecuency(seccion_df, 'height')

        
        