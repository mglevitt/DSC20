"""
TODO: This will be the module docstring; please put the description 
of this module, or file, here as how it is done with the method 
docstrings
"""

# Question 1
def sum_two(x,y):
    """Return the result sum of x and y
    >>> sum_two(2,-2)
    0
    >>> sum_two(-100,150)
    50
    >>> sum_two(-10, -10)
    -20
    >>> sum_two(-3,9)
    6
    >>> sum_two(-5,23)
    18
    >>> sum_two(0,3)
    3
    """
    return x+y

# Question 2
def distance(x1,y1,x2,y2):
    """Return the distance between the points (float) 
    between (x1,y1) and (x2,y2)
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(-3, -4, 3, 4  )
    10.0
    >>> distance (100, 100, 100.5, 100)
    0.5
    >>> distance (10, 20, 40, 4)
    34.0
    >>> distance (0, 20, 9, 7)
    15.8
    >>> distance (-4, 9, 36, 4)
    40.3
    """
    return round(((x1-x2)**2+(y1-y2)**2)**(1/2),1)
    

# Question 3
def find_slope(x1, y1, x2, y2):
    """Return the slope of the line (float) between 
    points (x1,y1) and (x2,y2)
    >>> find_slope(0,0,5,5)
    1.0
    >>> find_slope(0, 0, 1 , 0.5)
    0.5
    >>> find_slope(1, 1, -1, -1)
    1.0
    >>> find_slope(0, 0, 1, 2)
    2.0
    >>> find_slope(2,3,6,19)
    4.0
    >>> find_slope(-3,9,0,1)
    -2.7
    >>> find_slope(8,-3,0,17)
    -2.5
    """
    if x2-x1==0:
        return 0.0
    else:
        return round((y2-y1)/(x2-x1),1)

# Question 4
def find_intercept(x1, y1, x2, y2):
    """Return y intercept of the line (float) between 
    points (x1,y1) and (x2,y2)
    >>> find_intercept(0, 0, 123, 123)
    0.0
    >>> find_intercept(-22, -55, 55, 22)
    -33.0
    >>> find_intercept(-20, 20, 30, 40)
    28.0
    >>> find_intercept(10,30,-10,-10)
    10.0
    >>> find_intercept(1,9,-80,34)
    9.3
    >>> find_intercept(14,20,18,-16)
    146.0
    """
    return round(y1-((y2-y1)/(x2-x1))*x1,1)

