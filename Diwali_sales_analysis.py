#!/usr/bin/env python
# coding: utf-8

# In[116]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[114]:


df=pd.read_csv(r'C:\Users\Priyanka\Downloads\Diwali Sales Data.csv', encoding='unicode_escape')


# In[115]:


df.shape


# In[20]:


df.head()


# In[23]:


df.info()


# In[28]:


#DROP UNRELATED/BLANKS COLUMNS
df.drop(['Status', 'unnamed1'], axis=1,inplace=True)


# In[30]:


df.info()


# In[31]:


pd.isnull(df)


# In[32]:


#check for null values
pd.isnull(df).sum()


# In[34]:


df.shape


# In[35]:


#drop null values
df.dropna(inplace=True)


# In[36]:


df.shape


# In[37]:


pd.isnull(df).sum()


# In[60]:


#initialize lists of lists
data_test = [['Madhav',11], ['Gopi',15], ['keshav', ], ['lalita',16]]


#create the pandas Dataframe using list 
df_test = pd.DataFrame(data_test, columns=['Name', 'Age'])

df_test


# In[66]:


df_test.dropna(inplace= True) #for changes save in column to use inplace


# In[67]:


df_test


# In[68]:


#both are same thing
#df_test.dropna(inplace=True)  #### assign value inplace
#df_test = df_test.dropna()      ####without inplace.... assign variable)


# In[69]:


#change data type
df['Amount'] = df['Amount'].astype('int')


# In[70]:


df['Amount'].dtypes


# In[71]:


df.columns


# In[72]:


#rename column
df.rename(columns = {'Marital_Status':'Shaadi'})


# In[73]:


#describe() method returns description of the data in the dataFrame(i.e. count,mean,std,etc)
df.describe()


# In[74]:


#use describe() for specific columns
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 

# # Gender
# 

# In[79]:


df.columns


# In[81]:


ax=sns.countplot(x='Gender',data = df)


# In[82]:


ax=sns.countplot(x='Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[86]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[89]:


sales_gen =df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x= 'Gender',y='Amount',data =sales_gen)


# In[ ]:


# from above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than man


# # Age

# In[92]:


df.columns


# In[98]:


ax=sns.countplot(data=df,x='Age Group')


# In[101]:


ax =sns.countplot(data = df, x ='Age Group', hue= 'Gender')


# In[102]:


ax =sns.countplot(data = df, x ='Age Group', hue= 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[104]:


#total Amount vs age group 
sales_age =df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Age Group',y='Amount', data =sales_age)


# In[105]:


#from above graphs we can see that most of the  buyers are of age group between -yrs female


# # State

# In[106]:


df.columns


# In[112]:


#total number of orders from top 10 states

sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state,x='State',y ='Orders')
    


# In[119]:


#TOTAL AMOUNT/SALES FROM TOP 10 STATES

sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data= sales_state,x='State',y ='Amount')


# In[123]:


###***from above graphs we can see that most of the orders are from Uttar Pradesh,Maharashtra and Karnataka respectively***


# # Martial Status

# In[128]:


ax = sns.countplot(data=df,x= 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[137]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(7,5)})
sns.barplot(data=sales_state,x='Marital_Status', y='Amount', hue ='Gender')


# In[136]:


##fromabove graphs we can see that most of the buyers are married (women) and they have high purchasing power


# # Occupation

# In[138]:


sns.set(rc={'figure.figsize':(20,5)})
ax=sns.countplot(data=df,x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[140]:


sales_state = df.groupby(['Occupation','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data =sales_state, x='Occupation',y ='Amount')


# In[141]:


### from above graphs we can see that most of the buyers are woirking in IT, aviation and Heathcare sector


# In[142]:


df.columns


# # Product Category

# In[146]:


sns.set(rc={'figure.figsize':(21,5)})
ax=sns.countplot(data=df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[149]:


sales_state = df.groupby(['Product_Category','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(21,5)})
sns.barplot(data =sales_state, x='Product_Category',y ='Amount')


# In[150]:


### from above graphs we can see that most of the sold products are from food , foodwear and Electrinics category


# In[151]:


sales_state = df.groupby(['Product_ID','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(21,5)})
sns.barplot(data =sales_state, x='Product_ID',y ='Amount')


# In[153]:


#top 10 most sold products (same thing as above)

fig1,ax1=plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# In[ ]:


##Married women age group 26-35 yrs from UP,Maharastra and Karnatak

