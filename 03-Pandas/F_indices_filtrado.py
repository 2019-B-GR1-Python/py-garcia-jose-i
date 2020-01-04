#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:28 2019

@author: tkhacker
"""
import pandas as pd


path_guardado_bin = "/home/tkhacker/git/py-garcia-jose-i/03-Pandas/data/artwork_data.pickle"
df = pd.read_pickle(path_guardado_bin)


serie_artistas_repetidos = df['artist']

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake = df['artist'] == "Blake, William"
blake.value_counts()
df['artist'].value_counts()

df_blake = df[blake]
