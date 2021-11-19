import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
'''
# data is pulled from github repo https://github.com/mwaskom/seaborn-data
database = sb.load_dataset('diamonds')
print(database)
sb.distplot(database['carat'],bins=1)
plt.show()

database = sb.load_dataset('dots')
print(database)
sb.distplot(database['coherence'])
plt.show()
'''
'''
database = sb.load_dataset('tips')
print(database)
sb.jointplot(x='tip',y='total_bill',data=database)
plt.show()
'''
'''
database = sb.load_dataset('flights')
#print(database)
sb.catplot(x='month',y='passengers',data=database,kind='box')
plt.show()
'''
database = sb.load_dataset('tips')
#print(database)
graph = sb.FacetGrid(data=database, col='sex',hue='smoker')
graph.map(plt.scatter,'total_bill','tip')
plt.show()











