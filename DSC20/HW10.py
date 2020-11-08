import numpy as np
from stack import Stack

## Question 1 ##
def paren_checker(expression):
    """
    YOU MUST USE YOUR STACK CLASS THAT YOU IMPLEMENTED IN LAB10. Check the
    writeup for details. This function checks whether the pairs and the orders
    of '{', '}', '(','), '[', ']' are correct in a given expression.

    >>> paren_checker("(((]})")
    False
    >>> paren_checker("(")
    False
    >>> paren_checker("(){}[]")
    True
    >>> paren_checker("(   x   )")
    True
    >>> paren_checker("a()b{}c[]d")
    True
    >>> paren_checker("")
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> paren_checker("({)(}{)()})})")
    False
    >>> paren_checker("]")
    False
    >>> paren_checker("({[({([[{()}]])})]})")
    True
    """
    bal=True
    stack=Stack(len(expression))
    for i in expression:
        if i=='(' or i=='[' or i=='{':
            stack.push(i)
        if i==')' or i==']' or i=='}':
            temp=stack.pop()
            if i==')' and temp!='(':
                bal=False
            if i==']' and temp!='[':
                bal=False
            if i=='}' and temp!='{':
                bal=False
    if stack.isEmpty()==False:
        bal=False
    return bal
    
## Question 2 ##
class Queue:
    """
    A queue ADT that dequeues from front and enqueues at rear.

    >>> a=Queue()
    >>> a.enqueue(1)
    >>> a.enqueue(2)
    >>> a.enqueue(3)
    >>> a.enqueue(4)
    >>> a.enqueue(5)
    >>> a.print_queue()
    [ | 1 | 2 | 3 | 4 | 5 | ]
    >>> a.front
    0
    >>> a.rear
    5
    >>> a.data
    array([1, 2, 3, 4, 5, None, None, None, None, None], dtype=object)
    >>> a.capacity
    10
    >>> a.dequeue()
    1
    >>> a.print_queue()
    [ | 2 | 3 | 4 | 5 | ]
    >>> a.front
    1
    >>> a.rear
    5

    >>> a=Queue(10)
    >>> a.capacity
    10

    >>> b=Queue()
    >>> b.dequeue()
    Attempt to dequeue from an empty queue
    >>> b.enqueue(1)
    >>> b.enqueue(max)
    >>> b.print_queue()
    [ | 1 | <built-in function max> | ]
    >>> b.dequeue()
    1
    >>> b.dequeue()
    <built-in function max>
    >>> b.front
    2
    >>> b.rear
    2
    >>> b.dequeue()
    Attempt to dequeue from an empty queue

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> d=Queue(1)
    >>> d.is_empty()
    True
    >>> d.is_full()
    False
    >>> d.enqueue(0)
    >>> d.print_queue()
    [ | 0 | ]
    >>> d.enqueue(1)
    >>> d.dequeue()
    0
    >>> d.dequeue()
    1
    >>> d.is_empty()
    True
    >>> e=Queue()
    >>> e.enqueue('hi')
    >>> e.enqueue(5)
    >>> e.enqueue(2.0)
    >>> e.is_full()
    False
    >>> e.is_empty()
    False
    >>> e.dequeue()
    'hi'
    >>> e.print_queue()
    [ | 5 | 2.0 | ]
    >>> f=Queue(2)
    >>> f.enqueue('doc')
    >>> f.enqueue('docer')
    >>> f.is_full()
    False
    >>> f.dequeue()
    'doc'
    >>> f.dequeue()
    'docer'
    >>> f.print_queue()
    []
    """

    def __init__(self, capacity = 5):
        """
        >>> q = Queue()
        """
        self.data=np.array([None]*capacity)
        self.front=0
        self.rear=1
        self.capacity=capacity
        self.num_elems=0

    def dequeue(self):
        """
        dequeues from the front of the queue

        >>> q = Queue()
        >>> q.dequeue()
        Attempt to dequeue from an empty queue
        """
        if self.num_elems==0:
            print('Attempt to dequeue from an empty queue')
        else:
            out=self.data[self.front]
            self.data[self.front]=None
            self.front+=1
            self.num_elems-=1
            return out

    def enqueue(self, elem):
        """
        enqueue at the rear of the queue
        >>> q = Queue()
        >>> q.enqueue("a")
        """
        if self.num_elems==self.capacity-1:
            self.expand()
        if self.num_elems==0:
            self.data[self.rear-1]=elem
        elif self.rear==self.capacity-1:
            self.data[self.rear]=elem
            self.rear=0
        else:
            self.data[self.rear]=elem
            self.rear+=1
        self.num_elems+=1
        
    def expand(self):
        """
        expand the capacity of the circular array when needed
        >>> q = Queue()
        >>> q.capacity
        5
        >>> q.expand()
        >>> q.capacity
        10
        """
        double=2
        self.data=np.append(self.data,[None]*self.capacity)
        self.capacity*=double

    def is_full(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array([0, 1, 2, 3, None], dtype=object)
        >>> q.is_full()
        False
        """
        if self.num_elems==self.capacity:
            return True
        else:
            return False

    def is_empty(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        if self.num_elems==0:
            return True
        else:
            return False
        
    def print_queue(self):
        """
        prints out queue in a human-friendly format
        >>> q = Queue()
        >>> for i in range(5): q.enqueue(i)
        >>> q.print_queue()
        [ | 0 | 1 | 2 | 3 | 4 | ]
        >>> p = Queue()
        >>> p.print_queue()
        []
        """
        out=''
        if self.is_empty()==False:
            out+=' | {0} | '.format(self.data[self.front])
        if self.num_elems>1:
            for i in range(1,self.num_elems):
                if self.front+i<=self.capacity-1:
                    out+='{0} | '.format(self.data[self.front+i])
                else:
                    cap=self.capacity
                    out+='{0} | '.format(self.data[cap-self.front-i-1])
        print('[{0}]'.format(out))
        
        

## Question 3 ##
def cursed_carousel(n, m):
    """
    m is the number of customers in line
    n is the number of customers sent to the back of the line
    Return the number of the customer which is last to be served

    >>> cursed_carousel(6,3)
    3
    6
    4
    2
    5
    1
    >>> cursed_carousel(-1,-2)
    m and n should be positive!
    >>> cursed_carousel('5','1')
    Invalid input data type.

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cursed_carousel(1,2)
    1
    >>> cursed_carousel(10,1)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    >>> cursed_carousel(5,5)
    5
    1
    2
    3
    4
    """
    if not isinstance(n,int) or not isinstance(m,int):
        print('Invalid input data type.')
        return
    if n<0 or m<0:
        print('m and n should be positive!')
        return
    q = Queue()
    for i in range(n):
        q.enqueue(i+1)
    for i in range(n):
        q.data=np.append(q.data[m-1:n],q.data[:m-1])
        print(q.data[0])
        q.data=q.data[1:]
        

## Question 4 (Extra Credit) ##
def find_best_farm(land_plots):
    """
    Finds the best farm given a list of land plots.

    Restrictions: You must use a stack and your algorithm must run
    in O(n) time. Make sure to fill out extra_credit.txt to get credit.
    
    This code works but it does not use stacks:
    max=0
    for i in range(1,len(land_plots)+1):
        for j in range(i):
            temp=min(land_plots[j:i])*(i-j)
            if temp>max:
                max=temp
    return max
    
    
    >>> find_best_farm([3, 2, 3])
    6
    >>> find_best_farm([1, 2, 3, 4, 5])
    9
    >>> find_best_farm([5, 4, 3, 2, 1])
    9

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> find_best_farm([1])
    1
    >>> find_best_farm([1, 2, 3, 4, 5,6,7,8,9])
    25
    >>> find_best_farm([5, 2,4,3,1,7])
    8
    """
    l=Stack(len(land_plots))
    g=Stack(len(land_plots))
    max=0
    for i in land_plots:
        if i>max:
            max=i
        if l.nelem>0:
            if i <l.peek():
                l.push(i)
                temp=l.nelem*i
                if temp>max:
                    max=temp
            elif i>l.peek():
                l.push(l.peek())
                temp=l.nelem*l.peek()
                if temp>max:
                    max=temp
        else:
            l.push(i)
            if i>max:
                max=i
    for i in land_plots[::-1]:
        if g.nelem>0:
            if i <g.peek():
                g.push(i)
                temp=g.nelem*i
                if temp>max:
                    max=temp
            elif i>g.peek():
                g.push(l.peek())
                temp=g.nelem*l.peek()
                if temp>max:
                    max=temp
        else:
            g.push(i)
    return max