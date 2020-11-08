import numpy as np
class Stack():
    """
    >>> stack = Stack(3)
    >>> isinstance(stack.items, np.ndarray)
    True
    >>> stack.nelem
    0
    >>> stack.isEmpty()
    True
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
    >>> print(stack.size())
    5
    >>> stack.isEmpty()
    False
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
            return out
        else:
            return 'No elements to remove'
    def push(self,new):
        if self.nelem==self.lngth:
            return 'No space to add elements'
        else:
            self.nelem+=1
            self.items=np.append(self.items,new)
    def peek(self):
        if self.nelem>0:
            return int(self.items[self.nelem-1])
        else:
            return 'No elements to remove'
    def size(self):
        out=0
        for i in self.items:
            out+=len(str(i))
        return out
    def isEmpty(self):
        if self.nelem==0:
            return True
        else:
            return False