# Question 5
def is_triangle (x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    triangle. Returns False otherwise.
    >>> is_triangle(0, 0, 3, 0, 3, 4)
    True
    >>> is_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_triangle(-5, -5, 1, 2, -10, 15)
    True
    >>> is_triangle(-3,4,5,6,-4,9)
    True
    >>> is_triangle(0,0,32,6,-32,-6)
    False
    >>> is_triangle(0,-8,9,6,10,-2)
    True
    """
    if ((y2-y1)/(x2-x1))*x3 +y1-((y2-y1)/(x2-x1))*x1==y3:
        return False
    else:
        return True

# Question 6
def is_right_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) 
    form a right triangle. Returns False otherwise.
    >>> is_right_triangle(0, 0, 0, 3, 4, 0)
    True
    >>> is_right_triangle(0, 0, 0, 12, 5, 0)
    True
    >>> is_right_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_right_triangle(0, 0, 5, 5, 10, 10)
    False
    >>> is_right_triangle(0,2,0,7,5,2)
    True
    >>> is_right_triangle(9,8,0,-6,0,7)
    False
    >>> is_right_triangle(-6,9,8,-9,0,0)
    False
    """
    dis1=distance(x1,y1,x2,y2)
    dis2=distance(x1,y1,x3,y3)
    dis3=distance(x3,y3,x2,y2)
    if round(dis1**2+dis2**2)==round(dis3**2):
        return True
    elif round(dis1**2+dis3**2)==round(dis2**2):
        return True
    elif round(dis2**2+dis3**2)==round(dis1**2):
        return True
    else:
        return False


# Question 7

def is_equilateral_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    equilateral triangle. Returns False otherwise.
    >>> is_equilateral_triangle(2,1, 7,1 ,4.5, 5.33)
    True
    >>> is_equilateral_triangle(0, 0, 10, 0, 3, 4)
    False
    >>> is_equilateral_triangle(-5, -4, -2, -4, -3.5, -1.402)
    True
    >>> is_equilateral_triangle(-8, 9, 0, -7, 8, 0)
    False
    >>> is_equilateral_triangle(0, 5, -7, 8, 9, -2)
    False
    >>> is_equilateral_triangle(1, 1, 2, 2, 1.5, 2.5)
    False
    """
    dis1=distance(x1,y1,x2,y2)
    dis2=distance(x1,y1,x3,y3)
    dis3=distance(x3,y3,x2,y2)
    if dis1==dis2 and dis1==dis3:
        return True
    else:
        return False


# Question 8
def type_of_triangle(x1, y1, x2, y2, x3, y3):
    """Return the type of triangle formed by 
    points (x1,y1), (x2,y2)  and (x3,y3).
    >>> type_of_triangle(-5, -4, -2, -4, -3.5, -1.402)
    'Equilateral triangle'
    >>> type_of_triangle(0, 0, 0, 3, 4, 0)
    'Right triangle'
    >>> type_of_triangle(0, 0, 0, 12, 5, 0)
    'Right triangle'
    >>> type_of_triangle( 1, 2, 3, 4, -2, 6)
    'Simple triangle'
    >>> type_of_triangle( -3, -3, 0, 0, 3, 3)
    'Not a triangle'
    >>> type_of_triangle(-2, 4, 0, 3, -2, 7)
    'Simple triangle'
    >>> type_of_triangle(0, 5, 8, 5, 8, -3)
    'Right triangle'
    >>> type_of_triangle(4, 1, 14, 6, 24, 11)
    'Not a triangle'
    """
    if is_right_triangle(x1, y1, x2, y2, x3, y3)==True:
        return 'Right triangle'
    elif is_equilateral_triangle(x1, y1, x2, y2, x3, y3)==True:
        return 'Equilateral triangle'
    elif is_triangle (x1, y1, x2, y2, x3, y3)==False:
        return 'Not a triangle'
    else:
        return 'Simple triangle'

# Question 9:
def even_odd_list(lst1):
    """Return a new list indicating which replaces each 
    element of lst1 with "Even" or "Odd". See the doctest 
    examples for reference.
    >>> even_odd_list([1, 2, 3])
    ['Odd', 'Even', 'Odd']
    >>> even_odd_list([5, 8, 9, 10, 12])
    ['Odd', 'Even', 'Odd', 'Even', 'Even']
    >>> even_odd_list([-5, -1, -3])
    ['Odd', 'Odd', 'Odd']
    >>> even_odd_list([-2, 3, 11])
    ['Even', 'Odd', 'Odd']
    >>> even_odd_list([8,3,2,7,-9,0])
    ['Even', 'Odd', 'Even', 'Odd', 'Odd', 'Even']
    >>> even_odd_list([4,7,5])
    ['Even', 'Odd', 'Odd']
    >>> even_odd_list([0])
    ['Even']
    """
    lis=list()
    for i in lst1:
        if int(i/2)==i/2:
            lis.append('Even')
        else:
            lis.append('Odd')
    return lis



# Question 10
def party (guests):
    """Scans the guests of the event. If the # of people who 
    want to party (42's) is equal to or above 50%, 
    returns "There is a party!". Otherwise returns 
    "No party this time".

    >>> party([0,1,42,42,42,13,6,5])
    'No party this time'
    >>> party([0,1,42,42,42,42,6,7])
    'There is a party!'
    >>> party([0,42,6,42,42,7,66,12,13,42,42,42])
    'There is a party!'
    >>> party([0,1,42,5,6,42,42,42,5])
    'No party this time'
    >>> party([3,42,42,5,7,9,42,5,42])
    'No party this time'
    >>> party([9,2,42,9,42,9,42,42,42])
    'There is a party!'
    >>> party([3,2,9,8,4,2,4,2,42])
    'No party this time'
    """
    count=0
    for i in guests:
        if i==42:
            count=count+1
    if count>=len(guests)/2:
        return 'There is a party!'
    else:
        return 'No party this time'
    
