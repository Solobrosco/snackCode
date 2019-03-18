
# coding: utf-8

# # Here is the python code for the bonus HW

# # Nikko Solon

# In[1]:


import math #for math functions


# 1. Implement python functions for all logical operators:

# 1.1 AND (p and q)

# In[2]:


def AND(p,q):
    if p == True and q == True:
        #print("p AND q = True")
        return True
    else:
        #print("p AND q = false")
        return False


# 1.2 OR (p or q)

# In[3]:


def OR(p,q):
    if p == True or q == True:
        #print("p OR q = True")
        return True
    else:
        #print("p OR q = false")
        return False


# 1.3 IF (p->q)

# In[4]:


def IF(p,q):
    if p == q:
        #print("If p Then q = True")
        return True
    elif p == True and q == False:
        #print("If p Then q = False")
        return False
    else:
        #print("If p Then q = False")
        return True


# 1.4 NOT (-p)

# In[5]:


def NOT(p):
    if p == True:
        #print("Not p = False")
        return False
    else:
        #print("Not p = True")
        return True


# 1.5 IFF(p<->q)

# In[6]:


def IFF(p,q):
    if p == q:
        #print("p If And Only IF q = True")
        return True
    else:
        #print("p If And Only IF q = False")
        return False


# 1.6 Give a prefix representation of a proposition, of the form prop = ('OR', True, False). Write a function named evaluation, which will evaluate the proposition. You should use the functions defined in questions 1.1-1.5

# In[7]:


def evaluation(f,p,q):
    if f == AND:
        return AND(p,q)
    if f == OR:
        return OR(p,q)
    if f == IF:
        return IF(p,q)
    if f == NOT:
        return NOT(p)
    if f == IFF:
        return IFF(p,q)


# In[8]:


print("Simple Evaluation Fuction Test")
print()
p = False
q = False
print("(p and q):",evaluation(AND,p,q))
print("(p or q):",evaluation(OR,p,q))
print("(p -> q):",evaluation(IF,p,q))
print("(p <-> q):",evaluation(IFF,p,q))
print("(-p):",evaluation(NOT,p,q))


# 2. Develop the following python program.
# Implement Cartesian production of two sets. For example,
# x = [‘a’, ‘e’]
# y = [1, 3, 7, 9]

# In[9]:


def cartesian_Product(x,y):
    #So this loop will go through elements in x
    for i in range(len(x)):
        first = x[i]
        #Then as one element from x is chosen the 
        #rest of elements in y are multiplied with the ith of x
        for j in range(len(y)):
            second = y[j]
            print("(",first,",",second,")")


# In[10]:


x = ['a','e','here']
y = [1,3,7,9,0]
cartesian_Product(x,y)


# 3. Given two sorted lists, it is possible to merge them into one sorted lists in an efficient way. Design and implement a divide and conquer algorithm to merge two sorted lists.

# In[11]:


def merge(list1,list2):
    l1=len(list1)
    l2=len(list2)
    i=j=0
    l=[]
    while i<l1 and j<l2:
        if list1[i]<list2[j]:
            l.append(list1[i])
            i=i+1
        else:
            l.append(list2[j])
            j=j+1
    while i<l1:
        l.append(list1[i])
        i=i+1
    while j<l2:
        l.append(list2[j])
        j=j+1
    return l

x=[1,3,5,7]
y=[2,4,6,8]
print("merge([1,3,5,7],[2,4,6,8]):\t",merge(x,y))


# 4. Implement Euclid's Algorithm for finding the greatest common divisor of two integer

# In[12]:


def gcd(a,b):
    #Provide Euclid's Algorithm here.
    while a is not b:
        if a > b:
            a=a-b
        else:
            b=b-a
    return b
print(gcd(128,60))

