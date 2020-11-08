import numpy as np

# 1 Sets (simple)
def common_letters(input1, input2):
    """
    >>> common_letters("marina", "langlois")
    'The common letters are: a i n'

    >>> common_letters("turkey", "gravy")
    'The common letters are: r y'

    >>> common_letters("cat", "dog")
    'There are no common letters'
    """
    cl=set(input1) & set(input2)
    lst=[]
    out=''
    for i in cl:
        lst.append(i)
    for i in input1:
        if i in lst and i not in out:
            out+=' '+i
    if len(out)==0:
        return 'There are no common letters'
    else:
        return 'The common letters are:'+out


# 2 Sets
def common_words(file1, file2):
    """
    >>> common_words("file1.txt", "file4.txt")
    'File does not exist'
    
    >>> common_words("file1.txt", "file2.txt")
    'The common words are: Today World! a is'

    >>> common_words("file2.txt", "file3.txt")
    'The common words are: Goodbye, rainy'

    >>> common_words("file1.txt", "file3.txt")
    'There are no common words'
    """
    try:
        f1=open(file1,'r')
        f1t=f1.read()
        f1.close()
    except:
        return 'File does not exist'
    try:
        f2=open(file2,'r')
        f2t=f2.read()
        f2.close()
    except:
        return 'File does not exist'
    f1l=f1t.split('\n')
    f1w=[]
    for i in f1l:
        f1w+=i.split(' ')
    f2l=f2t.split('\n')
    f2w=[]
    for i in f2l:
        f2w+=i.split(' ')
    cw=set(f1w)&set(f2w)
    lst=[]
    for i in cw:
        lst.append(i)
    if len(lst)==0:
        return 'There are no common words'
    else:
        lst=sorted(lst)
        out=''
        for i in lst:
            out+=' '+i
        return 'The common words are:'+out
    

# 3 Stack
class Stack():
    """
    >>> stack = Stack(3)
    >>> isinstance(stack.items, np.ndarray)
    True
    >>> stack.nelem
    0
    >>> print(stack)
    (bottom)(top)
    >>> stack.push(1)
    >>> stack.push(2)
    >>> print(stack)
    (bottom) 1 -> 2 (top)
    >>> stack.pop()
    2
    >>> print(stack)
    (bottom) 1 (top)
    >>> stack.pop()
    1
    >>> stack.pop()
    'No elements to remove'
    >>> stack.push(5)
    >>> stack.push(10)
    >>> stack.push(15)
    >>> stack.push(20)
    'No space to add elements'
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    >>> stack.peek()
    15
    >>> print(stack)
    (bottom) 5 -> 10 -> 15 (top)
    """
    def __init__(self,lngth):
        self.items=np.array([])
        self.nelem=0
        self.lngth=lngth
    def __str__(self):
        out='(bottom)'
        if self.nelem>=1:
            out+=' {0} '.format(self.items[0])
        if self.nelem>1:
            for i in range(self.nelem-1):
                out+='-> {0} '.format(self.items[i+1])
        return out+'(top)'
    def pop(self):
        if self.nelem>0:
            self.nelem-=1
            out=self.items[self.nelem]
            self.items=np.delete(self.items,self.nelem)
            return int(out)
        else:
            return 'No elements to remove'
    def push(self,new):
        if self.nelem==self.lngth:
            return 'No space to add elements'
        else:
            self.nelem+=1
            self.items=np.append(self.items,str(new))
    def peek(self):
        if self.nelem>0:
            return int(self.items[self.nelem-1])
        else:
            return 'No elements to remove'
            
        
    
