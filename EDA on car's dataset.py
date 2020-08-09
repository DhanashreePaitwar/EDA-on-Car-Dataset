#!/usr/bin/env python
# coding: utf-8

# ### Goal : Performing EDA on car dataset and find insights from it.

# Exploring the dataset columns
# 1. Car       : The brand name of the car
# 2. MPG       : It is an abbreviation for "miles-per-gallon", it is used to indicate of the fuel economy of a car.
# 3. Cylinders : A cylinder is a power unit of an engines, it's a chamber where gasoline is burned and turned into power. generally engine with more cylinders produce more power and fewer cylinders gets better fuel economy.
# 4. Displacement : Engine displacement is defined as the total volume of air/fuel mixture an engine can draw in during one complete engine cycle.
# 5. Horsepower : The power produced by engine is known as horse power. For cars horsepower tranlate into speed.
# 6. Weight : Total mass of the car  with all equipments and operating consumables.
# 7. Acceleration : Acceleration means changing speed of the car with in the time. The car that can accelerate in a short amount of time is consider as good.
# 8. Model : model name or number of the car
# 9. origin : Origin place of the car.

# ####  Importing all necessary libraries

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ####  Loading dataset

# In[3]:


data=pd.read_csv('cars.csv')
data


# Here we can see data is not in the form of table, it is seprated by " ; " so we have to remove it and make our data in form of pandas dataframe. we can do this while reading the csv file

# In[4]:


data=pd.read_csv('cars.csv',sep=';')
data


# #### Exploring data by seeing top 5 row's and bottom 5 row's

# In[5]:


data.head()


# In[6]:


data.tail()


# ####  Explore columns of the data set

# In[7]:


data.columns


# In[8]:


data.index


# ####  how many records are present

# In[9]:


data.shape


# Observations :- 
#     1. car data set contains 407 rows and 9 columns

# In[10]:


data.ndim


# ####  Exploring data types

# In[11]:


data.info()


# #### Counting missing values
# 

# In[12]:


data.isnull().sum()


# In[13]:


data.isnull().mean()


# Observation : From above we can see our car dataset has 0 missing values.

# #### deleting 1st record

# In[14]:


data.head(3)


# Observation : Here 1st row of the data set is not informative so we dan drop 1st record

# In[15]:


data.drop(data.index[0],inplace=True)


# In[16]:


data.head(3)


# In[17]:


data.index


# Observation : Here we can see now the index starts from 1 rather than 0.

# #### Checking for duplicate rows

# In[18]:


data.duplicated().sum()


# observation : zero duplicate records are present in the car dataset.

# #### Finding unique values

# In[19]:


data['Car'].unique()


# In[20]:


data['MPG'].unique()


# In[21]:


data['Cylinders'].unique()


# In[22]:


data['Displacement'].unique()


# In[23]:


data['Horsepower'].unique()


# In[24]:


data['Acceleration'].unique()


# In[25]:


data['Weight'].unique()


# In[26]:


data['Model'].unique()


# In[27]:


data['Origin'].unique()


# In[28]:


data.info()


# Observation : we can see "cylienders","Displacement","Horsepower","Weight","Acceleration","Model" looks like a numerical variables. But after we study each columns unique values, they all fallls in a particular category. So therefore its data type is Objective.

# #### Statistical insights

# In[29]:


data.describe().T


# #### Graphical insights

# In[31]:


plt.figure(figsize=(15,10))
sns.countplot(x='Car',data=data)


# Observation : Hence here are lots of points so we are not able to see all things clearly and cannot decide anything. So to overcome this problem we will choose top frequent cars.

# In[39]:


data['Car'].value_counts()[:10].plot(kind='bar')


# Observation :  here we can see top 10 cars has maximum no. of frequencies. Toyota Corolla is quiet prefered and has high number of frequency.

# In[67]:


plt.figure(figsize=(15,10))
sns.countplot(x='MPG',data=data)


# In[70]:


data['MPG'].value_counts()[:20].plot(kind='bar')


# Observation : 
#        1.we can see that the few cars has a MPG of 0. 
#        2.Highest frequency of cars i.e 20 having 13.0 as Mpg.

# In[50]:


data['Cylinders'].value_counts().plot(kind='bar')


# Observation : 
#     1. Approximately 50% of car's having 4 cylinders.
#     2. Its rarley seen car's having 3 or 5 cylinders in it. 

# In[51]:


data['Origin'].value_counts().plot(kind='bar')


# Observation : 
#     1. More than 50 % car's has "US" origin.

# In[52]:


data['Model'].value_counts().plot(kind='bar')


# observation :
#     1. 73 is the popular model of the car with frequency of 40.
#     2. The data has information of 13 models.
#     3. Model number 71,80,79 has equal number of cars.

# In[55]:


data['Horsepower'].value_counts()[:10].plot(kind='bar')


# Above are the top 10 cars having highest horsepower.

# In[59]:


plt.figure(figsize=(15,10))
data['Weight'].value_counts()[:25].plot(kind='bar')


# In[61]:


data['Acceleration'].value_counts()[:10].plot(kind='bar')


# In[ ]:




