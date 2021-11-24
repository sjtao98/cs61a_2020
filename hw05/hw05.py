#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1: Vending Machine
"""
Create a class called VendingMachine that represents a vending machine for some product. 
A VendingMachine object returns strings describing its interactions.

Fill in the VendingMachine class, adding attributes and methods as appropriate, 
such that its behavior matches the following doctests:
"""
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, category, price):
        self.type      = category
        self.price     = price
        self.inventory = 0
        self.funds     = 0

    def vend(self):
        if self.inventory == 0:
            return f'Inventory empty. Restocking required.'
        else:
            if self.funds < self.price:
                lack = self.price - self.funds
                return f'You must add ${lack} more funds.'
            else:
                self.inventory -= 1
                self.funds -= self.price
                if self.funds > 0:
                    message = f'Here is your {self.type} and ${self.funds} change.'
                    self.funds = 0
                    return message 
                elif self.funds == 0:
                    return f'Here is your {self.type}'
    
    def add_funds(self, cash):
        if self.inventory == 0:
            return f'Inventory empty. Restocking required. Here is your ${cash}.'
        else:
            self.funds += cash
            return f'Current balance: ${self.funds}'
    
    def restock(self, number):
        self.inventory += number
        return f'Current soda stock: {self.inventory}'
        
    
    


# In[2]:


v = VendingMachine('candy', 10)


# In[3]:


v.vend()


# In[4]:


v.add_funds(15)


# In[5]:


v.restock(2)


# In[6]:


v.vend()


# In[7]:


v.add_funds(7)


# In[8]:


v.vend()


# In[9]:


v.add_funds(5)


# In[10]:


v.vend()


# In[11]:


v.add_funds(10)


# In[12]:


v.vend()


# In[13]:


v.add_funds(15)


# In[14]:


w = VendingMachine('soda', 2)


# In[15]:


w.restock(3)


# In[16]:


w.restock(3)


# In[17]:


w.add_funds(2)


# In[18]:


w.vend()


# In[19]:


# Q2: Mint
"""
Complete the Mint and Coin classes so that the coins created by a mint have the correct year and worth.
Each Mint instance has a year stamp. 
The update method sets the year stamp to the current_year class attribute of the Mint class.
The create method takes a subclass of Coin and returns an instance of that class stamped with 
the mint's year (which may be different from Mint.current_year if it has not been updated.)
A Coin's worth method returns the cents value of the coin plus one extra cent for each year
of age beyond 50. A coin's age can be determined by subtracting the coin's year from the 
current_year class attribute of the Mint class.
"""
class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Mint.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + max(0, Mint.current_year -self.year - 50)

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


# In[20]:


mint = Mint()


# In[21]:


mint.year


# In[22]:


dime = mint.create(Dime)


# In[23]:


dime.year


# In[24]:


Mint.current_year = 2100


# In[25]:


nickel = mint.create(Nickel)


# In[26]:


nickel.year


# In[27]:


nickel.worth()


# In[28]:


mint.update()


# In[29]:


Mint.current_year = 2175


# In[30]:


mint.create(Dime).worth()


# In[31]:


Mint().create(Dime).worth()


# In[32]:


dime.worth()


# In[33]:


Dime.cents = 20


# In[34]:


dime.worth()


# In[35]:


# Q3: Store Digits
"""
Write a function store_digits that takes in an integer n and returns a linked list 
where each element of the list is a digit of n.
Note: do not use any string manipulation functions like str and reversed
"""
class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s)
    <6 7>
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    ans = Link.empty
    while(n > 0):
        ans = Link(n % 10, ans)
        n = n // 10
    return ans


# In[36]:


store_digits(2345)


# In[37]:


store_digits(876)


# In[ ]:




