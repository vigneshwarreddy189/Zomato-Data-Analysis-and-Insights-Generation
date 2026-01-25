import numpy as np
import pandas as pd

#zomato dataset loaded
data = pd.read_csv("C:/Users/tammi/Desktop/cleaned zomato through excel.csv", encoding='latin1')

'''
dataset basic information checking
print(data.head())
print(data.tail())
data.info()
print(data.describe())
print(data.shape)
print(data.columns)

print(data.isnull())

print(data.dropna())
'''
#print(data.to_string())
print(data.columns)
