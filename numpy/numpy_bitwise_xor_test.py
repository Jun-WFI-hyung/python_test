import numpy as np

a = np.array([0,1,1,0,0,1], dtype=np.uint8).reshape((2,-1))
b = np.array([0,0,1,0,1,1], dtype=np.uint8).reshape((2,-1))
print(a)
print(b)
print(np.bitwise_xor(a,b))
