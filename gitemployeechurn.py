#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
df= pd.read_csv(r'C:/users/Victor/Downloads/emp_churn_data .csv')
df                


# In[2]:


df.info()


# In[3]:


df.columns


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


dis = df['left'].value_counts()
print("left (1):", dis[1])
print("stayed (0):", dis[0])


# In[16]:


dis = df['left'].value_counts()

labels = ['stayed', 'left']
sizes = [dis.get(0, 0), dis.get(1, 0)]

plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
plt.title('Left Status Distribution')
plt.axis('equal')  
plt.show()


# In[25]:


#Plot the distribution of salary levels among those who left/stayed
sns.countplot(x='salary', hue='left', data=df)
plt.title('Salary Level Distribution Among Employees Who Left vs. Stayed')
plt.xlabel('Salary Level')
plt.ylabel('Count')
plt.show()


# In[28]:


#the distribution of tenure among those who left/stayed
sns.countplot(x='tenure', hue='left', data=df)
plt.title('Tenure Distribution Among Employees Who Left vs. Stayed')
plt.xlabel('tenure')
plt.ylabel('Count')
plt.show()


# Findings
# Employee Turnover:  29% of employees left the company, while 71% remained.
# Salary Influence:     A significant portion of those who left had medium salaries.
# Tenure Insight:      Employees with 4 to 8 years of tenure were most likely to leave the company.

# In[30]:


plt.figure(figsize=(15, 8))
sns.boxplot(data=df)

plt.show()


# In[ ]:




