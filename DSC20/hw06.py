"""
DSC 20 HW 06
NAME: Maxwell Levitt
PID: A15788481
"""

## Question 1.1 ##
def conversion_binary(n):
    """
    Converts the given base-10 number to binary representation.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert

    Returns:
    (str): Binary representation of the input

    >>> conversion_binary(86)
    '1010110'
    >>> conversion_binary(1)
    '1'
    >>> conversion_binary(0)
    '0'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> conversion_binary(100)
    '1100100'
    >>> conversion_binary(999)
    '1111100111'
    >>> conversion_binary('0')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    base=2
    assert isinstance(n,int)
    if n//base==0:
        return str(n%base)
    else:
        return conversion_binary(n//base)+str(n%base)
        
## Question 1.2 ##
def conversion_any(n, base):
    """
    Converts the given base-10 number to any base representation given by the
    base parameter. Assume that base will be 10 maximum.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    n (int): Number to convert
    base (int): Base to convert the number to

    Returns:
    (str): Base-x representation of the input number n

    >>> conversion_any(86, 2)
    '1010110'
    >>> conversion_any(86, 3)
    '10012'
    >>> conversion_any(86, 4)
    '1112'
    >>> conversion_any(86, 10)
    '86'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> conversion_any(9, 8)
    '11'
    >>> conversion_any(999, 3)
    '1101000'
    >>> conversion_any(1000, 10)
    '1000'
    >>> conversion_any('1', 10)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    cutoff=10
    assert isinstance(n,int) and isinstance(base,int)
    assert n>=0 and base>1 and base<=cutoff
    if n//base==0:
        return str(n%base)
    else:
        return conversion_any(n//base,base)+str(n%base)
        
## Question 2.1 ##
def create_recursive_list(rec_count):
    """
    Returns a list with a recursive structure who has "rec_count" levels.

    Restrictions:
    You should use recursion in this question. You should do input validation.

    Parameters:
    rec_count (int): Depth of recursion in the list

    Returns:
    Recursion list specified in the question

    >>> create_recursive_list(0)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(1)
    [1]
    >>> create_recursive_list(2)
    [2, [1]]
    >>> create_recursive_list(5)
    [5, [4, [3, [2, [1]]]]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_recursive_list('0')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_recursive_list(8)
    [8, [7, [6, [5, [4, [3, [2, [1]]]]]]]]
    >>> create_recursive_list(10)
    [10, [9, [8, [7, [6, [5, [4, [3, [2, [1]]]]]]]]]]
    >>> create_recursive_list(25)
    [25, [24, [23, [22, [21, [20, [19, [18, [17, [16, [15, [14, [13, [12, [11\
, [10, [9, [8, [7, [6, [5, [4, [3, [2, [1]]]]]]]]]]]]]]]]]]]]]]]]]
    """
    assert isinstance(rec_count,int) and rec_count>0
    if rec_count>1:
        return [rec_count, create_recursive_list(rec_count-1)]
    else:
        return [rec_count]
        
## Question 2.2 ##
def decode_recursive_list(rec_list):
    """
    Decodes a list of the recursive structure from the previous question.
    Returns a single level list containing the elements of the above list,
    in the same order.

    Restrictions:
    You should do input validation. Recursion is NOT required.

    Parameters:
    rec_list (list): Recursive list as defined in Q1.1

    Returns:
    Recursive list decoded in a normal list format

    >>> decode_recursive_list([1])
    [1]
    >>> decode_recursive_list([2, [1]])
    [2, 1]
    >>> decode_recursive_list([5, [4, [3, [2, [1]]]]])
    [5, 4, 3, 2, 1]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> decode_recursive_list([1,2])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode_recursive_list([10, [9, [8, [7, [6, [5, [4, [3, [2, [1]]]]]]]]]])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> decode_recursive_list([8, [7, [6, [5, [4, [3, [2, [1]]]]]]]])
    [8, 7, 6, 5, 4, 3, 2, 1]
    """
    assert create_recursive_list(rec_list[0])==rec_list
    lst=[]
    for i in range(rec_list[0],0,-1):
        lst+=[i]
    return lst

## Question 3.1 ##
def fibonacci_gen():
    """
    Yields the numbers of the Fibonacci sequence starting from F(1).

    Restrictions:
    This function should be a generator

    Returns:
    The fibonacci sequence in generator format

    >>> fibo = fibonacci_gen()
    >>> next(fibo)
    1
    >>> next(fibo)
    1
    >>> [next(fibo) for i in range(8)]
    [2, 3, 5, 8, 13, 21, 34, 55]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc1 = fibonacci_gen()
    >>> next(doc1)
    1
    >>> next(doc1)
    1
    >>> [next(doc1) for i in range(100)]
    [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181\
, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832\
040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169\
, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170\
, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32\
951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162\
, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 655\
7470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72\
723460248141, 117669030460994, 190392490709135, 308061521170129, 4984540118792\
64, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 552\
7939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 3788906\
2373143906, 61305790721611591, 99194853094755497, 160500643816367088, 25969549\
6911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 17799\
79416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429\
, 12200160415121876738, 19740274219868223167, 31940434634990099905, 516807088\
54858323072, 83621143489848422977, 135301852344706746049, 2189229958345551690\
26, 354224848179261915075, 573147844013817084101, 927372692193078999176]

    
    """
    a=0
    b=0
    c=1
    while True:
        yield c
        a=b
        b=c
        c=a+b
        
## Question 3.2 ##
def approximate_pi(n):
    """
    Returns  the nth approximation of pi according to the Leibniz series.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place. You should use recursion in this question.

    Parameters:
    n (int): Represents nth approximation of pi.

    Returns:
    (float) The nth approximation of pi.

    >>> approximate_pi(1)
    4
    >>> approximate_pi(25)
    3.181
    >>> approximate_pi(50)
    3.122

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> approximate_pi(-1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> approximate_pi(2)
    2.667
    >>> approximate_pi(100)
    3.131
    """
    mult=4
    dbl=2
    rnd=3
    assert isinstance(n,int) and n>0
    if n==1:
        return mult
    else:
        return round(mult*((-1)**(n+1))/(dbl*(n-1)+1)+approximate_pi(n-1),rnd)
    
## Question 3.3 ##
def pi_fibo_generator():
    """
    Yields the result of the current approximation of pi times the
    the current fibonacci number in their respective sequences.

    Restrictions:
    You should do input validation. You should round results to the 3rd
    decimal place.

    Returns:
    Multiplication of the nth approximation of pi and nth fibonacci number

    >>> pi_fibo = pi_fibo_generator()
    >>> [next(pi_fibo) for i in range(5)]
    [4, 2.667, 6.934, 8.688, 16.7]
    >>> [next(pi_fibo) for i in range(5)]
    [23.808, 42.692, 63.357, 110.568, 167.255]
    >>> [next(pi_fibo) for i in range(5)]
    [287.559, 440.208, 749.561, 1157.013, 1956.27]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc = pi_fibo_generator()
    >>> next(doc)
    4
    >>> next(doc)
    2.667
    >>> [next(doc) for i in range(100)]
    [6.934, 8.688, 16.7, 23.808, 42.692, 63.357, 110.568, 167.255, 287.559, 44\
0.208, 749.561, 1157.013, 1956.27, 3037.986, 5108.803, 7971.64, 13349.933, 209\
03.85, 34895.848, 54815.545, 91243.888, 143694.432, 238654.525, 376682.479, 62\
4216.404, 986803.155, 1632677.075, 2585148.28, 4271711.537, 6774540.99, 111799\
61.416, 17747384.344, 29251064.05, 46493116.128, 76556122.073, 121798734.604, \
200363283.648, 318975561.135, 524226726.406, 835356774.928, 1372009893.105, 21\
87693838.227, 3590833629.88, 5729293137.36, 9397953275.899, 15004291692.096, 2\
4596382358.938, 39294331896.05, 64394165015.988, 102906847749.177, 16853279639\
7.853, 269499892653.728, 441224589188.645, 705785730365.625, 1154775535871.92\
, 1847771030871.875, 3022284880263.519, 4837527362250.0, 7909939809432.838, 12\
664811055878.125, 20701933799741.195, 33167516015242.098, 54198366320572.7, 86\
833684250310.28, 141848219591764.06, 227333536735688.75, 371245791104436.06, 5\
95166925956756.0, 971626037770586.9, 1558167241134579.2, 2543749991237785.5, 4\
080639766991910.0, 6659623935942770.0, 1.068667006045218e+16, 1.74351218165905\
24e+16, 2.79780654448197e+16, 4.563126917980412e+16, 7.324752627400691e+16, 1.\
1946421366252274e+17, 1.9176451337720106e+17, 3.126621769546694e+17, 5.0204601\
38575963e+17, 8.185602062638584e+17, 1.3147937243363151e+18, 2.143018441836905\
7e+18, 3.442174658507533e+18, 5.610495119246859e+18, 9.014610318380654e+18, 1.\
4688466915903672e+19, 2.3600556208856064e+19, 3.845490562846416e+19, 6.1806798\
5824074e+19, 1.006762499694888e+20, 1.618122994245614e+20, 2.6357384428000225e\
+20, 4.236300996912768e+20, 6.898263598746833e+20, 1.1090779996492691e+21, 1.8\
059888564875375e+21, 2.90360389925653e+21]
    """
    def fibonacci_gen():
        a=0
        b=0
        c=1
        while True:
            yield c
            a=b
            b=c
            c=a+b
    def approximate_pi(n):
        mt=4
        dl=2
        rd=3
        assert isinstance(n,int) and n>0
        if n==1:
            return mt
        else:
            return round(mt*((-1)**(n+1))/(dl*(n-1)+1)+approximate_pi(n-1),rd)
    fibo=fibonacci_gen()
    round_fac=3
    count=0
    while True:
        count+=1
        yield round(next(fibo)*approximate_pi(count),round_fac)

## Question 4 ##
def create_powerset(parent_list):
    """
    Creates the powerset of the set represented by parent_list.

    Restrictions:
    You should do input validation. You can use at most one loop (not nested).

    Parameters:
    parent_list (list): The list for which the powersets will be created

    Returns:
    (list) The powerset of list parent_list

    >>> create_powerset([])
    [[]]
    >>> create_powerset('hello')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> lst_to_return = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> arg1 = create_powerset([1, 2, 3])
    >>> arg1.sort()
    >>> arg1 == lst_to_return
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> lst_to_return = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], \
[1, 3], [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]
    >>> doc1 = create_powerset([1,2,3,4])
    >>> doc1.sort()
    >>> doc1 == lst_to_return
    True
    >>> lst_to_return = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, \
4, 5], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [1\
, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9], [1, 2, 3, 4, 5, 6, 8], [1\
, 2, 3, 4, 5, 6, 8, 9], [1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 7], [1, 2, 3, 4\
, 5, 7, 8], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 9], [1, 2, 3, 4, 5, 8\
], [1, 2, 3, 4, 5, 8, 9], [1, 2, 3, 4, 5, 9], [1, 2, 3, 4, 6], [1, 2, 3, 4, 6\
, 7], [1, 2, 3, 4, 6, 7, 8], [1, 2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 9], \
[1, 2, 3, 4, 6, 8], [1, 2, 3, 4, 6, 8, 9], [1, 2, 3, 4, 6, 9], [1, 2, 3, 4, 7]\
, [1, 2, 3, 4, 7, 8], [1, 2, 3, 4, 7, 8, 9], [1, 2, 3, 4, 7, 9], [1, 2, 3, 4, \
8], [1, 2, 3, 4, 8, 9], [1, 2, 3, 4, 9], [1, 2, 3, 5], [1, 2, 3, 5, 6], [1, 2\
, 3, 5, 6, 7], [1, 2, 3, 5, 6, 7, 8], [1, 2, 3, 5, 6, 7, 8, 9], [1, 2, 3, 5, 6\
, 7, 9], [1, 2, 3, 5, 6, 8], [1, 2, 3, 5, 6, 8, 9], [1, 2, 3, 5, 6, 9], [1, 2\
, 3, 5, 7], [1, 2, 3, 5, 7, 8], [1, 2, 3, 5, 7, 8, 9], [1, 2, 3, 5, 7, 9], [1\
, 2, 3, 5, 8], [1, 2, 3, 5, 8, 9], [1, 2, 3, 5, 9], [1, 2, 3, 6], [1, 2, 3, 6\
, 7], [1, 2, 3, 6, 7, 8], [1, 2, 3, 6, 7, 8, 9], [1, 2, 3, 6, 7, 9], [1, 2, 3\
, 6, 8], [1, 2, 3, 6, 8, 9], [1, 2, 3, 6, 9], [1, 2, 3, 7], [1, 2, 3, 7, 8], [\
1, 2, 3, 7, 8, 9], [1, 2, 3, 7, 9], [1, 2, 3, 8], [1, 2, 3, 8, 9], [1, 2, 3, 9\
], [1, 2, 4], [1, 2, 4, 5], [1, 2, 4, 5, 6], [1, 2, 4, 5, 6, 7], [1, 2, 4, 5, \
6, 7, 8], [1, 2, 4, 5, 6, 7, 8, 9], [1, 2, 4, 5, 6, 7, 9], [1, 2, 4, 5, 6, 8]\
, [1, 2, 4, 5, 6, 8, 9], [1, 2, 4, 5, 6, 9], [1, 2, 4, 5, 7], [1, 2, 4, 5, 7, \
8], [1, 2, 4, 5, 7, 8, 9], [1, 2, 4, 5, 7, 9], [1, 2, 4, 5, 8], [1, 2, 4, 5, 8\
, 9], [1, 2, 4, 5, 9], [1, 2, 4, 6], [1, 2, 4, 6, 7], [1, 2, 4, 6, 7, 8], [1, \
2, 4, 6, 7, 8, 9], [1, 2, 4, 6, 7, 9], [1, 2, 4, 6, 8], [1, 2, 4, 6, 8, 9], [1\
, 2, 4, 6, 9], [1, 2, 4, 7], [1, 2, 4, 7, 8], [1, 2, 4, 7, 8, 9], [1, 2, 4, 7\
, 9], [1, 2, 4, 8], [1, 2, 4, 8, 9], [1, 2, 4, 9], [1, 2, 5], [1, 2, 5, 6], [1\
, 2, 5, 6, 7], [1, 2, 5, 6, 7, 8], [1, 2, 5, 6, 7, 8, 9], [1, 2, 5, 6, 7, 9], \
[1, 2, 5, 6, 8], [1, 2, 5, 6, 8, 9], [1, 2, 5, 6, 9], [1, 2, 5, 7], [1, 2, 5, \
7, 8], [1, 2, 5, 7, 8, 9], [1, 2, 5, 7, 9], [1, 2, 5, 8], [1, 2, 5, 8, 9], [1\
, 2, 5, 9], [1, 2, 6], [1, 2, 6, 7], [1, 2, 6, 7, 8], [1, 2, 6, 7, 8, 9], [1, \
2, 6, 7, 9], [1, 2, 6, 8], [1, 2, 6, 8, 9], [1, 2, 6, 9], [1, 2, 7], [1, 2, 7\
, 8], [1, 2, 7, 8, 9], [1, 2, 7, 9], [1, 2, 8], [1, 2, 8, 9], [1, 2, 9], [1, 3\
], [1, 3, 4], [1, 3, 4, 5], [1, 3, 4, 5, 6], [1, 3, 4, 5, 6, 7], [1, 3, 4, 5, \
6, 7, 8], [1, 3, 4, 5, 6, 7, 8, 9], [1, 3, 4, 5, 6, 7, 9], [1, 3, 4, 5, 6, 8]\
, [1, 3, 4, 5, 6, 8, 9], [1, 3, 4, 5, 6, 9], [1, 3, 4, 5, 7], [1, 3, 4, 5, 7, \
8], [1, 3, 4, 5, 7, 8, 9], [1, 3, 4, 5, 7, 9], [1, 3, 4, 5, 8], [1, 3, 4, 5, 8\
, 9], [1, 3, 4, 5, 9], [1, 3, 4, 6], [1, 3, 4, 6, 7], [1, 3, 4, 6, 7, 8], [1, \
3, 4, 6, 7, 8, 9], [1, 3, 4, 6, 7, 9], [1, 3, 4, 6, 8], [1, 3, 4, 6, 8, 9], [1\
, 3, 4, 6, 9], [1, 3, 4, 7], [1, 3, 4, 7, 8], [1, 3, 4, 7, 8, 9], [1, 3, 4, 7\
, 9], [1, 3, 4, 8], [1, 3, 4, 8, 9], [1, 3, 4, 9], [1, 3, 5], [1, 3, 5, 6], [1\
, 3, 5, 6, 7], [1, 3, 5, 6, 7, 8], [1, 3, 5, 6, 7, 8, 9], [1, 3, 5, 6, 7, 9], \
[1, 3, 5, 6, 8], [1, 3, 5, 6, 8, 9], [1, 3, 5, 6, 9], [1, 3, 5, 7], [1, 3, 5, \
7, 8], [1, 3, 5, 7, 8, 9], [1, 3, 5, 7, 9], [1, 3, 5, 8], [1, 3, 5, 8, 9], [1\
, 3, 5, 9], [1, 3, 6], [1, 3, 6, 7], [1, 3, 6, 7, 8], [1, 3, 6, 7, 8, 9], [1, \
3, 6, 7, 9], [1, 3, 6, 8], [1, 3, 6, 8, 9], [1, 3, 6, 9], [1, 3, 7], [1, 3, 7\
, 8], [1, 3, 7, 8, 9], [1, 3, 7, 9], [1, 3, 8], [1, 3, 8, 9], [1, 3, 9], [1, 4\
], [1, 4, 5], [1, 4, 5, 6], [1, 4, 5, 6, 7], [1, 4, 5, 6, 7, 8], [1, 4, 5, 6, \
7, 8, 9], [1, 4, 5, 6, 7, 9], [1, 4, 5, 6, 8], [1, 4, 5, 6, 8, 9], [1, 4, 5, 6\
, 9], [1, 4, 5, 7], [1, 4, 5, 7, 8], [1, 4, 5, 7, 8, 9], [1, 4, 5, 7, 9], [1, \
4, 5, 8], [1, 4, 5, 8, 9], [1, 4, 5, 9], [1, 4, 6], [1, 4, 6, 7], [1, 4, 6, 7\
, 8], [1, 4, 6, 7, 8, 9], [1, 4, 6, 7, 9], [1, 4, 6, 8], [1, 4, 6, 8, 9], [1, \
4, 6, 9], [1, 4, 7], [1, 4, 7, 8], [1, 4, 7, 8, 9], [1, 4, 7, 9], [1, 4, 8], [\
1, 4, 8, 9], [1, 4, 9], [1, 5], [1, 5, 6], [1, 5, 6, 7], [1, 5, 6, 7, 8], [1, \
5, 6, 7, 8, 9], [1, 5, 6, 7, 9], [1, 5, 6, 8], [1, 5, 6, 8, 9], [1, 5, 6, 9]\
, [1, 5, 7], [1, 5, 7, 8], [1, 5, 7, 8, 9], [1, 5, 7, 9], [1, 5, 8], [1, 5, 8\
, 9], [1, 5, 9], [1, 6], [1, 6, 7], [1, 6, 7, 8], [1, 6, 7, 8, 9], [1, 6, 7, 9\
], [1, 6, 8], [1, 6, 8, 9], [1, 6, 9], [1, 7], [1, 7, 8], [1, 7, 8, 9], [1, 7\
, 9], [1, 8], [1, 8, 9], [1, 9], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, \
4, 5, 6], [2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8, 9]\
, [2, 3, 4, 5, 6, 7, 9], [2, 3, 4, 5, 6, 8], [2, 3, 4, 5, 6, 8, 9], [2, 3, 4\
, 5, 6, 9], [2, 3, 4, 5, 7], [2, 3, 4, 5, 7, 8], [2, 3, 4, 5, 7, 8, 9], [2, 3\
, 4, 5, 7, 9], [2, 3, 4, 5, 8], [2, 3, 4, 5, 8, 9], [2, 3, 4, 5, 9], [2, 3, 4\
, 6], [2, 3, 4, 6, 7], [2, 3, 4, 6, 7, 8], [2, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6\
, 7, 9], [2, 3, 4, 6, 8], [2, 3, 4, 6, 8, 9], [2, 3, 4, 6, 9], [2, 3, 4, 7], [\
2, 3, 4, 7, 8], [2, 3, 4, 7, 8, 9], [2, 3, 4, 7, 9], [2, 3, 4, 8], [2, 3, 4, 8\
, 9], [2, 3, 4, 9], [2, 3, 5], [2, 3, 5, 6], [2, 3, 5, 6, 7], [2, 3, 5, 6, 7, \
8], [2, 3, 5, 6, 7, 8, 9], [2, 3, 5, 6, 7, 9], [2, 3, 5, 6, 8], [2, 3, 5, 6, 8\
, 9], [2, 3, 5, 6, 9], [2, 3, 5, 7], [2, 3, 5, 7, 8], [2, 3, 5, 7, 8, 9], [2, \
3, 5, 7, 9], [2, 3, 5, 8], [2, 3, 5, 8, 9], [2, 3, 5, 9], [2, 3, 6], [2, 3, 6\
, 7], [2, 3, 6, 7, 8], [2, 3, 6, 7, 8, 9], [2, 3, 6, 7, 9], [2, 3, 6, 8], [2, \
3, 6, 8, 9], [2, 3, 6, 9], [2, 3, 7], [2, 3, 7, 8], [2, 3, 7, 8, 9], [2, 3, 7\
, 9], [2, 3, 8], [2, 3, 8, 9], [2, 3, 9], [2, 4], [2, 4, 5], [2, 4, 5, 6], [2\
, 4, 5, 6, 7], [2, 4, 5, 6, 7, 8], [2, 4, 5, 6, 7, 8, 9], [2, 4, 5, 6, 7, 9]\
, [2, 4, 5, 6, 8], [2, 4, 5, 6, 8, 9], [2, 4, 5, 6, 9], [2, 4, 5, 7], [2, 4, 5\
, 7, 8], [2, 4, 5, 7, 8, 9], [2, 4, 5, 7, 9], [2, 4, 5, 8], [2, 4, 5, 8, 9], [\
2, 4, 5, 9], [2, 4, 6], [2, 4, 6, 7], [2, 4, 6, 7, 8], [2, 4, 6, 7, 8, 9], [2\
, 4, 6, 7, 9], [2, 4, 6, 8], [2, 4, 6, 8, 9], [2, 4, 6, 9], [2, 4, 7], [2, 4, \
7, 8], [2, 4, 7, 8, 9], [2, 4, 7, 9], [2, 4, 8], [2, 4, 8, 9], [2, 4, 9], [2, \
5], [2, 5, 6], [2, 5, 6, 7], [2, 5, 6, 7, 8], [2, 5, 6, 7, 8, 9], [2, 5, 6, 7\
, 9], [2, 5, 6, 8], [2, 5, 6, 8, 9], [2, 5, 6, 9], [2, 5, 7], [2, 5, 7, 8], [2\
, 5, 7, 8, 9], [2, 5, 7, 9], [2, 5, 8], [2, 5, 8, 9], [2, 5, 9], [2, 6], [2, 6\
, 7], [2, 6, 7, 8], [2, 6, 7, 8, 9], [2, 6, 7, 9], [2, 6, 8], [2, 6, 8, 9], [2\
, 6, 9], [2, 7], [2, 7, 8], [2, 7, 8, 9], [2, 7, 9], [2, 8], [2, 8, 9], [2, 9]\
, [3], [3, 4], [3, 4, 5], [3, 4, 5, 6], [3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8], [\
3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 9], [3, 4, 5, 6, 8], [3, 4, 5, 6, 8, 9]\
, [3, 4, 5, 6, 9], [3, 4, 5, 7], [3, 4, 5, 7, 8], [3, 4, 5, 7, 8, 9], [3, 4, 5\
, 7, 9], [3, 4, 5, 8], [3, 4, 5, 8, 9], [3, 4, 5, 9], [3, 4, 6], [3, 4, 6, 7]\
, [3, 4, 6, 7, 8], [3, 4, 6, 7, 8, 9], [3, 4, 6, 7, 9], [3, 4, 6, 8], [3, 4, 6\
, 8, 9], [3, 4, 6, 9], [3, 4, 7], [3, 4, 7, 8], [3, 4, 7, 8, 9], [3, 4, 7, 9]\
, [3, 4, 8], [3, 4, 8, 9], [3, 4, 9], [3, 5], [3, 5, 6], [3, 5, 6, 7], [3, 5, \
6, 7, 8], [3, 5, 6, 7, 8, 9], [3, 5, 6, 7, 9], [3, 5, 6, 8], [3, 5, 6, 8, 9], \
[3, 5, 6, 9], [3, 5, 7], [3, 5, 7, 8], [3, 5, 7, 8, 9], [3, 5, 7, 9], [3, 5, 8\
], [3, 5, 8, 9], [3, 5, 9], [3, 6], [3, 6, 7], [3, 6, 7, 8], [3, 6, 7, 8, 9], \
[3, 6, 7, 9], [3, 6, 8], [3, 6, 8, 9], [3, 6, 9], [3, 7], [3, 7, 8], [3, 7, 8\
, 9], [3, 7, 9], [3, 8], [3, 8, 9], [3, 9], [4], [4, 5], [4, 5, 6], [4, 5, 6, \
7], [4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 9], [4, 5, 6, 8], [4, 5\
, 6, 8, 9], [4, 5, 6, 9], [4, 5, 7], [4, 5, 7, 8], [4, 5, 7, 8, 9], [4, 5, 7, \
9], [4, 5, 8], [4, 5, 8, 9], [4, 5, 9], [4, 6], [4, 6, 7], [4, 6, 7, 8], [4, 6\
, 7, 8, 9], [4, 6, 7, 9], [4, 6, 8], [4, 6, 8, 9], [4, 6, 9], [4, 7], [4, 7, 8\
], [4, 7, 8, 9], [4, 7, 9], [4, 8], [4, 8, 9], [4, 9], [5], [5, 6], [5, 6, 7]\
, [5, 6, 7, 8], [5, 6, 7, 8, 9], [5, 6, 7, 9], [5, 6, 8], [5, 6, 8, 9], [5, 6\
, 9], [5, 7], [5, 7, 8], [5, 7, 8, 9], [5, 7, 9], [5, 8], [5, 8, 9], [5, 9], [\
6], [6, 7], [6, 7, 8], [6, 7, 8, 9], [6, 7, 9], [6, 8], [6, 8, 9], [6, 9], [7]\
, [7, 8], [7, 8, 9], [7, 9], [8], [8, 9], [9]]
    >>> doc2 = create_powerset([1, 2, 3,4,5,6,7,8,9])
    >>> doc2.sort()
    >>> doc2 == lst_to_return
    True
    >>> create_powerset([1,2,3,'4'])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(parent_list,list)
    assert all([isinstance(i,int) for i in parent_list])
    lst=[[]]
    for i in parent_list:
        lst.append([i])
    for c in range(len(parent_list)):
        for l in lst[:len(lst)-1]:
            for i in parent_list:
                if i not in l:
                    temp=l+[i]
                    temp.sort()
                    if temp not in lst:
                        lst.append(temp)
    return lst
            

## Question 5.1 ##
def recursive_reverse_up_to_n(name, n):
    """
    Recursively reverses the given string at chunks 1..n

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be reversed
    n (int): How many times the string should be reversed

    Returns:
    (str) Reversed string with the given formula

    >>> recursive_reverse_up_to_n('Nabi', 3)
    'bNai'
    >>> recursive_reverse_up_to_n('klmn', 3)
    'mkln'
    >>> recursive_reverse_up_to_n('klmn', 4)
    'nlkm'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> recursive_reverse_up_to_n('Data Is Life', 9)
    'Ls tDaaI ife'
    >>> recursive_reverse_up_to_n('I Need A Job 4 $', 12)
    'bJAde INe  o 4 $'
    >>> recursive_reverse_up_to_n("Let's Get It", 15)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(name,str)
    assert isinstance(n,int) and n>0
    assert len(name)>=n
    if n==1:
        return name
    updated_name=recursive_reverse_up_to_n(name,n-1)
    out=updated_name[n-1::-1]+updated_name[n:]
    return out
        
## Question 5.2 ##
def undo_recursive_reverse_up_to_n(name, n):
    """
    Recursively corrects the recursive reverse
    done on the string up to n characters.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    Parameters:
    name (str): The string to be corrected
    n (int): How many times the string has been previously reversed

    Returns:
    (str) Corrected string

    >>> undo_recursive_reverse_up_to_n('bNai', 3)
    'Nabi'
    >>> undo_recursive_reverse_up_to_n('mkln', 3)
    'klmn'
    >>> undo_recursive_reverse_up_to_n('nlkm', 4)
    'klmn'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> undo_recursive_reverse_up_to_n('Ls tDaaI ife', 9)
    'Data Is Life'
    >>> undo_recursive_reverse_up_to_n('bJAde INe  o 4 $', 12)
    'I Need A Job 4 $'
    >>> undo_recursive_reverse_up_to_n('how', '-1')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(name,str)
    assert isinstance(n,int) and n>0
    assert len(name)>=n
    if n==1:
        return name
    else:
        return undo_recursive_reverse_up_to_n(name[n-1::-1]+name[n:],n-1)
        
## Question 6 ##
def build_repr(operations, templates):
    """
    Build the representation of the series of operations with the given
    templates. The operations are prioritized from right to left.

    Restrictions:
    You should use recursion. You should do input validation.

    Parameters: operations (list(str)): List of numbers and operations to be
    executed on them

    Returns: (str): String representation of the operations

    >>> build_repr([0, '+', 1, '-', 3], {'+': '({0}, +, {1})', '-':\
    '({0}, -, {1})'})
    '(0, +, (1, -, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-':'({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    >>> build_repr([0, '+', 1, '-', 3], \
    {'+': '({0}, add, {1})', '-': '({0}, minus, {1})'})
    '(0, add, (1, minus, 3))'

    ++++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW:
    ++++++++++++++++++++++++++
    >>> build_repr([0, '+', 1, '+',2,'-', 3,'-',4,'-',5], {'+': '({0}, +, {1})\
', '-':'({0}, -, {1})'})
    '(0, +, (1, +, (2, -, (3, -, (4, -, 5)))))'

    >>> build_repr([0, '+', 1, '+',2,'+', 3,'-',4,'-',5,'+',6], {'+': '({0}, a\
dd, {1})', '-':'({0}, minus, {1})'})
    '(0, add, (1, add, (2, add, (3, minus, (4, minus, (5, add, 6))))))'

    >>> build_repr([0, '-', 1, '+',2,'-', 3,'+',4,'-',5,'+',6], {'+': '({0}, a\
dd, {1})', '-': '({0}, minus, {1})'})
    '(0, minus, (1, add, (2, minus, (3, add, (4, minus, (5, add, 6))))))'
    >>> build_repr(['0', '+', 1, '+',2,'-', 3,'-',4,'-',5], {'+': '({0}, +, {1})\
', '-':'({0}, -, {1})'})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> build_repr([0, '+', 1, '+',2,'-', 3,0,4,'-',5], {'+': '({0}, +, {1})\
', '-':'({0}, -, {1})'})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    length=len(operations)
    skip=2
    assert isinstance(operations,list) and isinstance(templates,dict)
    assert all(isinstance(operations[i],str) for i in range(1,length,skip))
    assert all(isinstance(operations[i],int) for i in range(0,length,skip))
    num=operations[0]
    if length==1:
        return str(num)
    else:
        op=operations[1]
        short_ops=operations[skip:]
        return templates[op].format(num,build_repr(short_ops,templates))
