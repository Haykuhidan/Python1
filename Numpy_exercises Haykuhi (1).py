#!/usr/bin/env python
# coding: utf-8

# # Numpy exercises
# 

# #### 1. Import the numpy package under the name `np`
# 
# #### Import արեք numpy module-ը np անունով:

# In[1]:


import numpy as np


# #### 2. Create a numpy array of size 10 filled with zeros. 
# 
# #### Ստեղծեք 10 չափի 0-ներով լցված numpy array:

# In[7]:


a = np.array([0])
x = np.tile(a,10)
x


# #### 3.  How to get the documentation of the numpy add function? 
# 
# #### Նայեք numpy-ի add ֆունկցիայի դոկումենտացիան:

# In[10]:


help(np.add)


# #### 4.  Create a numpy array of size 10 filled with zeros but the fifth value is 1 
# 
# #### Ստեղծեք 10 չափի 0-ներով լցված numpy array, որի 5րդ արժեքը 1 է:

# In[133]:


b = np.zeros(10)
b[5] = 1
b


# #### 5.  Create a numpy array with values ranging from 10 to 49
# 
# #### Ստեղծեք 10-ից 49 հաջորդական թվերով numpy array:

# In[18]:


c = np.arange(10, 50)
c


# #### 6.  Reverse the numpy array ranging from 0 to 50. 
# 
# #### Ստեղծեք 0-ից 50 հաջորդական թվերով numpy array և տպեք այն շրջած ձևով:

# In[46]:


a = np.arange(51)
np.flip(a)


# #### 7.  Create a 3x3 matrix with values ranging from 0 to 8 
# 
# #### Ստեղծեք 0-ից 8 հաջորդական թվերով 3x3 numpy array

# In[49]:


a = np.arange(9)
a.reshape(3,3)


# #### 8. Find indices of non-zero elements from \[1,2,0,0,4,0\]
# 
# #### Տրված է \[1,2,0,0,4,0\] numpy array-ը, գտեք ոչ-զրոյական արժեքներով տարրերի կոորդինատները:

# In[54]:


b = np.array([1,2,0,0,4,0])
result = np.where(b != 0)
result


# #### 9. Create a 3x3x3 array with random integers from 1 to 20
# 
# #### Ստեղծեք 1-ից 20 պատահական թվերով լցված (3x3x3) չափանի numpy array:

# In[72]:


a = np.random.randint(1,21,27).reshape(3,3,3)
a


# #### 10. Create a 10x10 array with random values and find the minimum and maximum values 
# 
# #### Ստեղծեք պատահական թվերով լցված (10x10) չափանի numpy array ու տպեք դրա փոքրագույն ու մեծագույն արժեքները:

# In[85]:


a = np.random.rand(100).reshape(10,10)
print(np.amax(a))
print(np.amin(a))


# #### 11. Create a random vector of size 30 and find the mean value 
# 
# #### Ստեղծեք 30 չափանի պատահական թվերով լցված numpy array ու տպեք դրա միջին արժեքը:

# In[88]:


a = np.random.rand(30)
print(np.average(a))


# #### 12. Given a 1D array ranging from 0 to 10, print all the elements which are between 3 and 8. 
# 
# #### Ստեղծեք 0-ից 10 հաջորդական թվերով numpy array: Տպեք բոլոր արժեքները, որոնք 3-ից 8 միջակայքում են:

# In[94]:


a = np.arange(0,11, 1)
a[3:9]


# #### 13. Given a 1D array of 20 random integers from 0 to 10, multiply the values that are less than 5 by 2 and print the resulting array.
# 
# #### Ստեղծեք 1-ից 10 պատահական ամբողջ թվերով լցված 20 չափանի numpy array: Բազմապատկեք 5-ից փոքր արժեք ունեցող տարերրը 2-ով ու տպեք արդյունքում ստացված array-ը:

# In[109]:


a = np.random.randint(1,10,20)
b = ([2])
c = a[a < 5] * b
c


