import scipy as sp
import numpy as np
from scipy import integrate
from scipy import cluster
from scipy import fftpack
from scipy import special
from scipy import linalg
'''
#help(integrate)
#sp.info(fftpack)
#sp.source(cluster)
'''
'''
#fun1 = special.kelvin(15)
#fun1 = special.xlogy(2,10)
#fun1 = special.exp10(50)
#fun1 = special.sindg(90)
fun1 = special.cosdg(90)
print(fun1)
'''
'''
#var1 = lambda x: x**3
#function1 = integrate.quad(var1,0,6)
#print(function1)
var1 = lambda y, x: x* y**6
function1 = integrate.dblquad(var1,0,6,lambda x:0, lambda x:1)
print(function1)
'''
'''
var1 = np.array([(2,4,6),(1,3,5)])
trans1 = sp.fftpack.fft(var1)
print(trans1)
'''
array1 = np.array([(1,3),(2,4)])
array2 = np.array([(5,9),(6,8)])
function1 = sp.linalg.solve(array1,array2)
function2 = sp.linalg.inv(array1)
print(function1)
print(function2)




