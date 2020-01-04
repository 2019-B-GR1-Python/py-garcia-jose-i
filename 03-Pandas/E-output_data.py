#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:59:46 2019

@author: tkhacker
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado_bin = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[30000:42000,].copy()

#   Tipos archivos
#   JSON
#   EXCEL
#   SQL

### EXCEL ###

path_guardado = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/mi_df_completo.xlsx"
df.to_excel(path_guardado)
df.to_excel(path_guardado, index = False)

columnas = ['artist', 'title', 'year']
df.to_excel(path_guardado, columns=columnas)

### Múltiples hojas de trabajo ###

path_multiple = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/mi_df_multiple.xlsx"
writer = pd.ExcelWriter(path_multiple,
                        engine = "xlsxwriter")

df.to_excel(writer, sheet_name = 'Primera')

df.to_excel(writer, sheet_name = 'Segunda', 
            index = False)

df.to_excel(writer, 
            sheet_name = 'Tercera', 
            index = False,
            columns=columnas)

writer.save()

num_artistas = df['artist'].value_counts()

path_colores = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/mi_df_colores.xlsx"
writer = pd.ExcelWriter(path_multiple,
                        engine = "xlsxwriter")

num_artistas.to_excel(writer, 
                      sheet_name="Artistas")

hoja_artistas = writer.sheets['Artistas']

rango_celdas = "B2:B{}".format(len(num_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

workbook = writer.book
chart1 = workbook.add_chart({'type': 'column'})
chart1.add_series({
        'name': 'Número de Artistas',
        'categories': '=Artistas!A3:A{}'.format(len(num_artistas.index) + 1),
        'values': '=Artistas!B3:B{}'.format(len(num_artistas.index) + 1),
        })

hoja_artistas.insert_chart('D3', chart1)

workbook.close()
writer.save()

######## SQL ########
with sqlite3.connect("/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/bdd_artist.db") as conexion:
    df5.to_sql('py_artistas', conexion)
    
# with mysql.connect('mysql://user:password@ip:puerto/nombre?base')
#    df5.to_sql('py_artistas', conexion)

df.to_json('/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artistas.json')

