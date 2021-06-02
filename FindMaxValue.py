#!/usr/bin/env python
# coding: utf-8

# In[110]:


arr = [8, 3, 1, 2]
maxSum = 0
tempSum = 0
final = []
index = 0


# In[ ]:





# In[ ]:





# In[103]:



n = len(arr)
sumArray = 0
prSum = 0
for i in range(len(arr)):
  sumArray += arr[i]
  prSum += i*arr[i]
maxSum = prSum
for i in range(1, len(arr)):
  prSum = prSum + sumArray - (n)*arr[n-i]
  if prSum > maxSum:
      maxSum = prSum
print(maxSum)


# In[100]:


print(maxSum)


# In[ ]:




