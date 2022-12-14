'''
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right.
The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge,
if the integer is negative, return the mirror image of the identity matrix of n x n dimensions. It does not matter
if the mirror image is left-right or top-bottom.

Examples

    id_mtrx(2) ➞ [
    [1, 0],
    [0, 1]
    ]
    id_mtrx(-2) ➞ [
    [0, 1],
    [1, 0]
    ]
    id_mtrx(0) ➞ []

Notes

Incompatible types passed as n should return the string "Error".

'''

def id_mtrx(n):
    if type(n) is not int:
        return "Error"
    matrix = []
    if n == 0:
        return matrix
    negative = False
    if n < 0:
        negative = True
        n = -n
    for i in range(n):
        line = []
        for j in range(n):
            if not negative and j == i:
                line.append(1)
            elif negative and (n - j - 1) == i:
                line.append(1)
            else:
                line.append(0)
        matrix.append(line)
    return matrix

''' Tests '''
m0 = id_mtrx(0) # empty matrix
print("\nid_mtrx(0):")
print(m0)
m0 = id_mtrx(0.0) # float input
print("\nid_mtrx(0.0):")
print(m0)
m0 = id_mtrx('0') # String input
print("\nid_mtrx('0'):")
print(m0)
m0 = id_mtrx([0]) # integer list input
print("\nid_mtrx([0]):")
print(m0)
m1 = id_mtrx(1) # 1x1 Identity matrix (list consisting of a list consisting of one element: 1)
print("\nid_mtrx(1):")
print(m1)
m2 = id_mtrx(-1) # 1x1 Identity matrix (list consisting of a list consisting of one element: 1)
print("\nid_mtrx(-1):")
print(m2)
m3 = id_mtrx(3) # 3x3 matrix
print("\nid_mtrx(3):")
for elem in m3:
    print(elem)
m4 = id_mtrx(-3) # 3x3 Inverse Identity matrix
print("\nid_mtrx(-3):")
for elem in m4:
    print(elem)
m5 = id_mtrx(15) # 15x15 matrix
print("\nid_mtrx(15):")
for elem in m5:
    print(elem)
m6 = id_mtrx(-15) # 15x15 Inverse Identity matrix
print("\nid_mtrx(-15):")
for elem in m6:
    print(elem)
print()