# #### 14. Given the 1D array [1, 5, 6, 2, -2, 23, 45], find the indices of the array elements that are divisible by 2.
# 
# #### Տրված է [1, 5, 6, 2, -2, 23, 45] numpy array-ը, գտեք 2-ի բաժանվող տարրերի կոորդինատները:

# In[114]:


a = np.array([1,5,6,2,-2,23,45])
result = np.where(a % 2 == 0)
result


# #### 15. Given a 1D array ranging from 0 to 20, print all the elements which are divisible by 3. 
# 
# #### Ստեղծեք 1-ից 20 հաջորդական թվերով լցված numpy array, տպեք բոլոր 3-ի բաժանվող տարրերի արժեքները:

# In[118]:


a = np.arange(0,21,1)
result = a[np.where(a % 3 == 0)]
result


# #### 16. Create a 5x5 numpy array with each row values ranging from 0 to 4 
# 
# #### Ստեղծեք 5x5 numpy array, որի ամեն տող իրենից ներկայացնում է 0-ից 4 հաջորդական թվեր:

# In[124]:


a = np.arange(0,5,1)
x = np.tile(a, (5,1))
print(x)


# #### 17. Create a 3x5 numpy array filled with random numbers from 1 to 10.
# 
# #### 17. Ստեղծեք 1-ից 10 պատահական թվերով լցված (3, 5) չափերով numpy array։

# In[127]:


a = np.random.randint(1,11,15).reshape(3,5)
a


# #### 18. Create a numpy array of size 10 filled with 0s and replace its 5th value with a 3.
# 
# #### 18. Ստեղծեք 10 չափի 0-ներով լցված numpy array ու փոխարինեք դրա 5-րդ արժեքը 3 թվով։

# In[131]:


a = np.zeros(10)
a[5] = 3
a


# #### 19. Create a numpy array filled with numbers from 3 to 15 i.e. ([3, 4 … 13, 14])
# 
# #### 19. Ստեղծեք 3-ից 15 թվերից բաղկացած numpy array ([3, 4 … 13, 14])

# In[136]:


a = np.arange(3,15)
a


# #### 20. Write a function which gets a numpy array as an input and divides all of the array values by 2 over and over again, until the mean of the array numbers is <=5. Then, once the mean of the array numbers is <=5, the funtion returns the modified numpy array. 
# 
# #### 20. Գրեք ֆունկցիա, որը ստանում է numpy array ու բաժանում է դրա բոլոր արժեքները 2-ի այնքան ժամանակ մինչև որ դրանց միջին արժեքը լինի <=5։ Այնուհետև, հենց միջին արժեքը դառնում է <=5, ֆունկցիան վերադարձնում է փոփոխված numpy array-ը։

# In[157]:


def division(a,b,c):
    while np.average(c) > 5:
        a = c
        c = a/b
    else: 
        print (c)
        
a = np.arange(3,15)
b = ([2])
c = a/b


x = division(a,b,c)
    


# #### 21. Write a function which gets a 5x4 numpy array filled with random numbers from 1 to 10 as an inputand returns 4 different numpy arrays which are the columns of the original numpy array. Write another similar function which returns 5 different numpy arrays which are rows of the original numpy array. 
# 
# #### 21. Գրեք ֆունկցիա, որը ստանում է 1-ից 10 պատահական թվերով լցված 5x4 numpy array ու վերադարձնում է 4 տարբեր numpy array-ներ, որոնք սկզբնական numpy array-ի սյուներն են։ Գրեք նմանատիպ ֆունկցիա, որը վերադարձնում է 5 տարբեր numpy array-ներ, որոնք սկզբնական numpy array-ի տողերն են։

# In[174]:


def columns(a):
    for i in range(np.shape(a)[1]):
        print (a[:, i])
a = np.random.randint(1,11,20).reshape(5,4)
x = columns(a)

print("\n")

def rows(a):
    for i in range(np.shape(a)[0]):
        print (a[i])
a = np.random.randint(1,11,20).reshape(5,4)
y = rows(a)

