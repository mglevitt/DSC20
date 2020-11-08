"""
DSC 20 HW 04
NAME: Maxwell Levitt
PID: A15788481
"""
import math
from math import factorial
from math import floor

## Question 1 ##
def prime_number_generator(number_of_primes):
    """
    Generator for creating the first 'number_of_primes' prime numbers
    using the prime number formula based on Wilson's theorem

    Restrictions:
    You should use a generator in this question.

    Parameters:
    number_of_primes (int): Number of primes to be generated

    Returns:
    The required generator of the question.

    >>> prime_gen = prime_number_generator(2)
    >>> next(prime_gen)
    2
    >>> list(prime_number_generator(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_gen = prime_number_generator(20)
    >>> list(prime_gen)[10:20]
    [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> prime_gen=prime_number_generator(100)
    >>> list(prime_gen)[85:95]
    [443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
    >>> prime_gen=prime_number_generator(9)
    >>> next(prime_gen)
    2
    >>> list(prime_gen)
    [3, 5, 7, 11, 13, 17, 19, 23]
    """
    count=0
    n=1
    test=0
    addition=2    
    while count<number_of_primes:
        test=floor(math.factorial(n)%(n+1)/n)
        if test!=0:
            yield test*(n-1)+2
            count+=1
        n+=1 
    
## Question 2.1 ##
def exp_gen(n, e):
    """A generator that yields the following exponentials
    (given n, e as inputs):
    n**e, (n*e)**e, (n*e*e)**e, (n*e*e*e)**e, ... (and so on)
    >>> gen = exp_gen(2,2)
    >>> next(gen)
    4
    >>> next(gen)
    16
    >>> next(gen)
    64
    >>> next(gen)
    256

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gen = exp_gen(9,9)
    >>> next(gen)
    387420489
    >>> next(gen)
    150094635296999121
    >>> next(gen)
    58149737003040059690390169
    >>> gen = exp_gen(1,1)
    >>> next(gen)
    1
    >>> next(gen)
    1
    >>> next(gen)
    1
    >>> next(gen)
    1
    """
    
    count=0
    while True:
        yield (n*(e**count))**e
        count+=1
        
## Question 2.2 ##
def luc_seq():
    """A generator that yields the Lucas Sequence
    >>> gen = luc_seq()
    >>> next(gen)
    2
    >>> next(gen)
    1
    >>> next(gen)
    3

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> next(gen)
    4
    >>> next(gen)
    7
    >>> next(gen)
    11
    >>> next(gen)
    18
    >>> next(gen)
    29
    >>> next(gen)
    47
    """
    n=0
    start=2
    out=0
    last=0
    second_last=0
    while True:
        if n==0:
            out= start
        elif n==1:
            out= n
        else:
            out=last+second_last
        yield out
        second_last=last
        last=out
        n+=1
         

## Question 2.3 ##
def alpha_gen(stars_count, word):
    """Return a function that creates a generator that yields a
    letter from a given string with a specified number of stars between
    each letter.

    >>> gen = alpha_gen(2, "marina")
    >>> next(gen)
    'm'
    >>> next(gen)
    '*'
    >>> next(gen)
    '*'
    >>> for i in gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gen = alpha_gen(0, "data")
    >>> next(gen)
    'd'
    >>> next(gen)
    'a'
    >>> gen = alpha_gen(10, "cali")
    >>> next(gen)
    'c'
    >>> next(gen)
    '*'
    >>> next(gen)
    '*'
    >>> for i in gen:
    ... 	print(i, end='')
    ********a**********l**********i**********
    """
    
    for letter in word:
        yield letter
        for i in range(stars_count):
            yield '*'
