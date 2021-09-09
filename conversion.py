#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Asset conversion


# In[70]:


from forex_python.converter import CurrencyRates
import cryptocompare
import numpy as np
import pandas as pd


# In[71]:


c = CurrencyRates()
price = c.get_rate('USD', 'AUD')


# In[72]:


price = [price]
price


# In[73]:


df2 = pd.DataFrame(price, index=['AUD'], columns=['USD'])
df2


# In[74]:


df = pd.DataFrame(cryptocompare.get_price(['BTC','ETH'], ['AUD']))
df


# In[75]:


df['USD'] = df2['USD']
df


# In[76]:


write = df.to_excel(r"C:\Documents\Finance\conversion.xlsx",sheet_name="conversion")


# In[ ]:




