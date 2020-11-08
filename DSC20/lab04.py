
def square(x):
    return x * x

def negate(x):
    return -x

def identity(x):
    return x

def multy(x, mult):
    return mult * x

def sum(x,y):
    return x + y

def step_increment(x, step):
    return x + step

def triple(x):
    multiplier  = 3
    return multiplier * x



# Question 1:
def my_map(func, lst, param = None):
    """Use yield to create a generator that will iterator over the
    results after applying the given function to each item in 
    the given list

    >>> gen = my_map(square, [1,2,3,4,5])
    >>> print(next(gen))
    1
    >>> print(next(gen))
    4
    >>> list(gen)
    [9, 16, 25]
    >>> gen = my_map(step_increment, [1,2,3], 2)
    >>> tuple(gen)
    (3, 4, 5)
    >>> gen = my_map(multy, [1,2,3], 3)
    >>> for i in gen:
    ...     print(i)
    ... 
    3
    6
    9
    >>> gen = my_map(identity, [1,2,3])
    >>> next(gen)
    1
    >>> next(gen)
    2
    >>> next(gen)
    3
    >>> gen = my_map(negate, [1,2,3])
    >>> list(gen)
    [-1, -2, -3]
    >>> gen = my_map(square, [])
    >>> print(next(gen))
    Traceback (most recent call last):
        ...
    StopIteration
    """
    if param==None:
        for i in lst:
            yield func(i)
    else:
        for i in lst:
            yield func(i,param)    



# Question 2:
def my_filter(func, lst):
    """Creates a generator that iterates over elements 
    for which a function returns True
    >>> gen = my_filter(lambda x: x < 0, [1, -2, 3, -4])
    >>> list(gen)
    [-2, -4]
    >>> gen = my_filter(lambda x: x%2 == 0, [1, -2, 3, -4, 6])
    >>> tuple(gen)
    (-2, -4, 6)
    >>> gen = my_filter(lambda x: (x == "".join(reversed(x))), \
    ["anna", "likes", "her", "detartrated", "tote", "given", "by", "eve" ])
    >>> list(gen)
    ['anna', 'detartrated', 'eve']
    """ 
    end_lst=[]
    for i in lst:
        output=func(i)
        if output==True:
            end_lst.append(i)
    return end_lst
        



# Question 3
def map_then_filter(func_map, func_filter, lst):
    """
    >>> map_then_filter(square, (lambda x: x>10), [1,2,3,4])
    [16]
    >>> map_then_filter(square, (lambda x: x < 0), [1,2,3,4])
    []
    >>> map_then_filter(negate, (lambda x: x > 0), [1, -2, -3, 4])
    [2, 3]
    >>> map_then_filter(triple, (lambda x: x%2==0), [1,2,3,4])
    [6, 12]
    >>> map_then_filter(lambda x: x + "added", \
    (lambda x: len(x)%2 == 0), ["one", "two", "four"])
    ['oneadded', 'twoadded']
    """
    return list(filter(func_filter,list(map(func_map,lst))))
    
    



# Question 4
def new_matrix(func, matrix):
    """Apply func to every element in 2D-array mat.

    >>> m0 = [[1,2], [3, 4]]
    >>> m1 = [[10, 0, 0], [5, 2, 2], [0, 3, 4]]
    >>> m2 = [[1, 1], [2, 2], [6, 6]]

    >>> new_matrix(triple, m0)
    [[3, 6], [9, 12]]
    >>> new_matrix(square, m0)
    [[1, 4], [9, 16]]
    >>> new_matrix(negate, m2)
    [[-1, -1], [-2, -2], [-6, -6]]
    >>> new_matrix(square, m1)
    [[100, 0, 0], [25, 4, 4], [0, 9, 16]]
    """
    return [list(map(func,lst)) for lst in matrix]



# Question 5
def apply_twice(func, param):
    """Apply func to the result of applying func to param"
    >>> apply_twice(square, 3)
    81
    >>> apply_twice(square, 5)
    625
    >>> apply_twice(negate, -1)
    -1
    >>> apply_twice(identity, 10)
    10
    >>> apply_twice(triple, 5)
    45
    """
    return list(map(func,list(map(func,[param]))))[0]
    


# Question 6
def apply_n_times(func, param, n, optional=None):
    """Apply function func to param n times.
    >>> apply_n_times(step_increment, 2, 1, 10)
    12
    >>> apply_n_times(step_increment, 2, 3, 5)
    17
    >>> apply_n_times(step_increment, 3, 4, 7)
    31
    >>> apply_n_times(square, 2, 3)
    256
    >>> apply_n_times(multy, 3, 4, 3)
    243
    >>> apply_n_times(negate, -10, 10)
    -10
    >>> apply_n_times(square, 5, 3)
    390625
    >>> apply_n_times(multy, 5, 5, 5)
    15625
    """
    output=param
    if optional==None:
        for i in range(n):
            output=func(output)
    else:
         for i in range(n):
             output=func(output,optional)
    return output



# Question 7
def pick_me(f, g, num):
    """Returns the function h where:
    h(x) = f(x) if x > num,
           g(x) otherwise

    >>> abs_value = pick_me(negate, identity, 0)
    >>> abs_value(10)
    -10
    >>> abs_value(-10)
    -10
    >>> trip_sq = pick_me(triple, square, 3)
    >>> trip_sq(5)
    15
    >>> trip_sq(10)
    30
    >>> id_square = pick_me(identity, square, 9)
    >>> id_square(11)
    11
    >>> id_square(8)
    64
    """
    def h(param):
        if param>num:
            ans=f(param)
        else:
            ans=g(param)
        return ans
    return h
    
