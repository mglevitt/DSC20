"""
DSC 20 HW 03
NAME: Maxwell Levitt
PID: A15788481
"""

from math import isclose

## Question 1 ##

def order_scores(student_ids, student_scores, student_hours_worked):
    """
    Orders elements of student_ids, student_scores, and student_hours_worked,
    according to the contents of student_scores (descending order)

    >>> order_scores(['Work','Hard','Get','A'],[100, 80, 90, 70],[10,12,13,10])
    {'Work': (100, 10), 'Get': (90, 13), 'Hard': (80, 12), 'A': (70, 10)}
    >>> order_scores(['A1','A2','A3'],[90, 27, 56],[9,10, 6])
    {'A1': (90, 9), 'A3': (56, 6), 'A2': (27, 10)}
    >>> order_scores(['A1','A2','A3'],[90.4, 27],[9,10, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['A1','A2','A3'],[90, 27, 80],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> order_scores(['Data','Is','Pretty','Cool'],[30,45,12,78],[3,2,5,0])
    {'Cool': (78, 0), 'Is': (45, 2), 'Data': (30, 3), 'Pretty': (12, 5)}
    >>> order_scores([5,'The','Man'],[1,2,3],[10,11,12])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['AAA','BBB','CCC'],[34,74,87,3],[0,3,1])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert len(student_ids)==len(student_scores)
    assert len(student_ids)==len(student_hours_worked)
    for i in student_ids:
        assert type(i)==str
    for i in student_scores:
        assert type(i)==int
    for i in student_hours_worked:
        assert type(i)==int
    tup=[]
    dic={}
    temp_lst=[]
    temp_dic={}
    lst=[]
    for i in range(len(student_ids)):
        temp_lst=[student_ids[i],student_scores[i],student_hours_worked[i]]
        lst.append(temp_lst)
    lst=sorted(lst,key=lambda lst:lst[1],reverse=True)
    for i in lst:
        tup=tuple([i[1],i[2]])
        temp_dic={i[0]:tup}
        dic.update(temp_dic)
    return dic

        ## Question 2 ##

def word_length_count(book):
    """
    Returns a dictionary containing the count of each length of word
    E.g. how many words total of length 1, 2, 3...?

    This function takes in a string book, which is a file name
    string. The function reads the file with the argument string
    and returns a dictionary where the keys are the length of words
    and the values are the number of words of that length. The keys
    should be sorted in ascending order.

    >>> word_length_count('War_and_Peace_no_punc.txt')[6]
    48342
    >>> word_length_count('War_and_Peace_no_punc.txt')[15]
    254
    >>> word_length_count('War_and_Peace_no_punc.txt')[23]
    2

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> word_length_count('War_and_Peace_no_punc.txt')[1]
    14932
    >>> word_length_count('War_and_Peace_no_punc.txt')[12]
    2986
    >>> word_length_count('War_and_Peace_no_punc.txt')[20]
    8

    """
    txt=open(book,'r',encoding='utf-8')
    dic={}
    final_dic={}
    temp={}
    for line in txt:
        for word in line.split():
            if len(word)!=0 and type(word)==str:
                if len(word) in dic:
                    dic[len(word)]+=1
                else:
                    dic[len(word)]=1
    for key in sorted(dic.keys()):
        temp={key:dic[key]}
        final_dic.update(temp)

    return final_dic

## Question 3 ##

def counting_spaces(list_of_strings):
    """
    >>> test = ["s t r i n g ", 'nospace', 'one space']
    >>> counting_spaces(test)
    [True, True, 1]

    >>> test2 = ["two spac es", "thr ee spa ces", "nospaces"]
    >>> counting_spaces(test2)
    [2, True, True]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> test = []
    >>> counting_spaces(test)
    []

    >>> test = "s t r i n g "
    >>> counting_spaces(test)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> test = [8, 'big guy', 'needs some space']
    >>> counting_spaces(test)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    divisor=3
    assert type(list_of_strings)==list
    assert all(isinstance(i,str) for i in list_of_strings)
    lst=[len(i.split(' '))-1 for i in list_of_strings]
    return [True if int(i/divisor)==i/divisor else i for i in lst]


## Question 4 ##

def create_trigrams(input_file, starting_words, num_words):
    """read in the input text, create a dictionary of trigrams, generate
    a new story based on the sequence of words starting a pair of words

    >>> create_trigrams("data/sherlock_small.txt", "one night", 10)
    'one night it was on the twentieth of march 1888'

    >>> create_trigrams("data/sherlock_small.txt", "i was", 10)
    'i was returning from a journey to a patient for'

    >>> create_trigrams("data/sherlock_small.txt", "Holmes Sherlock", 10)
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_trigrams("data/sherlock_small.txt", "which had", 10)
    'which had formerly been in part my own '

    >>> create_trigrams("data/sherlock_small.txt", "i rang", 2)
    'i rang'

    >>> create_trigrams("data/sherlock_small.txt", 'one night', 100)
    'one night it was on the twentieth of march 1888 i was returning from a \
journey to a patient for i had now returned to civil practice when my way \
led me through baker street as i passed the well remembered door which \
must always be associated in my mind with my wooing and with the dark \
incidents of the study in scarlet i became seized with a keen desire \
to see holmes again and to know how he was employing his \
extraordinary powers his rooms were brilliantly lit and even when i \
looked up i saw his tall spare'
    """
    assert type(num_words)==int
    assert type(starting_words)==str
    assert starting_words.lower()==starting_words
    file=open(input_file,'r')
    start_words_index=2
    temp={}
    dic={}
    words=[]
    lines=[]
    for i in file:
        lines=i.lower().split('\n')
    for i in lines:
        line=i.split(' ')
        words.extend(line)
    for i in range(len(words)-start_words_index):
        temp={words[i]+' '+words[i+1]:words[i+start_words_index]}
        dic.update(temp)
    string=starting_words
    lst=[]
    assert starting_words in dic
    for i in range(num_words-start_words_index):
        lst=string.split(' ')
        if lst[i]+' '+lst[i+1] in dic:
            string=string+' '+dic[lst[i]+' '+lst[i+1]]
        else:
            break
    return string
    
## Question 5 ##

DELTA = 0.0001

def newton_sqrt(n):
    """
    >>> newton_sqrt(4)
    1
    >>> newton_sqrt(1)
    5
    >>> newton_sqrt(2)
    4

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> newton_sqrt(11)
    5
    >>> newton_sqrt(0)
    1
    >>> newton_sqrt(458)
    8
    """
    count=1
    half=1/2
    squared=2
    guess=n*half
    while isclose(n,(guess)**squared,abs_tol=DELTA)==False:
        count+=1
        guess=half*(guess+(n/guess))
    return count



## Question 6.1 ##

B = 'O'
W = ' '

def list_to_pixel(file_path, filename):
    """
    >>> list_to_pixel("data/list0.txt","graph.txt")
    >>> with open ("graph.txt", "r") as f:
    ...     print(f.readline())
      OOOO  
    <BLANKLINE>
    >>> f1 = open("expected_graph.txt", "r")
    >>> f2 = open("graph.txt", "r")
    >>> f1.read() == f2.read()
    True
    >>> f1.close()
    >>> f2.close()

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> list_to_pixel("doc_list_1.txt","doc_graph_1.txt")
    >>> with open ("doc_graph_1.txt", "r") as f:
    ...     print(f.readline())
    OO    OOOOOOO  
    <BLANKLINE>
    >>> list_to_pixel("doc_list_2.txt","doc_graph_2.txt")
    >>> with open ("doc_graph_2.txt", "r") as f:
    ...     print(f.readline())
    <BLANKLINE>
    >>> list_to_pixel("doc_list_3.txt","doc_graph_3.txt")
    >>> with open ("doc_graph_3.txt", "r") as f:
    ...     print(f.readline())
    O      O O
    <BLANKLINE>
    """
    txt=open(file_path,'r')
    art=open(filename,'w+')
    count=0
    even=2
    for line in txt:
        count=0
        for char in line:
            if char!=','and char!=' 'and char!='\n':
                num=int(char)
                if count%even==0:
                    for i in range(num):
                        art.write(W)
                else:
                    for i in range(num):
                        art.write(B)
                count+=1
        art.write('\n')



## Question 6.2 ##

def pixel_to_list(pixel):
    """
    >>> pixel0="O OO OOOO OO O\\n"
    >>> pixel_to_list(pixel0)
    [[0, 1, 1, 2, 1, 4, 1, 2, 1, 1]]


    >>> with open("data/pixel_art.txt",'r') as infile:
    ...     pixel1 = infile.readlines()
    >>> pixel1 = ''.join(pixel1)
    >>> pixel_to_list(pixel1)
    [[2, 4, 2], [1, 2, 2, 2, 1], [0, 2, 4, 2], [0, 1, 6, 1], \
[0, 1, 6, 1], [0, 2, 4, 2], [1, 2, 2, 2, 1], [2, 4, 2]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> with open("doc_graph_1.txt",'r') as infile:
    ...     pixel2 = infile.readlines()
    >>> pixel2 = ''.join(pixel2)
    >>> pixel_to_list(pixel2)
    [[0, 2, 4, 7, 2], [3, 1, 1, 4, 2], [5, 1], [0, 9, 3, 4, 2]]
    >>> with open("doc_graph_2.txt",'r') as infile:
    ...     pixel3 = infile.readlines()
    >>> pixel3 = ''.join(pixel3)
    >>> pixel_to_list(pixel3)
    []
    >>> with open("doc_graph_3.txt",'r') as infile:
    ...     pixel4 = infile.readlines()
    >>> pixel4 = ''.join(pixel4)
    >>> pixel_to_list(pixel4)
    [[0, 1, 6, 1, 1, 1], [2, 3, 1, 1, 2, 1, 4], [0, 7, 1, 1, 4, 2, 3], [0], [2, 5, 3, 1]]
    """
    count=0
    color=0
    lst=[]
    temp=[]
    for char in pixel:
        if char!=' 'and char!='O':
            temp.append(count)
            lst.append(temp)
            count=0
            color=0
            temp=[]
        else:
            if color==0:
                if char==' ':
                    count+=1
                else:
                    temp.append(count)
                    color=1
                    count=1
            else:
                if char=='O':
                    count+=1
                else:
                    temp.append(count)
                    color=0
                    count=1
    return lst
                
## Question 7 Extra Credit ##

def parameter_debugger(*params):
    """
    Given a list of string values representing function parameter, output a
    tuple with two items: a corrected list of parameter and a boolean value
    telling whether the list has been corrected or not.

    >>> parameter_debugger('first', 'second=30', '*third', '**fourth')
    (['first', 'second=30', '*third', '**fourth'], True)
    >>> parameter_debugger('slope', '*constants', 'intercept')
    (['slope', 'intercept', '*constants'], False)
    >>> parameter_debugger('*tutor', 'professor="Marina"', '*ta', 'me')
    (['me', 'professor="Marina"', '*tutor'], False)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """
    normal=[]
    default=[]
    args=[]
    kwargs=[]
    lst=[]
    for parameter in params:
        if len(parameter.split('='))>1:
            default.append(parameter)
        elif len(parameter.split('**'))>1:
            if type(kwargs)==list and not len(kwargs)>0:
                kwargs.append(parameter)
        elif len(parameter.split('*'))>1:
            if type(args)==list and not len(args)>0:
                args.append(parameter)
        else:
            normal.append(parameter)
    lst.extend(normal)
    lst.extend(default)
    lst.extend(args)
    lst.extend(kwargs)
    correct=True
    for i in range(len(lst)):
        if lst[i]!=params[i]:
            correct=False
    return tuple([lst,correct])
