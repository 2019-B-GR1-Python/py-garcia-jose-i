#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:21:23 2019

@author: tkhacker
"""

import pandas as pd
import os

# 1) JSON CSV HTML XML ...

path = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.csv"

df1 = pd.read_csv(
        path,
        nrows = 10)


columnas = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear',
            'height', 'width', 'units']

df2 = pd.read_csv(
        path,
        nrows = 10,
        usecols = columnas)

df3 = pd.read_csv(
        path,
        usecols = columnas,
        index_col = 'id')

df4 = pd.read_csv(path)

path_guardado = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle"
path_guardado_bin = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle_2"


df3.to_pickle(path_guardado)
df4.to_pickle(path_guardado_bin)

df5 = pd.read_pickle(path_guardado_bin)