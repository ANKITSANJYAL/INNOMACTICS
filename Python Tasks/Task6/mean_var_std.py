import numpy as np
n, m = map(int, input().split())
k = np.array([input().split() for _ in range(n)],dtype = int)
np.set_printoptions(legacy='1.13')
print(np.mean(k,axis=1), np.var(k,axis=0), np.std(k), sep='\n')