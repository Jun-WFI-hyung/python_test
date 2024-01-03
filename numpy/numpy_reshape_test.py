import numpy as np

# 원소 순서 유지 됨.
a = np.array([1,2,3,4,5,6,7,8,9], dtype=np.uint32)
b = a.reshape((-1,3))
print(b)
c = b.reshape((-1))
print(c)