#!/usr/bin/env python
# coding: utf-8

# In[217]:


import copy

l=[[0,4,0,2,0,1,0,6,0],
   [0,0,0,0,0,0,0,0,0],
   [9,0,5,0,0,0,3,0,7],
   [0,0,0,0,0,0,0,0,0],
   [5,0,7,0,8,0,1,0,4],
   [0,1,0,0,0,0,0,9,0],
   [0,0,1,0,0,0,6,0,0],
   [0,0,0,7,0,5,0,0,0],
   [6,0,8,9,0,4,5,0,3]]



l=[[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,3,0,8,5],
   [0,0,1,0,2,0,0,0,0],
   [0,0,0,5,0,7,0,0,0],
   [0,0,4,0,0,0,1,0,0],
   [0,9,0,0,0,0,0,0,0],
   [5,0,0,0,0,0,0,7,3],
   [0,0,2,0,1,0,0,0,0],
   [0,0,0,0,4,0,0,0,9]]

l=[[1,0,0,0,7,0,0,3,0],
   [8,3,0,6,0,0,0,0,0],
   [0,0,2,9,0,0,6,0,8],
   [6,0,0,0,0,4,9,0,7],
   [0,9,0,0,0,0,0,5,0],
   [3,0,7,5,0,0,0,0,4],
   [2,0,3,0,0,9,1,0,0],
   [0,0,0,0,0,2,0,4,3],
   [0,4,0,0,8,0,0,0,9]]

l=[[0,3,0,0],
   [0,0,0,2],
   [1,0,0,0],
   [0,0,0,0]]

l=[[5,3,0,0,7,0,0,0,0],
   [6,0,0,1,9,5,0,0,0],
   [0,9,8,0,0,0,0,6,0],
   [8,0,0,0,6,0,0,0,3],
   [4,0,0,8,0,3,0,0,1],
   [7,0,0,0,2,0,0,0,6],
   [0,6,0,0,0,0,2,8,0],
   [0,0,0,4,1,9,0,0,5],
   [0,0,0,0,8,0,0,7,9]]
n=len(l)


# In[218]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://www.sudoku.ws/3-20.png")


# In[219]:


def print_sudoku(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if j%int(len(l)**0.5)==0:
                print("  ",end="")
            print(l[i][j],"  ",end="")
        if (i+1)%int(len(l)**0.5)==0:
            print("\n")
        print("\n")


# In[220]:


def place_probable(x,y,l):
    if l[x][y]!=0:
        return set([])
    p=list(range(1,n+1))
    p_r=[]
    for i in range(n):
        p_r.append(l[x][i])
        p_r.append(l[i][y])
    for i in range(0,n,int(n**0.5)):
        if i<=x and x<i+int(n**0.5):
            sub_x=i
        if i<=y and y<i+int(n**0.5):
            sub_y=i
    for i in range(sub_x,sub_x+int(n**0.5)):
        for j in range(sub_y,sub_y+int(n**0.5)):
            p_r.append(l[i][j])
    p_r=[i for i in range(1,n+1) if i not in p_r]
    return set(p_r)


# In[221]:


def sudoku_checker(l):
    n=len(l)
    for x in range(n):
        for y in range(n):
            if l[x][y]==0:
                return False
    return True


# In[222]:


def place_filler(l,give_l=True):
    n=len(l)
    for x in range(n):
        for y in range(n):
            if y%int(len(l)**0.5)==0:
                print("  ",end="")
            
            temp=place_probable(x,y,l)
            print(temp,end=" ")
            if len(temp)==1:
                l[x][y]=temp.pop()
                continue
            
            temp=place_probable(x,y,l)
            for j in range(n):
                if y!=j:
                    temp=temp-place_probable(x,j,l)
            if len(temp)==1:
                l[x][y]=temp.pop()
                continue
            
                
            temp=place_probable(x,y,l)
            for i in range(n):
                if x!=i:
                    temp=temp-place_probable(i,y,l)
            if len(temp)==1:
                l[x][y]=temp.pop()
                continue
            
            temp=place_probable(x,y,l)
            for i in range(0,n,int(n**0.5)):
                if i<=x and x<i+int(n**0.5):
                    sub_x=i
                if i<=y and y<i+int(n**0.5):
                    sub_y=i
            for i in range(sub_x,sub_x+int(n**0.5)):
                for j in range(sub_y,sub_y+int(n**0.5)):
                    if x!=i or y!=j:
                        temp=temp-place_probable(i,j,l)
            if len(temp)==1:
                l[x][y]=temp.pop()
                continue
        if (x+1)%int(len(l)**0.5)==0:
            print("\n")        
        print("\n")
    if(give_l):
        return l


# In[ ]:





# In[223]:


print_sudoku(l)


# In[224]:


while(True):
    temp_l=place_filler(copy.deepcopy(l))
    if(temp_l==l):
        print("can't go further")
        break
    else:
        l=temp_l
    print("\n\n")
print(sudoku_checker(l))


# In[225]:


print_sudoku(l)


# In[ ]:





# In[ ]:




