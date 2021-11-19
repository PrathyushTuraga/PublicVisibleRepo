import matplotlib.pyplot as plt
from matplotlib import style
'''
#plt.plot([1,3,5,10],[10,20,60,125])
#plt.show()

#style.use('bmh')
#style.use('classic')
style.use('dark_background')
x = [2,4,6]
y = [4,8,24]
x2 = [3,6,9]
y2 = [10,15,30]
plt.plot(x,y)
plt.plot(x2,y2)
plt.title('test')
plt.xlabel('test x values')
plt.ylabel('test y values')
plt.show()
'''
'''
style.use('bmh')
x1 = [2,4,6]
y1 = [3,6,9]
x2 = [4,8,12]
y2 = [5,10,15]
x3 = [6,12,18]
y3 = [12,24,36]
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.bar(x3,y3)
plt.title('test graph 1')
plt.xlabel('test x name')
plt.ylabel('test y name')
plt.show()
'''
'''
style.use('dark_background')
numbers = [1,4,55,23,67,33,1,5,24,56,76,89,27,93]
jumps = [0,15,30,45,60,75.90,105]
plt.hist(numbers,jumps,histtype='bar')
plt.title('test 1 hist')
plt.xlabel('test x label')
plt.ylabel('test y label')
plt.show()
'''
'''
style.use('classic')
food = ['pizza','ice cream','burgers']
sales = [20, 10, 30]
color = ['red','blue','yellow']
plt.pie(sales,labels=food,colors=color)
plt.title('example food')
plt.show()
'''
x = [3,6,7,9,10]
y = [5,10,25,3,1]
style.use('dark_background')
plt.title('test scatter')
plt.xlabel('test x')
plt.ylabel('test y')
plt.scatter(x,y)
plt.show()
