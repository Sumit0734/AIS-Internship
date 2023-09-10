#!/usr/bin/env python
# coding: utf-8

# In[13]:


#odd even using while loop

i = int(input("Enetr the number :"))
while i%2 == 0:
    print(i, "is a even number")
else:
    print(i, "is odd number")
 


# In[14]:


# Pattern

a=1
while a<=5:
    print("*" * a)
    a=a+1
    


# In[23]:


# creat list 1-20 numbers list using while loop=> [1,2,3... 20]
a=[]
b=1
while b<=20:
    a.append(b)
    b=b+1
print(a)


# In[24]:


# creat list 20-1 (revers order) using while loop=> [20,19...1]
a=[]
b=20
while b>=1:
    a.append(b)
    b=b-1
print(a)
    


# In[2]:


# using break statement
i=1
while i<=10:
    print("6 * ",i,"=",6*i)
    if i>=5:
        break
    i=i+1


# In[13]:


# find odd numbers 1to 10 using continue statement
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue
    print(a)
    


# In[15]:


#  using pass statement
i=1
while i<=10:
    i=i+1
    print("Sumit")
pass
    
    


# In[ ]:




