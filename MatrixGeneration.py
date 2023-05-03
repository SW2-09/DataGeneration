import numpy as np

size = 100
arr = np.random.randint(0,10,(size,size))
np.savetxt('matrixA100.csv',arr, fmt = '%d', delimiter=",")
arr2 = np.random.randint(0,10,(size,size))
np.savetxt('matrixB100.csv',arr2, fmt = '%d', delimiter=",")