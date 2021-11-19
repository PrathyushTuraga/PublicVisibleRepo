import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

person = {'finance':    [3,4,5,4,5,8,7,3,9,6,3,5,7,10,5,6,3,2,6,7],
          'management': [1,5,6,4,5,8,4,9,4,6,3,5,7,10,5,6,3,2,6,7],
          'logistic':   [4,5,6,4,5,8,7,3,9,6,3,5,7,4,3,8,9,3,6,7],
           'get_work':   [1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1]
           }

Data = pd.DataFrame(person,columns=['finance','management','logistic','get_work'])
#print(Data)
X = Data[['finance','management','logistic']]
y = Data['get_work']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
lr = LogisticRegression()
lr.fit(X_train,y_train)
y_prediction = lr.predict(X_test)

conf_mat = pd.crosstab(y_test,y_prediction,rownames=['True'],colnames=['prevision'])
sn.heatmap(conf_mat,annot=True)
print('Accuracy: ',metrics.accuracy_score(y_test,y_prediction))
plt.show()
