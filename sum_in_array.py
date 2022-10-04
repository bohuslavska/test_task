#!/usr/bin/env python
# coding: utf-8

# ## Sum in array

# ### First function

# In[1]:


import time


# In[2]:


#Let's create the first function and measure the time of its execution.

def sum_in_array1(arr, arr_size, given_sum):
    solution_list = []
    for i in range(0, arr_size - 1):
        for j in range(i + 1, arr_size):
            if (arr[i] + arr[j] == given_sum):
                solution_list.extend([arr[i], arr[j]])
                return solution_list
    return [-1]


# In[3]:


get_ipython().run_cell_magic('time', '', '\narr = [-100, 200, -3, 50]\narr_size = len(arr)\ngiven_sum = 250\n\nsum_in_array1(arr, arr_size, given_sum)')


# In[4]:


get_ipython().run_cell_magic('time', '', '\narr = [-100, 200, -3, 50]\narr_size = len(arr)\ngiven_sum = 1000\n\nsum_in_array1(arr, arr_size, given_sum)')


# ### Second function

# In[5]:


#Let's create the second function and measure the time of its execution.

def sum_in_array2(arr, given_sum):
    dictionary = {}
    for i, value in enumerate(arr):
        rest = given_sum - arr[i]       
        if rest in dictionary:
            return [arr[i], arr[dictionary[rest]]]
        else:
            dictionary[value] = i            
    return [-1]


# In[6]:


get_ipython().run_cell_magic('time', '', '\narr = [-100, 200, -3, 50]\ngiven_sum = 250\n\nsum_in_array2(arr, given_sum)')


# In[7]:


get_ipython().run_cell_magic('time', '', '\narr = [-100, 200, -3, 50]\ngiven_sum = 1000\n\nsum_in_array2(arr, given_sum)')


# ## Conclusion

# > The second function performs better. I think it is because it has fewer for-loops.
