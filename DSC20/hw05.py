"""
DSC 20 HW 05
NAME: Maxwell Levitt
PID: A15788481
"""

from functools import reduce

# Question 1.1:
def question1_1():
    """Return a list with answers to the True/False questions.
    >>> out = question1_1()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, bool) for i in out])
    True
    """
    return [True,False,False,True,False,False,True,True,True,True]
    
# Question 1.2:
def question1_2():
    """Return a list with answers to the code complexity questions.
    >>> out = question1_2()
    >>> type(out) == list
    True
    >>> len(out)
    15
    >>> all([isinstance(i, int) and i<=7 and i>=1 for i in out])
    True
    """
    return [3,6,2,2,5,5,5,6,2,2,2,5,3,4,5]
    
# Question 2.1:
def make_id(name, suffix):
    """Returns a netid for name with suffix n.
    >>> make_id('Marina Aleksandrovna Langlois', 17)
    'mal17'
    >>> make_id('Donald Trump', "boss")
    'dtboss'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> make_id('Howie Tanner LaRiviere', 'legend')
    'htllegend'
    >>> make_id('Charles Beaner Yeganeh', 'illegal')
    'cbyillegal'
    >>> make_id('Andrew Hurricane Mohkhtarzadeh', 22)
    'ahm22'
    """
    out=''
    lst=name.split(' ')
    for i in lst:
        out+=i[0].lower()
    out+=str(suffix)
    return out
    
# Question 2.2:
def do_you_have_me(dic, item):
    """Returns a key for which item exists
    otherwise returns "Not there"
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9)
    'Not there'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 1)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 4)
    'key1'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> do_you_have_me({"key1":[1,2,3,4,9,10], "key2": [5,4,7,10,8]}, 10)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8],"key3":[9,2,8,203,\
4], "key4": [25,41,7,8,13,18]}, 18)
    'key4'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 21)
    'Not there'
    """
    d={}
    for i in dic.items():
        for j in i[1]:
            if j not in d:
                d.update({j:i[0]})
    if item in d:
        return d[item]
    else:
        return 'Not there'        
    
# Question 2.3:
def read_menus(food_cat, *menus):
    """Return a string that summarized amount of items from the same category
    in the menus.
    >>> read_menus("food_cat.txt", "menu1.txt", "menu2.txt")
    'There are 7 burgers, 4 salads and 5 desserts'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> read_menus("doc_food.txt", "menu1.txt", "menu2.txt","doc_menu_1.txt",\
"doc_menu_2.txt")
    'There are 17 burgers, 10 salads and 9 desserts'
    >>> read_menus("doc_food.txt","doc_menu_1.txt","doc_menu_2.txt")
    'There are 10 burgers, 6 salads and 4 desserts'
    >>> read_menus("doc_food.txt","doc_menu_1.txt")
    'There are 3 burgers, 4 salads and 3 desserts'
    """
    dic={}
    bur=0
    sal=0
    des=0
    item=''
    food=''
    lines=[]
    f=open(food_cat,'r')
    for line in f:
        words=line.strip().split(':')
        dic.update({words[0].strip():words[1].strip()})
    f.close()
    for file in menus:
        f=open(file,'r')
        lines=f.read().split('\n')
        for line in lines:
            item=line.strip().split(':')[0].strip()
            if item in dic:
                food=dic[item]
                if food=='Burger':
                    bur+=1
                elif food=='Salad':
                    sal+=1
                elif food=='Dessert':
                    des+=1
        f.close()
    return 'There are {} burgers, {} salads and {} desserts'.format(bur,sal,des)
    
# Question 2.4
def cuboid_coordinates(x, y, z, n):
    """
    Return a list of all possible coordinates (i, j, k)
    such that i + j + k is not equal to n.

    Restrictions: Your solution must be one line.

    >>> cuboid_coordinates(1, 1, 1, 2)
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cuboid_coordinates(1, 2, 3, 3)
    [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 3), (0, 2, \
0), (0, 2, 2), (0, 2, 3), (1, 0, 0), (1, 0, 1), (1, 0, 3), (1, 1, 0), (1, 1, \
2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, 3)]
    >>> cuboid_coordinates(2, 2, 2, 2)
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (0, 2, 2), (1, 0, \
0), (1, 0, 2), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, \
1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]
    >>> cuboid_coordinates(3, 3, 3, 3)
    [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 3), (0, 2, \
0), (0, 2, 2), (0, 2, 3), (0, 3, 1), (0, 3, 2), (0, 3, 3), (1, 0, 0), (1, 0, \
1), (1, 0, 3), (1, 1, 0), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), (1, 2, \
3), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 3), (2, 0, 0), (2, 0, 2), (2, 0, \
3), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 2, 0), (2, 2, 1), (2, 2, 2), (2, 2, \
3), (2, 3, 0), (2, 3, 1), (2, 3, 2), (2, 3, 3), (3, 0, 1), (3, 0, 2), (3, 0, \
3), (3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 2, 0), (3, 2, 1), (3, 2, \
2), (3, 2, 3), (3, 3, 0), (3, 3, 1), (3, 3, 2), (3, 3, 3)]
    """
    return [(i, j, k) for i in range(x+1) for j in range(y+1) for k in \
range(z+1) if i+j+k!=n]
    
# Question 2.5
def k_mapping(inp, k):
    """
    Maps each element in the circular list to the
    element k spaces in front of it.

    >>> k_mapping([1, 2, 3, 4, 5], 2)
    '1 -> 3, 3 -> 5, 5 -> 2, 2 -> 4, 4 -> 1'
    >>> k_mapping([1, 2, 3], 3)
    '1 -> 1, 2 -> 2, 3 -> 3'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> k_mapping([1, 2, 3, 4, 5,6,7,8,9,10,11,12], 1)
    '1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5, 5 -> 6, 6 -> 7, 7 -> 8, 8 -> 9, 9 -> 10, \
10 -> 11, 11 -> 12, 12 -> 1'
    >>> k_mapping([1, 2, 3, 4, 5,6,7,8,9,10,11], 5)
    '1 -> 6, 6 -> 11, 11 -> 5, 5 -> 10, 10 -> 4, 4 -> 9, 9 -> 3, 3 -> 8, 8 -> \
2, 2 -> 7, 7 -> 1'
    >>> k_mapping([1, 2, 3, 4, 5,6,7,8,9,10], 25)
    '1 -> 6, 6 -> 1, 1 -> 6, 6 -> 1, 1 -> 6, 6 -> 1, 1 -> 6, 6 -> 1, 1 -> 6, \
6 -> 1'
    """
    out=''
    count=0
    in1=0
    in2=0
    end=2
    while count<len(inp):
        in2=in1+k
        while in2>=len(inp):
            in2-=len(inp)
        out+=str(inp[in1])+' -> '+str(inp[in2])+', '
        if in1==in2:
            in1+=1
        else:
            in1=in2
        count+=1
    return out[:len(out)-end]
    
# Question 2.6
def gcd_fraction(frac_lst):
    """
    Returns the reduced fraction made by multiplying
    fractions in frac_lst. The first element of each
    tuple represents the numerator and the second
    element represents the denominator.

    Restrictions: No loops or maps outside the gcd inner function.
    Must use reduce.

    >>> gcd_fraction([(1, 2), (3, 4), (10, 6)])
    (5, 8)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> gcd_fraction([(12, 7), (2, 8), (19, 24),(13,23),(1,6)])
    (247, 7728)
    >>> gcd_fraction([(2, 2), (4, 4), (9, 9),(1,1)])
    (1, 1)
    >>> gcd_fraction([(7, 3), (2, 4), (10, 8),(9,4),(20,5)])
    (105, 8)
    """
    
    def gcd(x, y):
        """
        Find the greatest common divisor between x and y.
        """
        while y!=0:
            t=y 
            y=x%y 
            x=t 
        return x
    return reduce(lambda x,y:(int(x[0]*y[0]/gcd(x[0]*y[0],x[1]*y[1])),\
int(x[1]*y[1]/gcd(x[0]*y[0],x[1]*y[1]))),frac_lst)
