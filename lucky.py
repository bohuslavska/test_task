#!/usr/bin/env python
# coding: utf-8

# ## Lucky series

# In[1]:


user_input = str(input("Enter:"))


# In[2]:


#Let's create a list of digits without 5 and 6 and turn these digits into the strings.

without_56 = [1,2,3,4,7,8,9,0]
without_56_str = [str(x) for x in without_56]


# In[3]:


#Now let's replace all unlucky digits with whitespaces.

for i in user_input:
    if i in without_56_str:
         user_input = list(map(lambda x: x.replace( i, ' '), user_input))
print(user_input)


# In[4]:


#Let's join all the lucky digits, split them by space, and make a list of all lucky series.

lucky_digits_ws = ''.join(user_input)
lucky_list = lucky_digits_ws.rsplit()
lucky_list


# In[5]:


#Let's check if these lucky series have appropriate lengths and different digits.

lucky_list_diff = []

if len(lucky_list) == 0:
    print(0)
else:
    for x in lucky_list:
        if len(x) >= 4 and str(x) != str(x)[0] * len(str(x)):
            lucky_list_diff.append(x)

    if len(lucky_list_diff) == 0:
        print(0)


# In[6]:


#Now we can print the longest lucky series.

lucky_series = max(lucky_list_diff, key = len)
print(lucky_series)

