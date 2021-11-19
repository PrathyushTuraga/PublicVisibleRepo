import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,4,5,3,5,29,1,13,17,26])
func1 = np.polyfit(x,y,1)
#print(func1)
plt.plot(x,y,'.')
plt.plot(x,np.polyval(func1,x),'r-')
plt.show()
