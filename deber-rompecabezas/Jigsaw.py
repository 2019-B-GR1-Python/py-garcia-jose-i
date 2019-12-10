import math
import random
import numpy as np
import matplotlib.pyplot as plt
##import matplotlib.image as mpimg
class Puzzle:

    def __init__(self):
        self.imagen = plt.imread('/home/tkhacker/git/py-garcia-jose-i/deber-rompecabezas/thanos.jpg')
        self.rows_croped_image_list = None
        self.rows_croped_image_array = None
        self.columns_croped_image_list = []
        ##self.columns_croped_image_array = []
        self.rows = 0
        self.columns = 0
        self.img = None
        
    def createJigsaw(self,dimensions):
        self.img = np.array(self.imagen)
        self.rows_croped_image_list = np.vsplit(self.img,int(dimensions[0]))
        random.shuffle(self.rows_croped_image_list)
        for i in range(0,int(dimensions[0])):
            self.columns_croped_image_list.append(np.hsplit(self.rows_croped_image_list[i],int(dimensions[1])))
            random.shuffle(self.columns_croped_image_list[i])
            self.rows_croped_image_list[i] = np.hstack(self.columns_croped_image_list[i])
        self.rows_croped_image_array = np.vstack(self.rows_croped_image_list)
        plt.imshow(self.rows_croped_image_array)    
        plt.show(block=False)
    
    def changePiece(self,pos_piece_A,pos_piece_B):
        pos_x_piece_A = math.ceil(pos_piece_A/self.columns) - 1
        pos_y_piece_A = pos_piece_A - (pos_x_piece_A*self.columns) -1
        pos_x_piece_B = math.ceil(pos_piece_B/self.columns) - 1
        pos_y_piece_B = pos_piece_B - (pos_x_piece_B*self.columns) -1
        list_aux_1 = self.columns_croped_image_list[pos_x_piece_A]
        piece_1 = list_aux_1[pos_y_piece_A]
        list_aux_2 = self.columns_croped_image_list[pos_x_piece_B]
        piece_2 = list_aux_2[pos_y_piece_B]
        list_aux_1[pos_y_piece_A] = piece_2
        list_aux_2[pos_y_piece_B] = piece_1
        self.rows_croped_image_list[pos_x_piece_A] = np.hstack(list_aux_1)
        self.rows_croped_image_list[pos_x_piece_B] = np.hstack(list_aux_2)
        self.rows_croped_image_array = np.vstack(self.rows_croped_image_list)
        plt.imshow(self.rows_croped_image_array)
        plt.show(block=False)
        
    def main(self):
        keyboard_entry = None
        plt.imshow(self.imagen)    
        plt.show(block=False)
        entry = input("Ingrese en cuantas filas y columnas desea que esté dividido su rompecabezas. Ejemplo: 9,4\n")
        dimensions = entry.split(",")
        self.rows = int(dimensions[0])
        self.columns = int(dimensions[1])
        num_pieces = self.rows*self.columns
        self.createJigsaw(dimensions)
        print(f"Se han generado {num_pieces} piezas númeradas desde la esquina superior derecha")
        while keyboard_entry != 'q':
            if(np.array_equal(self.img,self.rows_croped_image_array)):
                print("Felicidades ganaste")
                break
            else:
                keyboard_entry = input("Ingrese las 2 piezas que quiere cambiar separadas por coma. Ejemplo: 12,1\nPresione q si desea salir\n")
                if(keyboard_entry != 'q'):
                    pieces = keyboard_entry.split(",")
                    piece_A = int(pieces[0])
                    piece_B = int(pieces[1])
                    if(1<=piece_A<=num_pieces and 1<=piece_B<=num_pieces):
                        self.changePiece(piece_A,piece_B)
                    else:
                        print("Escribe bien")

Puzzle().main()


