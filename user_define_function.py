#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(a,b):
    c=a+b
    return(c)
add(12,2)
    
    


# In[12]:


# pattern using function

def star(a):
    for i in range(0,a):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
        
star(3)


# In[13]:


# Multiplication of three values

def mult(a,b,c):
    d=a*b*c
    return(d)
mult(2,3,4)


# In[20]:


# power raised to 3
def power(a):
    b=a*a*a
    return(b)
power(3)
    


# In[21]:


# n raised to 4

def power(a):
    b=a*a*a*a
    return(b)
power(3)


# In[26]:


def power(a):
    if a!=a:
        b=a*a
        return(b)
power(3)


# In[3]:


# variance of 5 values

import statistics as s
a=[]
for i in range(10,15):
    a.append(i)
var=(s.variance(a))
print("The variance of above the numbers are :",var)


# In[5]:


# variance of given numbers

import statistics as s
a=[1,2455,65,45,12,5]
print(s.variance(a))


# In[8]:


# factorial

def fact(n):
    if n==0 | n==1:
        return 1
    else:
        return(n* fact(n-1))
    print(fact(n))
fact(3)
    


# In[19]:


# addition of even number

def even_add(number):
    a=0
    for i in number:
        if i % 2 ==0:
           a=a+i
    return a
number=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]
even_add(number)
            


# In[20]:


#print name

def name():
    for i in range(1,36):
        print(i,"Sumit")
name()


# In[21]:


#list of specific range
def create_list(a,b):
    i=1
    c=[]
    for i in range(a,b):
        c.append(i)
        i+i+1
    print(c)
create_list(20,56)


# In[ ]:




