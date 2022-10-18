import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('file.csv')
age=list(df.age)
city=list(df.home_city)
salary=list(df.salary)
plt.pie(age,labels=city)
plt.title('Age wise')
plt.show()
plt.pie(salary,labels=city)
plt.title('Salary wise')
plt.show()
plt.bar(city,salary)
plt.title('Salary wise')
plt.show()
plt.bar(city,age)
plt.title('Age wise')
plt.show()
from sklearn.datasets import load_boston
import pandas as pd
df=load_boston()
dfx=pd.DataFrame(df.data,columns=df.feature_names)
dfy=pd.DataFrame(df.target)
print(dfx)
print(dfy)

import matplotlib.pyplot as plt
plt.boxplot(dfx['AGE'])
plt.title('Boxplot for age')
plt.grid(True)
plt.show()
plt.boxplot(dfx['TAX']) #Price is tax here
plt.title('Boxplot for price')
plt.grid(True)
plt.show()

q1=dfx.quantile(0.25)
q3=dfx.quantile(0.75)
iqr=q3-q1
lo=q1-(1.5*iqr)
uo=q3+(1.5*iqr)
(dfx[(dfx<lo) | (dfx>uo)]).notnull

print('Mean: \n \n', dfx.mean())
print('\n Q1: \n', dfx.quantile(0.25))
print('\n Q3: \n', dfx.quantile(0.75))
print('\n Max: \n', dfx.max)
print('\n Min: \n', dfx.min )

dfx.isnull().sum()

dfx.corr()
import pandas as pd
df=pd.read_csv('file.csv')
df

import matplotlib.pyplot as plt
age=list(df.age)
age=list(df.age)
salary=list(df.salary)
plt.scatter(age,salary)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

plt.hist(age,bins = 70)
plt.xlabel('Age')
plt.ylabel('Value')
plt.grid(True)
plt.title('Age histogram')
plt.show()
plt.hist(salary, bins= 70)
plt.xlabel('Salary')
plt.ylabel('Values')
plt.title('Salary histogram')
plt.grid(True)
plt.show()

city=list(df.home_city)
plt.pie(age,labels=city)
plt.show()

plt.boxplot(age)
plt.title('Age boxplot')
plt.grid(True)
plt.show()
plt.boxplot(salary)
plt.title('Salary boxplot')
plt.grid(True)
plt.show()
arr=datasets.load_iris().data
df=pd.DataFrame(arr,columns=['sepal.length','sepal.width','petal.length','petal.
,→width'])
df

print('Mean: \n',df.mean(axis=0))
print('\n Mode: \n',df.mode(axis=0))
print('\n Median: \n',df.median(axis=0))
print('\n Standard deviation \n',df.std(axis=0))

df['sepal.length'].corr(df['sepal.width'])

df['sepal.length'].cov(df['petal.length'])

pd.crosstab(df['sepal.length'],['sepal.width']).head()

import pandas as pd
df_h=pd.read_csv('hepatitis.csv')
df_a=pd.read_csv('auto.csv')

print('Hepatitis:',len(df_h.index)*len(df_h.columns) - df.isna().sum().sum())
print('Auto: ',len(df_a.index)*len(df_a.columns) - df_a.isna().sum().sum())

df_h.dropna
df_a.dropna
print('All na values dropped')

df_a[0:1].abs
df_h[0:1].abs
print('Absolute used to normalize')

import matplotlib.pyplot as plt
col1=df_a['1'].sum()
col2=df_h['1'].sum()
list_a=[col1,col2]
plt.hist(list_a)


import pandas as pd
df=pd.read_csv('fileiris.csv')
df
print('Columns:',len(df.columns))
print('Rows:',len(df.index))

print('Correlation:', df['sepal.length'].corr(df['sepal.width']))
print(pd.crosstab(df['sepal.length'],df['sepal.width']).head())

print(df.var())
print(df.var().max())

petal_len=list(df['petal.length'])
petal_wid=list(df['petal.width'])
corr=str(df['petal.length'].corr(df['petal.width']))
plt.scatter(petal_len,petal_wid)
plt.grid(True)
plt.xlabel('Length')
plt.ylabel('Breadth')
plt.title('Petal Correlation: ' + corr)
import pandas as pd
df=pd.read_csv('carname.csv')
df
print('Most popular car: ',df.car[df.popularity==df.popularity.max()])
import matplotlib.pyplot as plt
labels=list(df.car)
values=list(df.popularity)
plt.pie(values,labels=labels)
plt.show()

cost=list((df.cost).head(2))
cost_new=[]
for i in cost:
cost_new.append(i/1000)
capacity=list((df.capacity).head(2))
cap_new=[]
for j in capacity:

21

cap_new.append(j/100)
plt.bar(cap_new,cost_new)
plt.xlabel('Capacity in hundreds')
plt.ylabel('Cost in hundreds')
plt.grid(True)
plt.show()

car=list(df.car)
popu=list(df.popularity)
d={}
for i in range(len(car)):
d[car[i]]=popu[i]
from wordcloud import WordCloud
wordcloud= WordCloud(background_color='black',

width=1500,
height=1000).generate_from_frequencies(d)

plt.imshow(wordcloud)
plt.show()

