import csv
from matrix_ops import *
from matrix_ops import myArray as my

x_vars = ['x1', 'x2', 'x3']
y_vars = ['y']

fit_intercept = True

with open('datasets\lin_reg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)

    header = next(csv_reader, None)[0].split(',')

    x_indices = [i for i, j in enumerate(header) if j in x_vars]
    y_indices = [i for i, j in enumerate(header) if j in y_vars]
    
    x, y = [], []
    
    for row in csv_reader:
        r = row[0].split(',')
        read_row = [float(j) for i, j in enumerate(r) if i in x_indices]

        if fit_intercept:
            read_row.extend([1])
        
        x.append(read_row)
        y.append([float(j) for i, j in enumerate(r) if i in y_indices])
    
    x = myArray(x)
    y = myArray(y)

    z = x.t()*x
    xtx_inv = myArray.getMatrixInverse(z.array)
    alpha = (xtx_inv*x.t())*y
    
    if fit_intercept:
        print('Estimated slopes of the Linear Regression:', *[i[0] for i in alpha.array[:-1]])
        print('Estimated intercept of the Linear Regression:', *alpha.array[-1])
    else:
        print('Estimated slopes of the Linear Regression:',  *[i[0] for i in alpha.array])

