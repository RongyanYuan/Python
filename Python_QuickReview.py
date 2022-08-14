# Running on Juypter notebook is strongly recommended.
# * Data types
#     * Numbers
#     * Strings
#     * Printing
#     * Lists
#     * Dictionaries
#     * Booleans
#     * Tuples 
#     * Sets
# * Comparison Operators
# * if, elif, else Statements
# * for Loops
# * while Loops
# * range()
# * list comprehension
# * functions
# * lambda expressions
# * map and filter
# * methods
# ____

# ## Data types
# 
# ### Numbers

# In[6]:


1 + 1


# In[7]:


1 * 3


# In[8]:


1 / 2


# In[9]:


2 ** 4


# In[10]:


4 % 2


# In[11]:


5 % 2


# In[12]:


(2 + 3) * (5 + 5)


# ### Variable Assignment

# In[13]:


# Can not start with number or special characters
name_of_var = 2


# In[14]:


x = 2
y = 3


# In[15]:


z = x + y


# In[16]:


z


# ### Strings

# In[17]:


'single quotes'


# In[18]:


"double quotes"


# In[19]:


" wrap lot's of other quotes"


# ### Printing

# In[20]:


x = 'hello'


# In[21]:


x


# In[22]:


print(x)


# In[2]:


num = 12
name = 'Sam'


# In[3]:


print('My number is: {one}, and my name is: {two}, and more {one}'.format(one=num,two=name))


# In[25]:


print('My number is: {}, and my name is: {}'.format(num,name))


# ### Lists

# In[26]:


[1,2,3]


# In[27]:


['hi',1,[1,2]]


# In[28]:


my_list = ['a','b','c']


# In[29]:


my_list.append('d')


# In[30]:


my_list


# In[31]:


my_list[0]


# In[32]:


my_list[1]


# In[33]:


my_list[1:]


# In[34]:


my_list[:1]


# In[35]:


my_list[0] = 'NEW'


# In[98]:


my_list


# In[99]:


nest = [1,2,3,[4,5,['target']]]


# In[100]:


nest[3]


# In[101]:


nest[3][2]


# In[102]:


nest[3][2][0]


# ### Dictionaries

# In[4]:


d = {'key1':'item1','key2':'item2'}


# In[5]:


d


# In[9]:


d['key1']


# In[11]:


d['key 3'] = 'item3'


# In[13]:


d['key 3']


# Nested dictionaries allowed

# In[15]:


d2 = {'k1':d, 'k2': d}


# In[16]:


print(d2) # dictionary does not store any order but just keys and elements.


# ### Booleans

# In[40]:


True


# In[41]:


False


# ### Tuples 

# In[18]:


t = (1,2,3) 


# In[19]:


t[0]


# Tuples are inmutable.

# You cannot change elemetns in tuples, here is an example.

# In[44]:


t[0] = 'NEW'


# ### Sets

# In[20]:


{1,2,3}


# Set function gives you a set of unique elements

# In[21]:


{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}


# Functions under SETS:

# In[22]:


s = {1,2,3}


# In[25]:


s.add(5)
print(s)


# In[26]:


s.remove(5) #Notre here: remove/add function mutates the set s.
print(s)


# In[ ]:





# ## Comparison Operators

# In[47]:


1 > 2


# In[48]:


1 < 2


# In[49]:


1 >= 1


# In[50]:


1 <= 4


# In[51]:


1 == 1 # '=' is an assignment operator


# In[52]:


'hi' == 'bye'


# ## Logic Operators

# In[53]:


(1 > 2) and (2 < 3)


# In[54]:


(1 > 2) or (2 < 3)


# In[55]:


(1 == 2) or (2 == 3) or (4 == 4)


# ## if,elif, else Statements

# In[56]:


if 1 < 2:
    print('Yep!')


# In[57]:


if 1 < 2:
    print('yep!')


# In[58]:


if 1 < 2:
    print('first')
else:
    print('last')


# In[59]:


if 1 > 2:
    print('first')
else:
    print('last')


# In[27]:


if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')


# Furthermore:

# In[32]:


print((3>2) + 1); # 3>2 gives us true, and true + 1 gives us 2.


# In[36]:


print((3>4) + 1);


# Follwoing example shows 1 and 0 are the embeded val for bool.

# In[35]:


if 0:
    print("bool is false");
if 1:
    print('bool is true');


# ## for Loops

# In[61]:


seq = [1,2,3,4,5]


# In[62]:


for item in seq: # for loop allows you to iterate in a sequence;
    print(item)


# In[63]:


for item in seq:
    print('Yep')


# In[64]:


for jelly in seq:
    print(jelly+jelly)


# ## while Loops

# In[65]:


i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


# ## range()

# In[66]:


range(5)


# In[67]:


for i in range(5):
    print(i)


# In[37]:


list(range(5)) #make it a squence;


# In[39]:


list(range(0,10,2)) #making a list from 0 to 10 with 2 stepss


# ## list comprehension

# In[69]:


x = [1,2,3,4]


# In[70]:


out = []
for item in x:
    out.append(item**2)
print(out)


# In[71]:


[item**2 for item in x] # list comprehension


# ## functions

# In[72]:


def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)


# In[73]:


my_func # reports back the object


# In[74]:


my_func() # calls the function


# In[75]:


my_func('new param')


# In[76]:


my_func(param1='new param')


# In[77]:


def square(x):
    return x**2


# In[78]:


out = square(2)


# In[79]:


print(out)


# ## lambda expressions

# In[80]:


def times2(var):
    return var*2


# In[81]:


times2(2)


# In[40]:


lambda var: var*2


# In[41]:


t = lambda var : var*2
print(t(2));


# ## map and filter

# In[83]:


seq = [1,2,3,4,5]


# In[84]:


map(times2,seq) # maps a function to each elemetn int the list 


# In[85]:


list(map(times2,seq))


# In[86]:


list(map(lambda var: var*2,seq)) # lambda expression saves code writing


# In[87]:


filter(lambda item: item%2 == 0,seq)


# In[88]:


list(filter(lambda item: item%2 == 0,seq)) # if fucntion iterating on each element.


# ## methods

# In[111]:


st = 'hello my name is Sam'


# In[112]:


st.lower() # you can type st. and see all available methods


# In[113]:


st.upper()


# In[103]:


st.split() # splits the string on the white space if there's no input.


# In[104]:


tweet = 'Go Sports! #Sports'


# In[106]:


tweet.split('#') 


# In[107]:


tweet.split('#')[1]


# In[92]:


d


# In[93]:


d.keys()


# In[94]:


d.items()


# In[43]:


lst = [1,2,3]


# In[44]:


lst.pop() #randomly pops out last item


# In[46]:


lst


# In[47]:


lst.pop(0)


# In[48]:


lst


# In[ ]:





# In[109]:


'x' in [1,2,3]


# In[49]:


'x' in ['x','y','z']


# Tuple unpacking:

# In[53]:


x = [(1,2),(3,4), (5,6)]
for a,b in x:
    print(a)


# In[55]:


for a,b in x :
    print(b);


# # Great Job!
