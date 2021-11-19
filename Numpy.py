import numpy as np
#print('Hello World')
'''
var1 = np.array([(2,4,6),(1,3,5)])
print(var1)
print(var1.itemsize)
print(var1.dtype)
print(var1.ndim)
print(var1.size)
print(var1.shape)

var1 = var1.reshape(3,2)
print(var1)
'''

'''
#var2 = var1
#print(var1+var2)

#var1 = np.linspace(10,50,100)
var1 = np.array([(2,4,6),(1,3,5)])

#print(var1[0:,1])
print(var1.max())
print(var1.min())
print(var1.sum())
'''
'''
var1 = np.array([(2,4,6),(1,3,5)])
var2 = np.array([(5,9,3),(6,7,15)])
#print(var1+var2)
#print(var1.ravel())
#print(var1.sum(axis=1))
print(np.sqrt(var1))
print(np.std(var1))
'''

var1 = np.array([3,6,9])
print(np.exp(var1))
print(np.log(np.exp(var1)))

