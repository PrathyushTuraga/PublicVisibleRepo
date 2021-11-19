import pandas as pd
#print('Hello World')
'''
Employee = {'number':[1,2,3,4,5],'name':["abby","john","lina","marc","bob"],'hourly salary':[15,25,32,27,40]}
table1 = pd.DataFrame(Employee)
#print(table1)
print(table1.head(1))
print(table1.tail(1))
'''
'''
food1 = {'number':[1,2,3,4,5],'name':['corn','banana','chips','popcorn','pizza'],'price':[8,3,4,8,6]}
food2 = {'number':[1,2,3,4,5],'name':['apple','banana','beans','popcorn','pizza'],'price':[2,3,4,8,6]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

#fusion = pd.merge(table1,table2)
fusion_common_name = pd.merge(table1,table2,on='name')
fusion_common_number = pd.merge(table1,table2,on='number')
#print(fusion)
print(fusion_common_name)
print(fusion_common_number)
'''
'''
food1 = {'number':[1,2,3,4,5],'name':['apple','banana','chips','popcorn','pizza'],'price':[2,6,4,3,5]}
food2 = {'color':['red','yellow','orange','white','blue'],'weight':[100,200,150,175,225],'qt':[1,2,1,3,4]}
table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = table1.join(table2)
print(fusion)
'''
color = pd.read_csv('C:\\Users\\prath\\OneDrive\\PythonTutorial\\DataScience1\\work.csv')
print(color)
color.to_html('NiceColor.html')

