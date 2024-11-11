#File: matrices.py
import numpy as np

def n_by_n(matrix, dimension):
    """
    Pick out a square matrix from a 2-dimensional array starting from the top left corner
    """
    new_matrix=[] #A blank array to be filled with picked-out rows
    i=0 #Index to count rows
    for i in range(dimension):
        rows=[] #Blank list for picked-out elements of each row
        for j in range(dimension):
            rows.append(matrix[i][j]) #Add each elements to "rows"
            if len(rows) == dimension:
                i += 1
                new_matrix.append(rows) #Add "rows" to the array which will be our new matrix
    return np.array(new_matrix)

def find_determinant(matrix):
    """
    If it is possible to calculate it (i.e. if it is square), calculate the matrix's determinant
    """
    for row in matrix:
        if len(matrix)!= len(matrix[0]): #Check if the no. of rows equals no. of columns
            print("Not a square matrix.")

        else:
            return np.linalg.det(matrix) #Using a linear algebra numpy function!
    

def find_trace(matrix):
    """
    If it is possible to calculate it (i.e. if it is square), calculate the matrix's trace
    """
    trace=0
    for row in matrix:
        if len(matrix) != len(matrix[0]): #Check if theno. of rows equals no. of columns
            print("Not a square matrix.")
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    if i==j:
                        trace += matrix[i][j] #Add all the diagonal elements of the matrix (row=column)
        return trace




