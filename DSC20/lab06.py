# Question 1
def question1(num_list):
    """
    >>> question1([1,2,3,4,5,6,7,8,9,10])
    2 4 6 8 10 
    >>> result = question1([1,3,5,7,9])
    >>> print(result)
    None
    >>> question1([1,3,5,7,9, 0])
    0 
    """
    if len(num_list)>0:
        if num_list[0]%2==0:
            print(str(num_list[0]),end=' ')
        question1(num_list[1:])
        
    
# Question 2
def question2(words_list):
    """ Counts the number of "SOS" occurrences in a list
    >>> question2(["SOS", "Not SOS", "SOS", "Not SOS"])
    2
    >>> question2(["SOS", "Alarm", "Help"])
    1
    >>> question2(["Alarm", "Help", "Fire", "Not SOS"])
    0
    >>> question2(["SOS", "SOS", "SOS", "SOS"])
    4
    >>> question2([])
    0
    """    
    if len(words_list)>0:
        if words_list[0]=='SOS':
            return 1+question2(words_list[1:])
        return question2(words_list[1:])
    else:
        return 0

# Question 3
def question3(number):
    """
    >>> question3(123456)
    21
    >>> question3(123)
    6
    >>> question3(123908)
    23
    >>> question3(5)
    5
    """
    if number>0:
        return (number%10)+question3(number//10)
    else:
        return 0
        
# Question 4
def question4(string):
    """
    >>> question4("Recursion is cool.")
    'Recursion is cool'
    >>> question4("M.A.R.I.N.A.")
    'MARINA'
    >>> question4("No dots here!")
    'No dots here!'
    """
    if len(string)>0:
        if string[0]!='.':
            return string[0]+question4(string[1:])
        else:
            return question4(string[1:])
    else:
        return ''
        
# Question 5
def question5(number):
    """
    >>> question5(1181)
    4
    >>> question5(181)
    2
    >>> question5(11911)
    6
    >>> question5(111111)
    11
    """
    if number>0:
        if number%100==11:
            return 2+question5(number//10)
        elif number%10==1:
            return 1+question5(number//10)
        else:
            return question5(number//10)
    else:
        return 0

# Question 6
def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(int(n))
    if n!=1:
        if n%2==0:
            return 1+hailstone(n/2)
        else:
            return 1+hailstone(n*3+1)
    else:
        return 1
    
        
    
# Question 7
def question7(int1, int2):
    """
    >>> question7(8, 1)
    '8 7 6 5 4 3 2 1'
    >>> question7(1, -1)
    '1 0 -1'
    >>> question7(10, 10)
    '10'
    """
    if int1>int2:
        return str(int1)+' '+question7(int1-1,int2)
    else:
        return str(int2)

# Question 8
def question8(int1, int2):
    """
    >>> question8(8, 1)
    '8 7 6 5 4 3 2 1'
    >>> question8(1, -1)
    '1 0 -1'
    >>> question8(10, 10)
    '10'
    >>> question8(1, 8)
    '1 2 3 4 5 6 7 8'
    >>> question8(-1, 1)
    '-1 0 1'
    """
    if int1>int2:
        return str(int1)+' '+question8(int1-1,int2)
    elif int1<int2:
        return str(int1)+' '+question8(int1+1,int2)
    else:
        return str(int2)
