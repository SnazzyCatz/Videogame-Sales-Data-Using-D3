#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("D:/Kaggle Projects/Videogame Sales/vgsales.csv")
data.head()


# In[2]:


data.describe()


# ## Have enough data so dropping 100 values out of 14,000 shouldn't impact results too much

# In[3]:


data.dropna(inplace=True)
data.isnull().sum()


# In[4]:


#Creates scaled data if needed
num_cols = ['NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
scaled_data = data.copy()
scaler = MinMaxScaler()
scaled_data[num_cols] = scaler.fit_transform(scaled_data[num_cols])
scaled_data


# In[5]:


regions = ['Global','NA','EU','JP']
Sales_By_Year_Global = []
Sales_By_Year_JP = []
Sales_By_Year_NA = []
Sales_By_Year_EU = []
i = 1980
while i <= 2006:
    Sales_By_Year_Global.append(data['Global_Sales'].where(data['Year'] == i).sum())
    Sales_By_Year_NA.append(data['NA_Sales'].where(data['Year'] == i).sum())
    Sales_By_Year_EU.append(data['EU_Sales'].where(data['Year'] == i).sum())
    Sales_By_Year_JP.append(data['JP_Sales'].where(data['Year'] == i).sum())
    i += 1


# ## Line Graph of Sales by Region Over Time

# In[6]:


dates = data.Year.unique()
dates = np.sort(dates)
plt.plot(Sales_By_Year_Global,label="Global Sales")
plt.plot(Sales_By_Year_NA, label="NA Sales")
plt.plot(Sales_By_Year_EU, label="EU Sales")
plt.plot(Sales_By_Year_JP, label="JP Sales")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Global Sales in Millions")
plt.show()


# ## Bar Plot of Sales By Console

# In[7]:



Sales_By_Platform_Global = {}
consoles = data.Platform.unique()
Sales_By_Platform_Global.fromkeys(consoles)
for console in consoles:
    Sales_By_Platform_Global[console] = (data['Global_Sales'].where(data['Platform'] == console).sum())

plt.bar(Sales_By_Platform_Global.keys(), Sales_By_Platform_Global.values(), color='g', align='center', width=0.5)
#plt.xticks(list(Sales_By_Platform_Global.keys()))

#set parameters for tick labels
plt.tick_params(axis='x', which='major', labelsize=5)
#plt.autoscale(tight='True')
plt.tight_layout()


# ## Barplot of Sales By Genre

# In[8]:


Sales_By_Type_Global = {}
Sales_By_Type_NA = {}
Sales_By_Type_EU = {}
Sales_By_Type_JP = {}

types = data.Genre.unique()
Sales_By_Type_Global.fromkeys(types)
for types in types:
    Sales_By_Type_Global[types] = (data['Global_Sales'].where(data['Genre'] == types).sum())
    Sales_By_Type_NA[types] = (data['NA_Sales'].where(data['Genre'] == types).sum())
    Sales_By_Type_EU[types] = (data['EU_Sales'].where(data['Genre'] == types).sum())
    Sales_By_Type_JP[types] = (data['JP_Sales'].where(data['Genre'] == types).sum())

plt.bar(Sales_By_Type_Global.keys(), Sales_By_Type_Global.values(), color='g', align='center', width=0.5)
plt.bar(Sales_By_Type_NA.keys(), Sales_By_Type_Global.values(), color='r', align='center', width=0.5)
plt.bar(Sales_By_Type_EU.keys(), Sales_By_Type_Global.values(), color='b', align='center', width=0.5)
plt.bar(Sales_By_Type_JP.keys(), Sales_By_Type_Global.values(), color='y', align='center', width=0.5)
plt.tick_params(axis='x',which='major',labelsize=7)
plt.show()


# 12 unique genres
# 31 consoles
# 38 Years of Data

# In[9]:


#Genre_Sales_Bin = {}
#types = data.Genre.unique()
#Genre_Sales_Bin.fromkeys(types)
#Genre_Sales_Bin = 
#print(Sales_By_Type_Global)
#print(Sales_By_Year_Global)
Sales_By_Year_Global = {}
years = data.Year.unique()
years.sort()
years = years[:-1]
years = years.astype(int)
Sales_By_Year_Global.fromkeys(years)
for years in years:
    Sales_By_Year_Global[years] = (data['Global_Sales'].where(data['Year'] == years).sum())
print(Sales_By_Year_Global,'\n\n',Sales_By_Platform_Global,'\n\n',Sales_By_Type_Global)


# ## This data will be used to create three graphs, one where we bin by sales for the year, one where we bin by sales for each genre, and one where we bin by sales for each platform

# In[10]:


console_dic = {'Console': list(Sales_By_Platform_Global.keys()),'Console_Sales':list(Sales_By_Platform_Global.values())}
genre_dic = {'Genre':list(Sales_By_Type_Global.keys()),'Genre_Sales':list(Sales_By_Type_Global.values())}
yearly_dic = {'Year':list(Sales_By_Year_Global.keys()),'Years_Sales':list(Sales_By_Year_Global.values())}
#print(type(Sales_By_Platform_Global.values()))
Console_Sales = pd.DataFrame.from_dict(console_dic)
Genre_Sales = pd.DataFrame.from_dict(genre_dic)
Yearly_Sales = pd.DataFrame.from_dict(yearly_dic)
#Console_Sales.append(Genre_Sales)
Console_Sales.to_csv(r'D:/Kaggle Projects/Videogame Sales/consoles.csv')
Genre_Sales.to_csv(r'D:/Kaggle Projects/Videogame Sales/genres.csv')
Yearly_Sales.to_csv(r'D:/Kaggle Projects/Videogame Sales/yearly.csv')


# In[ ]:





# In[ ]:





# In[ ]:




