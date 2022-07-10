#!/usr/bin/env python
# coding: utf-8

# In[1]:


#we will do sum of n consecutive numbers


# In[28]:


n = input("Enter the number:")
#defining number as integer
n = int(n)
#creating a function for doing sum of n consequtive numbers
def sumof(n):
    sum_n = 0
    for a in range(n):
        a = a + 1
        sum_n += a
    return sum_n
print(f'The sum of first {n} consecutive numbers is {sumof(n)}')


# In[ ]:





# In[ ]:




