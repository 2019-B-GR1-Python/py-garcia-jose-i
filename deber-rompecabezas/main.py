# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

rows = 2
columns = 2
height = 800
width = 800

def division(image):
    # División por columnas
    puzzle_columns = np.hsplit(image, columns)
    # División por filas a las columnas
    puzzle_divided = list(map(lambda column: np.vsplit(column, columns), puzzle_columns))
    return puzzle_divided


def shuffle(puzzle_divided):
    # Shuffle Columnas
    random.shuffle(puzzle_divided)
    # Shuffle Filas
    list(map(lambda column: random.shuffle(column), puzzle_divided))
    return puzzle_divided

    
def reassemble(puzzle_divided):
    # Reassemble
    puzzle_columns = list(map(lambda column: np.vstack(column), puzzle_divided))
    puzzle = np.hstack(puzzle_columns)
    return puzzle


def change_position(puzzle_divided, positions): 
    positions = list(map(lambda x: int(x), positions))
    puzzle_divided[positions[0]][positions[1]], puzzle_divided[positions[2]][positions[3]] = puzzle_divided[positions[2]][positions[3]], puzzle_divided[positions[0]][positions[1]]
    return reassemble(puzzle_divided)


def main():
    image = plt.imread("/home/tkhacker/git/py-garcia-jose-i/Tarea2/image.png")
    puzzle = reassemble(shuffle(division(image)))
    plt.imshow(puzzle)
    plt.show(block = False)
    while(True):
        positions_input = input("Ingrese posiciones (#,#,#,#): ")
        puzzle = change_position(division(puzzle), positions_input.split(","))
        plt.imshow(puzzle)
        plt.show(block = False)
        
        
if __name__ == "__main__":
    main()