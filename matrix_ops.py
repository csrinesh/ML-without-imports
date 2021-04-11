from operator import mul, add

class myArray(object):
    def __init__(self, array):
        self.array = array
        self.shape = myArray.get_shape(self.array)

    @staticmethod
    def get_shape(obj, shape=()):
        if not isinstance(obj, list):
            return shape
        
        shape += (len(obj), )

        if isinstance(obj[0], list):
            if not all(len(item) == len(obj[0]) for item in obj):
                raise ValueError('All intra lists do not have shape length')
        shape = myArray.get_shape(obj[0], shape=shape)

        return shape
    
    def __repr__(self):
        return f'myArray{self.array}'

    def __add__(self, other):
        if len(self.shape) > 2:
            print('Only 2d arrays are supported')
            raise NotImplemented

        if self.shape == other.shape:
            return [list(map(lambda x, y: x+y, self.array[i] ,
             other.array[i])) for i in range(self.shape[:-1][0])]
        else:
            raise 'shape of the arrays incompatible for addition'

    def __sub__(self, other):
        if len(self.shape) > 2:
            print('Only 2d arrays are supported')
            raise NotImplemented

        if self.shape == other.shape:
            return [list(map(lambda x, y: x-y, self.array[i] ,
             other.array[i])) for i in range(self.shape[:-1][0])]
        else:
            raise 'shape of the arrays incompatible for subtraction'

    def __mul__(self, other):
        a, b = self.array, other.array
        for i in [a, b]:
            it = iter(i)
            the_len = len(next(it))
            if not all(len(l) == the_len for l in it):
                raise ValueError('not all lists have same length!')
        
        # Check if matrix compatible
        if len(a[0]) != len(b):
            raise ValueError('not multiplication compatible')
        
        return myArray([[sum(map(mul, row, col)) for col in zip(*b)] for row in a])
    
    def t(self):
        x = self.array
        return myArray(list(map(list, zip(*x))))

    @staticmethod
    def getTranspose(x):
        return list(map(list, zip(*x)))

    @staticmethod
    def getMatrixInverse(x):
        determinant = myArray.getMatrixDeterminant(x)
        #special case for 2x2 matrix:
        if len(x) == 2:
            return [[x[1][1]/determinant, -1*x[0][1]/determinant],
                    [-1*x[1][0]/determinant, x[0][0]/determinant]]

        #find matrix of cofactors
        cofactors = []
        for r in range(len(x)):
            cofactorRow = []
            for c in range(len(x)):
                minor = myArray.getMatrixMinor(x,r,c)
                cofactorRow.append(((-1)**(r+c)) * myArray.getMatrixDeterminant(minor))
            cofactors.append(cofactorRow)
        cofactors = myArray.getTranspose(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return myArray(cofactors)

    @staticmethod
    def getMatrixMinor(x,i,j):
        return [row[:j] + row[j+1:] for row in (x[:i]+x[i+1:])]

    @staticmethod
    def getMatrixDeterminant(x):
        if len(x) == 2:
            return x[0][0]*x[1][1]-x[0][1]*x[1][0]

        determinant = 0
        for c in range(len(x)):
            determinant += ((-1)**c)*x[0][c]*myArray.getMatrixDeterminant(myArray.getMatrixMinor(x,0,c))
        return determinant