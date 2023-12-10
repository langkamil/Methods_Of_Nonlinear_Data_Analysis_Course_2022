# -*- coding: utf-8 -*-
"""
mnoży macierze
"""

print("Ładuję moduł o nazwie: " + __name__)

def multiplication(A, B):
    '''
    Funkcja mnożąca macierze 
    parametry:
        A: numpy array object 
            pierwsza macierz w mnożeniu 
        B: numpy array object 
            druga macierz w mnożeniu
    '''
    import numpy as np 
    C = np.zeros((np.shape(A)[0], np.shape(B)[1]))

    for i in range(np.shape(A)[0]):
        
         for j in range(np.shape(B)[1]):
                
            for k in range(np.shape(B)[0]):
                
                C[i][j] += A[i][k] * B[k][j]
    return C