#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list datatype:


# In[1]:


students = ['sri','harsha','rishi','aasya','shrika']


# In[2]:


print(students)


# In[ ]:


indexing:0,1,2,3,4,5-------


# In[3]:


print(students[1])


# In[4]:


print(students[4])


# In[5]:


print(students[4].title())


# In[ ]:


adding new students to the list : use append.


# In[6]:


students.append('sloka')


# In[7]:


print(students)


# In[8]:


students.append('swathi')


# In[9]:


print(students)


# In[10]:


students.insert(4,'aanya')


# In[11]:


print(students)


# In[16]:


print(students[4].title())


# In[ ]:


modifying:


# In[17]:


students[0] = 'chandana'


# In[18]:


print(students)


# In[ ]:


deleting:(permanant deleting)


# In[19]:


del students[6]


# In[20]:


print(students)


# In[ ]:


temporary deleting: use pop (then it will temporarily delete the last element and save it as carbon copy)


# In[21]:


X = students.pop()


# In[22]:


print(students)


# In[24]:


print(X)


# In[ ]:


Negative Indexing: -1,-2,-3........called reverse indexing.


# In[25]:


print(students[-1])


# In[ ]:




