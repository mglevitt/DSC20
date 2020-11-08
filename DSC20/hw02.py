"""
DSC 20 HW 02
NAME:Maxwell Levitt
PID:A15788481
"""

## Question 1 ##

def convert_1(path):
    """
    Read a file that contains pairs of name and company and convert these
    pairs to a list of tuples.

    >>> convert_1('tests/q1_test1.txt')
    [('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'), ('Aaron', 'Apple'), \
('Judy', 'Microsoft'), ('Judy', 'Facebook')]
    >>> convert_1('tests/q1_test2.txt')
    [('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley', 'SoftBank'), \
('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'), ('Wesley', 'AT&T'), \
('Xiang', 'SoftBank'), ('Aaron', 'TMobile')]
    >>> convert_1('tests/q1_test3.txt')
    [('David', 'Intel'), ('David', 'Amazon'), ('Judy', 'Intel'), \
('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron', 'Amazon'), \
('Xiang', 'Amazon'), ('Wesley', 'Amazon')]
    >>> convert_1('tests/q1_test4.txt')
    [('Josh', 'BlueOrange'), ('Jeff', 'Slalom'), ('Mindy', 'Microsoft'), \
('Hannah', 'Slalom')]
    >>> convert_1('tests/q1_test5.txt')
    [('Ted', 'Amazon'), ('Bill', 'Apple'), ('Steve', 'Microsoft'), \
('Liz', 'Amazon'), ('Eric', 'Boeing')]
    >>> convert_1('tests/q1_test6.txt')
    []
    """
    lst=[]
    a=open(path,'r')
    txt=a.read()
    for i in txt.splitlines():
        tup=tuple(i.split())
        lst.append(tup)
    return lst

## Question 2 ##

def convert_2(lst):
    """
    Convert the given list of tuples that contain pairs of names and companies
    to a dictionary that has companies as keys and names that pairs with
    these companies as values.

    >>> convert_2([('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'),\
    ('Aaron', 'Apple'), ('Judy','Microsoft'), ('Judy', 'Facebook')])
    {'Microsoft': ['Wesley', 'Aaron', 'Judy'], 'Apple': ['Aaron'], \
'Facebook': ['Judy']}
    >>> convert_2([('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley',\
    'SoftBank'), ('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'),\
    ('Wesley', 'AT&T'), ('Xiang', 'SoftBank'), ('Aaron', 'TMobile')])
    {'TMobile': ['Owen', 'Aaron'], 'AT&T': ['Aaron', 'Wesley'], \
'SoftBank': ['Wesley', 'Xiang'], 'Qualcomm': ['Owen', 'Xiang']}
    >>> convert_2([('David', 'Intel'), ('David', 'Amazon'), ('Judy',\
    'Intel'), ('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron',\
    'Amazon'), ('Xiang', 'Amazon'), ('Wesley', 'Amazon')])
    {'Intel': ['David', 'Judy'], 'Amazon': ['David', 'Judy', 'Aaron', \
'Xiang', 'Wesley'], 'AMD': ['Judy']}
    >>> convert_2([('Josh', 'BlueOrange'), ('Jeff', 'Slalom'), \
('Mindy', 'Microsoft'), ('Hannah', 'Slalom')])
    {'BlueOrange': ['Josh'], 'Slalom': ['Jeff', 'Hannah'], 'Microsoft': \
['Mindy']}
    >>> convert_2([('Ted', 'Amazon'), ('Bill', 'Apple'), \
('Steve', 'Microsoft'), ('Liz', 'Amazon'), ('Eric', 'Apple')])
    {'Amazon': ['Ted', 'Liz'], 'Apple': ['Bill', 'Eric'], 'Microsoft': \
['Steve']}
    >>> convert_2([])
    {}
    """
    dic={}
    for i in lst:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else:
            temp={i[1]:[i[0]]}
            dic.update(temp)
    return dic

## Question 3 ##

MAX_N = 9

