#!/usr/bin/env python
# coding: utf-8

# In[1]:


def min_depth(t):
    """A simple function to return the distance between t's root and its closest leaf"""
    if is_leaf(t):
        return 0
    h = float('inf')
    for b in branches(t):
        # Still works fine!
        h = min(h, 1 + min_depth(b))
    return h

#Q1 weights
def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]


# In[2]:


def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ['planet', size]

def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'total_weight', ['Index'])
    True
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


# In[3]:


#Q2: Balanced
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return True
    else:
        left_end, right_end = end(left(m)), end(right(m))
        left_torque = length(left(m))*total_weight(left_end)
        right_torque = length(right(m))*total_weight(right_end)
        return left_torque == right_torque and balanced(left_end) and balanced(right_end)


# In[4]:


#Q3: Totals
def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'totals_tree', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return tree(size(m))
    else:
        branches = [totals_tree(end(b(m))) for b in [left, right]]
        return tree(m, sum([label(b) for b in branches]), branches)


# In[18]:


#Q4: Replace Leaf
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent = 0):
    print(' '*indent, label(t))
    for b in branches(t):
        print_tree(b, indent + 1)
"----------------------beyond functions are from course video---------------------"        
def replace_leaf(t, find_value, replace_value):
    """Returns a new tree where every leaf value equal to find_value has
    been replaced with replace_value.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) and label(t) == find_value:
        return tree(replace_value)
    else:
        bs = [replace_leaf(b, find_value, replace_value) for b in branches(t)]
        return tree(label(t), bs)


# In[22]:


#Q5: Preorder
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if branches == []:
        return [label(t)]
    
    entry_list = []
    for child in branches(t):
        entry_list += preorder(child)
    return [label(t)] + entry_list


# In[23]:


numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
preorder(numbers)


# In[24]:


#Q6: Has Path
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if label(t) != word[0]:
        return False
    elif len(word) == 1:
        return True
    
    for b in branches(t):
        if has_path(b, word[1:]):
            return True
    
    return False


# In[25]:


#Q7: Interval Abstraction
def interval(a, b):
    """Construct an interval from a to b."""
    assert a <= b
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]


# In[26]:


def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    #p1 = x[0] * y[0]
    #p2 = x[0] * y[1]
    #p3 = x[1] * y[0]
    #p4 = x[1] * y[1]
    p1 = lower_bound(x) * lower_bound(y)
    p2 = upper_bound(x) * lower_bound(y)
    p3 = lower_bound(x) * upper_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


# In[32]:


#Q8: Sub Interval
def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    "*** YOUR CODE HERE ***"
    interval_y = [-upper_bound(y), upper_bound(y)]
    return add_interval(x, interval_y)

def add_interval(x, y):
    p1 = lower_bound(x) + lower_bound(y)
    p2 = upper_bound(x) + lower_bound(y)
    p3 = lower_bound(x) + upper_bound(y)
    p4 = upper_bound(x) + upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]


# In[33]:


sub_interval([1,2], [4,5])


# In[34]:


#Q9: Div Interval
def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    "*** YOUR CODE HERE ***"
    assert not (upper_bound(y) >= 0 >= lower_bound(y))
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)


# In[35]:


#Q10: Par Diff
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    #r1 = interval(1, 1) # Replace this line!
    #r2 = interval(1, 1) # Replace this line!
    r1 = interval(1, 2)
    r2 = interval(1, 3)
    return r1, r2


# In[39]:


r1, r2 = check_par()
par1(r1, r2) == par2(r1, r2)


# In[ ]:


#Q11: Multiple References
def multiple_references_explanation():
    return """The multiple reference problem..."""


# In[44]:


#Q12: Quadratic
#f(t) = a*t*t + b*t + c
def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    ext_pt = -b/(2*a)
    if upper_bound(x) >= ext_pt >= lower_bound(x):
        if a > 0:
            lower = (4*a*c-b**2)/(4*a)
            upper = max(a*lower_bound(x)**2 + b*lower_bound(x) + c, a*upper_bound(x)**2 + b*upper_bound(x) + c)
        elif a < 0:
            upper = (4*a*c-b**2)/(4*a)
            lower = min(a*lower_bound(x)**2 + b*lower_bound(x) + c, a*upper_bound(x)**2 + b*upper_bound(x) + c)
    else:
        lower = min(a*lower_bound(x)**2 + b*lower_bound(x) + c, a*upper_bound(x)**2 + b*upper_bound(x) + c)
        upper = max(a*lower_bound(x)**2 + b*lower_bound(x) + c, a*upper_bound(x)**2 + b*upper_bound(x) + c)
            

    return interval(lower, upper)


# In[45]:


quadratic(interval(0, 2), -2, 3, -1)


# In[ ]:




