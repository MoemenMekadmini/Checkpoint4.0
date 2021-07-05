#!/usr/bin/env python
# coding: utf-8

# In[3]:


def Max_numbers(x,y,z):
    if x>=y and x>=z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))
Max_numbers(x,y,z)


# In[14]:


def calculation(x,y):
    return x+y,x-y   
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
calculation(x,y)  


# In[42]:


def Multiply_list(list):
    M=1
    for j in list:
        M=M*j
    return M        
list = [1,5,3,2,1] 
Multiply_list(list)
def Sum_list(list):
    S=0
    for k in list:
        S=S+k
    return S
Sum_list(list)
def EvenSum(list, n):
    even_sum = sum(list[::2])
    print("Even index sum", even_sum) 
n = len(list)
EvenSum(list, n)



        


# In[36]:


n=input("enter a string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))


# In[31]:





# In[ ]:




