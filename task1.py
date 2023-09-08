#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Grade code

p=95
if p>=75:
    print("O grade")
elif 75>p>=65:
    print("A grade")
elif 65>p>=55:
    print("B grade")
elif 55>p>=45:
    print("C grade")
elif 45>p>=35:
    print("pass")
else:
    print("Fail")


# In[7]:


# n divisible by 2 or 3,n=7
n=7
if(n%2 | n%3):
    print("Yes")


# In[9]:


# find odd numbers 20 to 40

i=20
for i in range(20,40):
    if(i%2==1):
        print(i)


# In[16]:


#creat a list of 1 to 20 numbers using for loop
a=[]
for i in range(1,21):
    a.append(i)
    print(a)
    


# In[8]:


#creat a list of 20 to 1 numbers using for loop(dont use reverse)
a=[]
for i in range(20,0,-1):
    a.append(i)
    print(a)


# In[21]:


#cube of odd values between 20 to 40
for i in range(20,40):
    if i%2==1:
        print(i**3)


# In[26]:


#create a list

name=["A","B","C","D","E"]
age=[21,22,23,24,25]
for i in range(0,len(age)):
    print("My name is",name[i],"and age is",age[i])


# In[29]:


# Sum of only non negative numbers

a=[1,4,-5,-15,10]
sum=0
for i in range(len(a)):
    if a[i]>0:
        sum=sum+a[i]
        print(sum)
        


# In[38]:


# Find factorial numbers

a=int(input("Enter a number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)


# In[11]:


# Swap first and last element of list

l=[10,20,30,40,50]
a=len(l)
l[0],l[-1]=l[-1],l[0]
print(l)


# In[12]:


# Count length of string
a=sorted("Sumit")
print(len(a))


# In[ ]:




