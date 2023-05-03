import numpy as np

size = 3000
arr = np.random.randint(0,10,(size,size))
np.savetxt('matrixA3k.csv',arr, fmt = '%d', delimiter=",")
arr2 = np.random.randint(0,10,(size,size))
np.savetxt('matrixB3k.csv',arr2, fmt = '%d', delimiter=",")