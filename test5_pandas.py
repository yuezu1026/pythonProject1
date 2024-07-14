import numpy as np
import pandas as pd
data = pd.Series([4,3,5,6,1])

print(data)
print(data.values)
print(data.index)

print(type(data))

print(type(data.values),data.values)
print(type(data.index),data.index)

#dsdsfl

data = pd.Series([5,4,6,3,1],index=['one','two','three','four','five'])
print(data)

data = pd.Series([4,3,2,1],index=list('abcd'))
print(data)

pop_dict = {'bj':3000,'gz':1500,'xa':100}
pop_series = pd.Series(pop_dict)
print(pop_series)

data = pd.Series(10,index=[4,3,2,1])
print(data)

dataframe = pd.DataFrame([[1,2,np.nan],[4,np.nan,6],[5,6,7]])
print(dataframe.dropna(axis='columns')) #按列删除缺失值
print(dataframe)

data = pd.Series([3,4,np.nan,1.5,None])

print('以0进行填充')

print(data.fillna(0))
print(data.fillna(method='ffill'))


print(data.fillna(method='bfill'))

