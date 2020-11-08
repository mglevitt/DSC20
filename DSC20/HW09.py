"""
DSC 20 HW 09
NAME: Maxwell Levitt
PID: A157881
"""

## Question 1 ##

def checkingInputs(input1, input2, input3):
    """
    You will be handling 3 basic checks
    - are all the input types correct
    - does input2 exist within input3
    - can you divide input1 by input3

    >>> checkingInputs(15, 'key1', {'key1': 5, 'key2': 10})
    3.0

    >>> checkingInputs(15, 'key1', {'key1': 0, 'key2': 10})
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Cannot divide 15 by 0

    >>> checkingInputs(15, 'key1', {'key2': 10})
    Traceback (most recent call last):
    ...
    KeyError: 'Cannot find key1 in the dictionary'

    >>> checkingInputs("15", 2810, ['key2', 10])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> checkingInputs(8,'k1',{'k0':0,'k1':1})
    8.0
    >>> checkingInputs('8','k0',{'k0':0,'k1':1})
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type
    >>> checkingInputs(8,'k0',{'k0':0,'k1':1})
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Cannot divide 8 by 0
    """
    if not (isinstance(input1,int) and isinstance(input2,str)):
        raise TypeError('Inputs are not the correct type')
    elif not isinstance(input3,dict):
        raise TypeError('Inputs are not the correct type')
    else:
        try:
            return input1/input3[input2]
        except KeyError:
            raise KeyError('Cannot find {0} in the dictionary'.format(input2))
        except ZeroDivisionError:
            o=input1
            t=input2
            th=input3
            raise ZeroDivisionError('Cannot divide {0} by {1}'.format(o,th[t]))


## Question 2 ##

def loadFile(filename):
    """
    >>> loadFile("file1.txt")
    'File loaded'

    >>> loadFile("file2.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: file2.txt does not exist

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> loadFile("doc_food.txt")
    'File loaded'

    >>> loadFile("docs.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: docs.txt does not exist
    >>> loadFile("docers.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: docers.txt does not exist
    """
    try:
        open(filename,'r')
        return 'File loaded'
    except FileNotFoundError:
        raise FileNotFoundError('{} does not exist'.format(filename))


## Question 3.1 ##

def recursive_triangle(n):
    """
    Creates a triangle structure with * characters. The triangle has n
    levels, each level has one more element than the previous. n is a
    positive integer, no validation is required.
    Parameters: n (int), positive integer
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(recursive_triangle(1))
    *
    >>> print(recursive_triangle(2))
    *
    **
    >>> print(recursive_triangle(3))
    *
    **
    ***

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(recursive_triangle(4))
    *
    **
    ***
    ****
    >>> print(recursive_triangle(6))
    *
    **
    ***
    ****
    *****
    ******
    >>> print(recursive_triangle(10))
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    """
    if n==1:
        return '*'
    else:
        return recursive_triangle(n-1)+'\n'+'*'*n


## Question 3.2 ##

def triangle_patterns(n, pattern_count):
    """
    Creates a triangle pattern with * characters. Each triangle has n
    levels, there are pattern_count total triangles. All inputs are
    positive integers, no input validation required.
    Parameters: n, pattern count (int), positive integers
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(triangle_patterns(3, 1))
    *
    **
    ***
    >>> print(triangle_patterns(3, 2))
    *
    **
    ***
    ***
    **
    *
    >>> triangle_patterns(3, 3)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***'
    >>> triangle_patterns(3, 4)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***\\n***\\n**\\n*'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(triangle_patterns(1, 1))
    *
    >>> print(triangle_patterns(10, 10))
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    **********
    *********
    ********
    *******
    ******
    *****
    ****
    ***
    **
    *
    >>> print(triangle_patterns(2, 5))
    *
    **
    **
    *
    *
    **
    **
    *
    *
    **
    """
    def op_recursive_tri(n):
        """This function is a recursive function that flips the pattern 
        created by recursive_triangle upside down"""
        if n==1:
            return '*'
        else:
            return '*'*n+'\n'+op_recursive_tri(n-1)
    even=2
    if pattern_count==1:
        return recursive_triangle(n)
    elif pattern_count%even==0:
        return triangle_patterns(n,pattern_count-1)+'\n'+op_recursive_tri(n)
    else:
        return triangle_patterns(n,pattern_count-1)+'\n'+recursive_triangle(n)


## Question 4 ##

## This question's implementation will be done in hw09_card.py

## Question 5.1 ##

def full_triangle(n, space_count = 0):
    """
    Creates a triangle structure as shown in the doctests. The triangles have
    n - 1 levels. space_count is a helper variable used to help with spacing
    of the triangle. Assume n >= 2, and space_count >= 0. All inputs are
    integers. No input validation is required.
    Parameters: n, space count (int), integers. n >= 1, space_count >= 0.
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
    >>> print(full_triangle(2)) # The smallest value we can have
    OO
    >>> print(full_triangle(3))
    -OO-
    OOOO
    >>> print(full_triangle(5))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> full_triangle(6)
    '----OO----\\n---OOOO---\\n--OOOOOO--\\n-OOOOOOOO-\\nOOOOOOOOOO'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(full_triangle(4)) 
    --OO--
    -OOOO-
    OOOOOO
    >>> print(full_triangle(6))
    ----OO----
    ---OOOO---
    --OOOOOO--
    -OOOOOOOO-
    OOOOOOOOOO
    >>> print(full_triangle(10))
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    """
    base=2
    check=-1
    if n==base:
        return '-'*space_count+'O'*n+'-'*space_count
    elif space_count==check:
        return 'O'*(n-1)*base
    else:
        s=space_count
        f=full_triangle
        return f(n-1,space_count=s+1)+'\n'+'-'*s+f(n,space_count=check)+'-'*s
    

## Question 5.2 ##

def diamond_patterns(n, pattern_count, space_count = 0):
    """
    Assume n >= 2, pattern_count >= 1 and space_count >= 0. All inputs are
    integers. No assertion required.
    >>> print(diamond_patterns(2,1))
    OO
    >>> print(diamond_patterns(2,2))
    OO
    OO
    >>> print(diamond_patterns(5,1))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> diamond_patterns(4,2)
    '--OO--\\n-OOOO-\\nOOOOOO\\nOOOOOO\\n-OOOO-\\n--OO--'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(diamond_patterns(3,3))
    -OO-
    OOOO
    OOOO
    -OO-
    -OO-
    OOOO
    >>> print(diamond_patterns(4,4))
    --OO--
    -OOOO-
    OOOOOO
    OOOOOO
    -OOOO-
    --OO--
    --OO--
    -OOOO-
    OOOOOO
    OOOOOO
    -OOOO-
    --OO--
    >>> print(diamond_patterns(10,10))
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOO
    -OOOOOOOOOOOOOOOO-
    --OOOOOOOOOOOOOO--
    ---OOOOOOOOOOOO---
    ----OOOOOOOOOO----
    -----OOOOOOOO-----
    ------OOOOOO------
    -------OOOO-------
    --------OO--------
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOO
    -OOOOOOOOOOOOOOOO-
    --OOOOOOOOOOOOOO--
    ---OOOOOOOOOOOO---
    ----OOOOOOOOOO----
    -----OOOOOOOO-----
    ------OOOOOO------
    -------OOOO-------
    --------OO--------
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOO
    -OOOOOOOOOOOOOOOO-
    --OOOOOOOOOOOOOO--
    ---OOOOOOOOOOOO---
    ----OOOOOOOOOO----
    -----OOOOOOOO-----
    ------OOOOOO------
    -------OOOO-------
    --------OO--------
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOO
    -OOOOOOOOOOOOOOOO-
    --OOOOOOOOOOOOOO--
    ---OOOOOOOOOOOO---
    ----OOOOOOOOOO----
    -----OOOOOOOO-----
    ------OOOOOO------
    -------OOOO-------
    --------OO--------
    --------OO--------
    -------OOOO-------
    ------OOOOOO------
    -----OOOOOOOO-----
    ----OOOOOOOOOO----
    ---OOOOOOOOOOOO---
    --OOOOOOOOOOOOOO--
    -OOOOOOOOOOOOOOOO-
    OOOOOOOOOOOOOOOOOO
    OOOOOOOOOOOOOOOOOO
    -OOOOOOOOOOOOOOOO-
    --OOOOOOOOOOOOOO--
    ---OOOOOOOOOOOO---
    ----OOOOOOOOOO----
    -----OOOOOOOO-----
    ------OOOOOO------
    -------OOOO-------
    --------OO--------
    """
    def op_full_tri(n, space_count = 0):
        """This function is a recursive function that flips the pattern 
        created by full_triangle upside down"""
        base=2
        check=-1
        if n==base:
            return '-'*space_count+'O'*n+'-'*space_count
        elif space_count==check:
            return 'O'*(n-1)*base
        else:
            s=space_count
            f=op_full_tri
            c=check
            return '-'*s+f(n,space_count=c)+'-'*s+'\n'+f(n-1,space_count=s+1)
    even=2
    if pattern_count==1:
        return full_triangle(n)
    elif pattern_count%even==0:
        return diamond_patterns(n,pattern_count-1)+'\n'+op_full_tri(n)
    else:
        return diamond_patterns(n,pattern_count-1)+'\n'+full_triangle(n)