## Question 2.4 ##
def generate_generators():
    """
    Return a generator that yields the previous three generators.
    First Yield:  exp_gen
    Second Yield: luc_seq
    Third Yield:  alpha_gen

    >>> gen_list = generate_generators()
    >>> exp_gnr = next(gen_list)
    >>> lucas_gnr = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gnr(2,2)
    >>> next(func1)
    4
    >>> next(func1)
    16
    >>> next(func1)
    64
    >>> next(lucas_gnr)
    2
    >>> next(lucas_gnr)
    1
    >>> next(lucas_gnr)
    3
    >>> alpha_gen = alpha_func(2, "marina")
    >>> next(alpha_gen)
    'm'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> func2 = exp_gnr(8,2)
    >>> next(func2)
    64
    >>> next(func2)
    256
    >>> next(func2)
    1024
    >>> next(lucas_gnr)
    4
    >>> next(lucas_gnr)
    7
    >>> next(lucas_gnr)
    11
    >>> alpha_gen = alpha_func(3, "surf")
    >>> next(alpha_gen)
    's'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    *u***r***f***
    """
    yield exp_gen
    yield luc_seq()
    yield alpha_gen

## Question 3 ##
def get_negative_lists(super_list):
    """
    Return a map object containing the lists in the
    super list that contain negative numbers.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    super_list (list): A list containing sublists of integers

    Returns:
    The map required by the question.

    >>> subLsts = [[1, 5, 2, 8, 4], [-900, -22, 33, -90, 529],\
[0, -2, 5, -199, 300]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-900, -22, 33, -90, 529], [0, -2, 5, -199, 300]]
    >>> subLsts = [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3], [0, 0, 1, 0, 0]]
    >>> list(get_negative_lists(subLsts))
    [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> subLsts = [[1, 2, 3, 4, 5], [0],[-1],[-89, 9273, -1, 0]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-1], [-89, 9273, -1, 0]]
    >>> subLsts = [[2, 9999, -6, 9087], [-1, 0, 0, 0, 1], [-7], [0]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[2, 9999, -6, 9087], [-1, 0, 0, 0, 1], [-7]]
    """
    def contain_negative(lst):
        if len(list(filter(lambda x:x<0,lst)))>0:
            return True
        else:
            return False
    return filter(lambda x:contain_negative(x),super_list)

## Question 4 ##
def get_distances():
    """
    Return a list of lambdas that help do bulk distance calculations on city
    coordinates.
    1: Define a function that converts miles to km, with miles as the input.
    2: Define a function that determines the distance between two points that
       use (x, y) coordinates as inputs
    3: Determine how many kilometers are between Point A(424.3601, 71.0589)
       and Point B (-3601.1128, 493.4276)
    4: Return a lambda that returns a map object of the distances between a
       list of tuple pairs of cities.


    >>> cities = [(424.3601, 71.0589), (-3601.1128, 493.4276), \
(158.1010, 8179.001), (-119.030, -117.334)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    4047.5705537240606
    >>> lambda_functions[2]((cities[0], cities[1]))
    6513.933385212495
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [6513.933385212495, 13359.103960657963]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cities = [(327.73,16726.83), (123.456,-897.3), \
(7826,7382.09), (-999, 999)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](0)
    0.0
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    17625.313787957817
    >>> lambda_functions[2]((cities[0], cities[1]))
    28365.192992767188
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [28365.192992767188, 17528.14732453411]
    """
    square_root=1/2
    square=2
    m_to_k=1.609344
    func1=lambda dis:dis*m_to_k
    func2=lambda x1,y1,x2,y2:((x1-x2)**square+(y1-y2)**square)**square_root
    func3=lambda loc:func1(func2(loc[0][0],loc[0][1],loc[1][0],loc[1][1]))
    func4=lambda lst:map(lambda city:func3(city),lst)
    return [func1,func2,func3,func4]



## Question 5 ##
def calculate_wages(filepath):
    """
    Calculator for tutor wages. See question description for explanation.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    filepath (str): Path to the input file

    Returns:
    dict: Dictionary of tutor names and their total wages

    >>> calculate_wages('data/input.txt')
    {'Judy': 8, 'Owen': 40, 'Xiang': 460}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> calculate_wages('doc_input_1.txt')
    {'Max': 140, 'Liz': 0, 'Eric': 3072, 'Seth': 0}
    >>> calculate_wages('doc_input_2.txt')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> calculate_wages('doc_input_3.txt')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    
    cut=5
    pay1=8
    pay2=12
    
    dic={}
    file=open(filepath,'r')
    txt=file.read()
    file.close()
    lines=txt.strip().split('\n')
    lines=list(map(lambda line:line.strip().split(','),lines))
    names,week1,week2,week3=list(zip(*lines))
    clean_func=lambda x:x.strip()
    check_int=lambda x:ord(x[0])>=48 and ord(x[0])<=57
    check_str=lambda x:ord(x[0])<=47 or ord(x[0])>=58
    assert all(list(map(check_str,list(map(clean_func,names)))))
    assert all(list(map(check_int,list(map(clean_func,week1)))))
    assert all(list(map(check_int,list(map(clean_func,week2)))))
    assert all(list(map(check_int,list(map(clean_func,week3)))))
    int_func=lambda x:int(x)
    unpaid=lambda x:0 if x<=cut else x-cut
    pay_func=lambda x:x*pay1 if x<=cut else (x-cut)*pay2+(cut*pay1)
    total_func=lambda x,y,z:x+y+z
    week1=list(map(pay_func,list(map(unpaid,list(map(int_func,week1))))))
    week2=list(map(pay_func,list(map(unpaid,list(map(int_func,week2))))))
    week3=list(map(pay_func,list(map(unpaid,list(map(int_func,week3))))))
    pay=list(map(total_func,week1,week2,week3))
    return dict(zip(names,pay))
    
    
    

## Question 6 ##
def calculate_best_scores(formulas, scores):
    """
    Calculates the maximum score achievable with the provided formulas.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    formulas (list(lambda)) : List of lambda functions to be applied to scores
    scores (list(int)) : List of integers indicating the scores for students

    Returns:
    list : List of scores with the function that maximizes each score applied
    to it

    >>> calculate_best_scores([lambda x : x - 1], [3, 4, 5])
    [3, 4, 5]
    >>> calculate_best_scores([lambda x : x + 1], [3, 4, 5])
    [4, 5, 6]
    >>> calculate_best_scores([lambda x : x + 1, lambda x : x * 2,\
lambda x : x - 1], [3, 4, 5])
    [6, 8, 10]
    >>> calculate_best_scores([lambda x : x + 20, lambda x : x * 2,\
lambda x : x * 3], [3, 4, 20])
    [23, 24, 60]
    >>> calculate_best_scores([lambda x : x + 20, 123], [3, 4, 5])
    [23, 24, 25]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> calculate_best_scores([lambda x : x * 1], [3, '4', 5])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> calculate_best_scores([lambda x : x + 9, 99,\
lambda x : x * 99],[1, 9, 99])
    [99, 891, 9801]
    >>> calculate_best_scores([lambda x : x - 5, lambda x : x * 0,\
lambda x : x ** 9], [-2, 9, 5])
    [0, 387420489, 1953125]
    """
    assert all(list(map(lambda x:isinstance(x,int),scores)))
    formulas=list(filter(lambda func:not isinstance(func,int),formulas))
    formulas.append(lambda x:x)
    possible_scores=list(map(lambda func:list(map(lambda score:func(score),scores)),formulas))
    possible_score=list(zip(*possible_scores))
    return list(map(lambda x:max(x),possible_score))
    
    
    
    
## Question 7 ##
def best_champ(champion_dict):
    """
    Returns a dictionary of champions and calculated scores.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    champion_dict: a dictionary of champions and K/D/A slash lines

    Returns:
    dict: a dictionary of champions and scores

    >>> champ_dict = {'Lucian': '20/7/8', 'Caitlyn': '2/8/4', \
"Kha\'Zix": '0/19/2'}
    >>> best_champ(champ_dict)
    {'Lucian': 77.0, 'Caitlyn': -2.0, "Kha'Zix": -8.5}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> champ_dict = {'Ben': '2/99/3', 'Sam': '99/3/2', 'Earn': '3/3/3'}
    >>> best_champ(champ_dict)
    {'Ben': -44.0, 'Sam': 394.0, 'Earn': 4.5}
    >>> champ_dict = {'Big': '99/99/99', 'Small': '0/0/0'}
    >>> best_champ(champ_dict)
    {'Big': 396.0, 'Small': 0.0}
    >>> champ_dict = {'Guy': '50/9/32'}
    >>> best_champ(champ_dict)
    {'Guy': 207.0}
    """
    cutoff=10
    high_kills=4
    low_kills=2
    half=1/2
    negative=-1
    kills_func=lambda k: k*high_kills if k>=cutoff else k*low_kills
    death_func=lambda d: d*half*negative if d>=cutoff else d*negative
    assist_func=lambda a:a*half
    int_func=lambda lst:list(map(lambda x:int(x),lst))
    split=lambda kda:kda.split('/')
    split_values=list(map(split,champion_dict.values()))
    int_values=list(map(int_func,split_values))
    kills,deaths,assists=zip(*int_values)
    kill_scores=list(map(kills_func,kills))
    death_scores=list(map(death_func,deaths))
    assist_scores=list(map(assist_func,assists))
    scores_list=list(zip(kill_scores,death_scores,assist_scores))
    scores=list(map(lambda x:sum(x),scores_list))
    return dict(zip(champion_dict.keys(),scores))
    
## Question 8 ## (Extra Credit)
def find_positive_magic_integer(filepath):
    """
    Find any positive magic integers in the given file and output a dictionary
    whose keys are the string value of the found magic numbers and values
    are the line numbers where they were found.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    The dictionary described above.

    >>> find_positive_magic_integer('./data/magic_number_test1.py')
    {'2': [3, 11], '3': [4, 11], '4': [5, 11], '5': [6, 11], '6': [7, 11], \
'7': [8, 11], '8': [9, 11], '9': [10, 11]}
    >>> find_positive_magic_integer('./data/magic_number_test2.py')
    {'20': [1, 7, 15], '5': [3, 8], '2': [4, 5, 5, 12], '3': [4, 6, 6, 6], '8': [12]}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> find_positive_magic_integer('doc_magic_1.txt')
    {'9273': [1], '273': [1], '73': [1], '3': [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, \
5, 5, 5], '783': [1], '83': [1], '98': [1], '8': [1, 2, 3, 3, 4, 5, 5, 5], \
'9': [1, 3, 4, 5], '43': [2], '23': [3], '38': [4], '83754': [4], '3754': \
[4], '754': [4], '54': [4], '4': [4], '89': [5]}
    >>> find_positive_magic_integer('doc_magic_2.txt')
    {'89': [2], '9': [2, 6], '8': [2], '4': [3], '67': [3], '7': [3, 5], \
'87': [5]}
    >>> find_positive_magic_integer('doc_magic_3.txt')
    {'9238': [1, 6], '238': [1, 6], '38': [1, 3, 4, 4, 5, 6, 7], '8': [1, 1, \
3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 11, 11], '79': [1, 6], '9': [1, \
5, 6, 7, 7, 7, 13, 13], '4': [1, 6], '3': [1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, \
6, 7, 7, 7, 7, 7, 9, 11], '83': [2, 3, 4, 5], '93': [5, 11], '98': [11], \
'48': [11], '39': [13]}
    """
    file=open(filepath)
    txt=file.read()
    lines=txt.strip().split('\n')
    line=0
    dic={}
    num=0
    for l in lines:
        line+=1
        for c in range(len(l)):
            if ord(l[c])>=48 and ord(l[c])<=57 and int(l[c])>1:
                temp1 = l[c]
                while ord(l[c])>=48 and ord(l[c])<=57:
                    if c+1==len(l):
                        break
                    if ord(l[c+1])>=48 and ord(l[c+1])<=57:
                        temp1 += l[c+1]
                        c += 1
                    else:
                        c+=1 
                if temp1 in dic:
                    dic[temp1].append(line)
                else:
                    dic.update({temp1:[line]})
    return dic
    
