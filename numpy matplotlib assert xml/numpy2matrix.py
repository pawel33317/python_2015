import numpy as np
A = np.arange(1,101)
A = A.reshape(10,10,order="F")

B = np.arange(100,0,-1)
B = B.reshape(10,10,order="C")

C = A+B
C[1][-1] *=2
print C
print np.median(C,axis=0)
print np.ptp(C, axis=0)