def multiplication_chart(n):
    """
    Create a triangle multiplication chart with given size. n will be positive
    integers only. If 1 <= n <= 9, create the chart normally. If n > 9, add
    a notice before creating a chart with n = 9. See the write-up for detailed
    description.

    >>> print(multiplication_chart(3))
    01
    02  04
    03  06  09
    >>> print(multiplication_chart(6))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    >>> print(multiplication_chart(10))
    n = 10 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(7))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    >>> print(multiplication_chart(100))
    n = 100 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(9))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(1))
    01
    """
    limit=9
    strng=''
    num=0
    final=''
    if n>limit:
        a=limit
        final='n = '+str(n)+' is too hard for me! Why not have n = 9?\n'
    else:
        a=n
    for i in range(a):
        for j in range(i+1):
            num='{:0>2}'.format((i+1)*(j+1))
            if j==0:
                strng=strng+str(num)
            else:
                strng=strng+'  '+str(num)
        if i==a-1:
            final=final+strng
        else:
            final=final+strng+'\n'
            strng=''
    return final


## Question 4 ##

LEN_ALPHABET = 26

def encrypt(s):
    """
    Encrypt the string by capitalizing all letters, applying Atbash cipher,
    and reverse the string. See the write-up for detailed description.

    >>> encrypt('ABCDefg, HIJKlmn, opqRST, uvwXYZ')
    'ABCDEF ,GHIJKL ,MNOPQRS ,TUVWXYZ'
    >>> encrypt('encrypt encrypt?')
    '?GKBIXMV GKBIXMV'
    >>> encrypt('CsE BaSeMeNt >.<')
    '<.> GMVNVHZY VHX'
    >>> encrypt('Uwk iuhbiy687^%5be ,fjbiasUYEbdybT {une},I')
    'R,}VMF{ GYBWYVBFHZRYQU, VY5%^786BRYSFR PDF'
    >>> encrypt('Data Science is Cool!')
    '!OLLX HR VXMVRXH ZGZW'
    >>> encrypt('eibYTweubibbyuYEV$ hegfsuvby(*vbew  uehiu)[wjifrunui)(87h)]')
    '])S78()RFMFIURQD[)FRSVF  DVYE*(BYEFHUTVS $EVBFBYYRYFVDGBYRV'
    """
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
    'R','S','T','U','V','W','X','Y','Z']
    atbash={}
    for i in range(LEN_ALPHABET):
        temp={alpha[i]:alpha[LEN_ALPHABET-1-i]}
        atbash.update(temp)
    a=s[::-1]
    b=a.upper()
    c=''
    l=''
    for i in b:
        if i in atbash:
            l=atbash[i]
            c=c+l
        else:
            c=c+i
    return c



## Question 5 ##

def sum_some(lst1, num):
    """
    Splits lst1 into subgroups of (equal) size num, and sums the contents \
    of each subgroup. Returns the individual sums in a new list. If splitting \
    can't be done properly, returns "split not valid"

    >>> sum_some([1, 2, 3, 4, 5, 6], 2)
    [3, 7, 11]
    >>> sum_some([1, 2, 3, 4, 5, 6], 3)
    [6, 15]
    >>> sum_some([1,2,3,4,5,6,7], 3)
    'split not valid'
    >>> sum_some([1,2], 3)
    'split not valid'
    >>> sum_some([3,5,7,1,2,4,5,9,2],3)
    [15, 7, 16]
    >>> sum_some([2,7,1,7,3,3,6,2],4)
    [17, 14]
    >>> sum_some([1,5,2,3],1)
    [1, 5, 2, 3]
    >>> sum_some([2,5,1,9,4],7)
    'split not valid'
    """
    sums=[]
    sum=0
    lst=[]
    total=0
    a=len(lst1)/num
    if int(a)==a:
        for i in range(int(a)):
            lst=lst1[i*num:(i+1)*num]
            total=0
            for j in lst:
                total=total+j
            sums.append(total)
        return sums
    else:
        return 'split not valid'

## Question 6 ##

def subset(lst1, lst2):
    """
    Returns True if lst1 is a subset of lst2. Returns False otherwise.

    >>> subset([1,2], [1,2,3])
    True
    >>> subset([1,2,3,4], [1,2,3])
    False
    >>> subset([], [1])
    True
    >>> subset([1,2,3], [1,2,3])
    True
    >>> subset([1], [])
    False
    >>> subset([3,5,7], [1,3,5,7,9])
    True
    >>> subset([1,2,3,4,5,6], [1,2,3,4,5,7,8,9])
    False
    >>> subset([], [])
    True
    """
    sub=True
    new_lst=[]
    for i in lst1:
        if i in new_lst:
            return False
        new_lst.append(i)
        if sub==True:
            if i in lst2:
                sub=True
            else:
                return False
        else:
            return False
    return True
