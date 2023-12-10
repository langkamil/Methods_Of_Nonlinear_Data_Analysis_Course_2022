# -*- coding: utf-8 -*-
"""
transponuje macierze
"""

print("Ładuję moduł o nazwie: " + __name__)


def transpose(A):
    '''
    Funkcja transponująca macierz
    parametry: 
        A: numpy array object 
            macierz, którą transponujemy 
    '''
    import numpy as np 
    B = np.zeros(shape=(np.shape(A)[1], np.shape(A)[0]))
    
    for j in range(np.shape(A)[1]):
        for i in range(np.shape(A)[0]):
            B[j][i] = A[i][j] 
    return B
