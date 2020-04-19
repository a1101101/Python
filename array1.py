import numpy as np
	     
x = np.array([[1,2,3],[4,5,6]],np.int32)

print(type(x))
print(x.dtype)
print(x[1,2])
	     
y = x[:1]

print(y)

y = x[:,1]
	     
print(y)

x = np.array([[0,1],[0,1],[0,1]])
	     
print(x[:,1])
print(x[:,:])

x[:,1] = [2,2,2]
	     
print(x)
