#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Q1: Make Bank
def make_withdraw(balance):
    """Return a withdraw function with BALANCE as its starting balance.
    >>> withdraw = make_withdraw(1000)
    >>> withdraw(100)
    900
    >>> withdraw(100)
    800
    >>> withdraw(900)
    'Insufficient funds'
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

"""
Write a new function make_bank, which should create a bank account with value balance and 
should also return another function. This new function should be able to withdraw and deposit money. 
The second function will take in two arguments: message and amount. When the message passed in is 
'deposit', the bank will deposit amount into the account. When the message passed in is 'withdraw', 
the bank will attempt to withdraw amount from the account. If the account does not have enough money 
for a withdrawal, the string 'Insufficient funds' will be returned. 
If the message passed in is neither of the two commands, the function should return 'Invalid message' 
Examples are shown in the doctests.
"""
def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """      
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'deposit':
            balance = balance + amount
            return balance
        elif message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        else:
            return 'Invalid message'
    return bank


# In[17]:


bank = make_bank(100)
print(bank('withdraw', 40) == 60)
print(bank('hello', 500) == 'Invalid message')
print(bank('deposit', 20) == 80)
print(bank('withdraw', 90) == 'Insufficient funds')
print(bank('deposit', 100) == 180)
print(bank('goodbye', 0) == 'Invalid message')
print(bank('withdraw', 60) == 120)


# In[130]:


#Q2: Password Protected Account
"""
Write a version of the make_withdraw function shown in the previous question that returns 
password-protected withdraw functions. That is, make_withdraw should take a password argument 
(a string) in addition to an initial balance. 
The returned function should take two arguments: an amount to withdraw and a password.
A password-protected withdraw function should only process withdrawals that include 
a password that matches the original. Upon receiving an incorrect password, the function should:
Store that incorrect password in a list, and Return the string 'Incorrect password'.
If a withdraw function has been called three times with incorrect passwords <p1>, <p2>, and <p3>, 
then it is frozen. All subsequent calls to the function should return:
"Frozen account. Attempts: [<p1>, <p2>, <p3>]"
"""

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    orig_password = 'hax0r'
    failed_password = list()
    failed = 0
    def bank(amount, password):
        nonlocal balance, failed, failed_password
        
        if failed == 3:
            return "Frozen account. Attempts: " + str(failed_password)
        
        if password == orig_password:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
        else:
            failed += 1
            failed_password.append(password)
            return 'Incorrect password'
        
    return bank
    


# In[131]:


w = make_withdraw(100, 'hax0r')
w(25, 'hax0r')


# In[132]:


w(90, 'hax0r')


# In[133]:


w(25, 'hwat')


# In[134]:


w(25, 'hax0r')


# In[135]:


w(75, 'a')


# In[136]:


w(10, 'hax0r')


# In[137]:


w(20, 'n00b')


# In[138]:


w(10, 'hax0r')


# In[139]:


w(10, 'l33t')


# In[144]:


#Q3: Repeated
"""
Implement a function (not a generator function) that returns the first value in the iterator t that 
appears k times in a row. As described in lecture, iterators can provide values using either the 
next(t) function or with a for-loop. Do not worry about cases where the function reaches the end 
of the iterator without finding a suitable value, all lists passed in for the tests will have a value 
that should be returned. If you are receiving an error where the iterator has completed then the 
program is not identifying the correct value. Iterate through the items such that if the same 
iterator is passed into repeated twice, it continues in the second call at the point it left off 
in the first. An example of this behavior is shown in the doctests
"""
def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    si = next(t)
    r  = 1
    for v in t:
        if v == si:
            r += 1
            if r == k:
                return v
        else:
            r = 1
        si = v
    return "Not FOUND" 
        
    


# In[145]:


s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
repeated(s, 2)


# In[146]:


s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
repeated(s2, 3)


# In[147]:


s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
repeated(s, 3)


# In[150]:


repeated(s, 3)


# In[151]:


s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
repeated(s2, 3)


# In[163]:


#Q4: Generate Permutations
"""
Given a sequence of unique elements, a permutation of the sequence is a list containing the elements 
of the sequence in some arbitrary order. For example, [2, 1, 3], [1, 3, 2], and [3, 2, 1] are some 
of the permutations of the sequence [1, 2, 3].

Implement permutations, a generator function that takes in a sequence seq and returns a generator 
that yields all permutations of seq.

Permutations may be yielded in any order. 
Note that the doctests test whether you are yielding all possible permutations, 
but not in any particular order. The built-in sorted function takes in an iterable object 
and returns a list containing the elements of the iterable in non-decreasing order.
"""
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if not seq:
        yield []
    else:
        for p in permutations(seq[1:]):
            for i in range(len(seq)):
                yield p[:i] + [seq[0]] + p[i:]


# In[165]:


sorted(permutations([1, 2, 3]))


# In[ ]:


# Q5: Joint Account
"""
Suppose that our banking system requires the ability to make joint accounts. 
Define a function make_joint that takes three arguments.

A password-protected withdraw function,
The password with which that withdraw function was defined, and
A new password that can also access the original account.

If the password is incorrect or cannot be verified because the underlying account is locked, 
the make_joint should propagate the error. Otherwise, it returns a withdraw function that provides
additional access to the original account using either the new or old password. 
Both functions draw from the same balance. Incorrect passwords provided to either function will be 
stored and cause the functions to be locked after three wrong attempts.
"""


# In[166]:


# Q6: Remainder Generator
"""
Like functions, generators can also be higher-order. 
For this problem, we will be writing remainders_generator, which yields a series of generator objects.
remainders_generator takes in an integer m, and yields m different generators. 
The first generator is a generator of multiples of m, i.e. numbers where the remainder is 0. 
The second is a generator of natural numbers with remainder 1 when divided by m. 
The last generator yields natural numbers with remainder m - 1 when divided by m.
"""
def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def gem(i):
        for n in naturals():
            if n % m == i:
                yield n
    for i in range(m):
        yield gem(i)


# In[169]:


remainders_four = remainders_generator(4)
for i in range(4):
    print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    gen = next(remainders_four)
    for j in range(3):
        print(next(gen))


# In[ ]:




