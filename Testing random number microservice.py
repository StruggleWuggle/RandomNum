#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests


# In[10]:


def get_request(url):
    """
    Set up HTTP request framework
    """
    response = requests.get(url)
    if response.status_code == 200:
        try:
            json_data = response.json()
            return json_data
        except ValueError:
            return {'error': 'Invalid JSON'}
    else:
        return {'error': f'Request failed with status code {response.status_code}'}


# In[11]:


url = "http://127.0.0.1:5000/getRand"


# In[17]:


get_request(url)


# In[ ]:




