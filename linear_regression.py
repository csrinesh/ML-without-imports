import csv
from matrix_ops import matmul, getTranspose, getMatrixInverse

x_vars = ['x1', 'x2', 'x3']
y_vars = ['y']

with open('datasets\lin_reg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)

    header = next(csv_reader, None)[0].split(',')

    x_indices = [i for i, j in enumerate(header) if j in x_vars]
    y_indices = [i for i, j in enumerate(header) if j in y_vars]
    
    x = []
    y = []

    for row in csv_reader:
        r = row[0].split(',')
        x.append([float(j) for i, j in enumerate(r) if i in x_indices])
        y.append([float(j) for i, j in enumerate(r) if i in y_indices])

    alpha = matmul(matmul(getMatrixInverse(matmul(getTranspose(x), x)), getTranspose(x)), y)
    print(alpha)
