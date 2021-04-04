from itertools import starmap
from operator import mul

def matmul(a, b):
    # Check if all rows are of same length
    for i in [a, b]:
        it = iter(i)
        the_len = len(next(it))
        if not all(len(l) == the_len for l in it):
            raise ValueError('not all lists have same length!')
    
    # Check if matrix compatible
    if len(a[0]) != len(b):
        raise ValueError('not multiplication compatible')
    
    return [[sum(map(mul, row, col)) for col in zip(*b)] for row in a]

def getTranspose(x):
    return list(map(list, zip(*x)))

def getMatrixMinor(x,i,j):
    return [row[:j] + row[j+1:] for row in (x[:i]+x[i+1:])]

def getMatrixDeternminant(x):
    if len(x) == 2:
        return x[0][0]*x[1][1]-x[0][1]*x[1][0]

    determinant = 0
    for c in range(len(x)):
        determinant += ((-1)**c)*x[0][c]*getMatrixDeternminant(getMatrixMinor(x,0,c))
    return determinant

def getMatrixInverse(x):
    determinant = getMatrixDeternminant(x)
    #special case for 2x2 matrix:
    if len(x) == 2:
        return [[x[1][1]/determinant, -1*x[0][1]/determinant],
                [-1*x[1][0]/determinant, x[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(x)):
        cofactorRow = []
        for c in range(len(x)):
            minor = getMatrixMinor(x,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = getTranspose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors