#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import glob
import os
import numpy as np
import json


# In[74]:


# Open the folder of csv files and concatenate them into one dataframe
# TODO save concatenated dataframe as csv file
path = r'./data'
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
pd.concat(df_from_each_file, ignore_index=True).to_csv('./data/merged.csv')


# In[53]:


df = pd.read_csv('./data/merged.csv')
df.drop(['Unnamed: 0'], axis=1, inplace=True)


# In[54]:


df.columns


# In[55]:


df_json_col = df[['category', 'location',  'profile', 'urls']]

for col in df_json_col.columns:
    print(df[col][0])


# In[61]:


def depurate_json(df, colum):
    try:
        df[colum] = df[colum].apply(lambda x: json.loads(x))
    except:
        print('error')


# In[63]:


remove = ['backers_count', 'id', 'permissions', 'location', 'photo', 'disable_communication', 'slug', 'converted_pledged_amount', 
       'source_url',  'creator', 'friends', 'profile', 'urls', 'is_backing', 'is_starrable', 'is_starred',
        'usd_type', 'static_usd_rate', 'currency_symbol','currency_trailing_code', 'current_currency', 'fx_rate']


# In[64]:


df.drop(remove, axis=1, inplace=True)


# In[65]:


categories = df['category'].apply(json.loads)

df['category_name'] = categories.apply(lambda x: x['name'])
df['category_slug'] = categories.apply(lambda x: x['slug'])


# In[66]:


df.drop(['category'], axis=1, inplace=True)


# In[67]:


df.info()


# In[68]:


# Save the dataframe as a csv file

df.to_csv('./data/procesed.csv')


# In[ ]:




