# -*- coding: utf-8 -*-
"""
sumuje elementy wektora
"""

print("Ładuję moduł o nazwie: " + __name__)

def summation(A):
    '''
    Funkcja sumująca elementy tablicy pionowej
    parametry: 
        A: numpy array object 
            sumowany wektor
    '''
    summation_value = 0
    
    for i in range(len(A)):
        summation_value += A[i]
        
    return(summation_value)