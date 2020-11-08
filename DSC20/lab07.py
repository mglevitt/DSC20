# Question 1

def reverse_list(lst):
    """ Reverses lst in place. Make sure to NOT create
    a new array. That is, switch all the elements
    within the same array. Only switch the elements 
    in the passed list and RETURN NOTHING.
    >>> x = [3, 2, 4, 5]
    >>> reverse_list(x)
    >>> x
    [5, 4, 2, 3]
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse_list(x)
    >>> x
    [1, 5, 4, 2, 3]
    >>> x = []
    >>> reverse_list(x)
    >>> x
    []
    >>> x = [1] 
    >>> reverse_list(x)
    >>> x
    [1]
    """
    for i in range(int(len(lst)/2)):
        temp=lst[i]
        lst[i]=lst[len(lst)-1-i]
        lst[len(lst)-1-i]=temp

 
# Question 2

def swap_lists(alist1, alist2):
    """Swaps content of two lists.
    Does not return anything. 
    >>> list1 = [1, 2]
    >>> list2 = [3, 4]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [3, 4]
    >>> print(list2)
    [1, 2]
    >>> list1 = [4, 2, 6, 8, 90, 45]
    >>> list2 = [30, 41, 65, 43, 4, 17]
    >>> swap_lists(list1, list2)
    >>> print(list1)
    [30, 41, 65, 43, 4, 17]
    >>> print(list2)
    [4, 2, 6, 8, 90, 45]
    """
    for i in range(len(alist1)):
        temp=alist1[i]
        alist1[i]=alist2[i]
        alist2[i]=temp


# Question 3

def updated_dic(dict_price, dict_quantity):
    """
    >>> dict_price = {"lemon": 7, "orange": 15, "apple": 5}
    >>> dict_quantity = {"apple": 4, "lemon": 2}
    >>> updated_dic(dict_price, dict_quantity)
    >>> sorted(dict_price)
    ['apple', 'lemon']
    >>> [dict_price[i] for i in sorted(dict_price)]
    [20, 14]

    >>> dict_price = {"peaches": 10, "pears": 4, "grapes": 12}
    >>> dict_quantity = {"peaches": 3, "pears": 10}
    >>> updated_dic(dict_price, dict_quantity)
    >>> sorted(dict_price)
    ['peaches', 'pears']
    >>> [dict_price[i] for i in sorted(dict_price)]
    [30, 40]

    >>> dict_price = {"peaches": 10, "pears": 4, "grapes": 12}
    >>> dict_quantity = {}
    >>> updated_dic(dict_price, dict_quantity)
    >>> dict_price == {}
    True
    """
    
    for i in [*dict_price]:
        if i in dict_quantity:
            dict_price[i]=dict_price[i]*dict_quantity[i]
        else:
            del dict_price[i]
    
    
        


# Question 4

def binary_search(lst, left, right, toFind):
    """
    >>> input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> for i in range(11):
    ...     print(binary_search(input, 0, 9, i), end = " ")
    -1 0 1 2 3 4 5 6 7 8 9 
    
    >>> input = [1, 3, 5, 10, 16, 19, 22]
    >>> binary_search(input, 0, 4, 5)
    2
    >>> binary_search(input, 0, 4, 22)
    -1
    >>> binary_search(input, 4, 6, 22)
    6

    >>> input = [1, 2, 3]
    >>> binary_search(input, 2, 0, 2)
    -1
    >>> input = []
    >>> binary_search(input, 0, 0, 6)
    -1
    """
    half=int((right-left)/2)
    if left<right and left<len(lst):
        if half==0: 
            if lst[left]==toFind:
                return left
            elif lst[right]==toFind:
                return right
            else:
                return -1
        else:
            if toFind in lst[left:left+half]:
                return binary_search(lst,left,left+half,toFind)
            else:
                return binary_search(lst,left+half,right,toFind)
    else:
        return -1


# Question 5

class Aquarium:
    """Creates an Aquarium class with 1 class attribute and two class methods
    >>> Aquarium.content
    'water'
    >>> Aquarium.move()
    'Shattered in pieces'
    >>> Aquarium.install()
    'Bright and shiny'
    """
    content='water'
    def move():
        return 'Shattered in pieces'
    def install():
        return 'Bright and shiny'


# Question 6

class FishTank:
    """ Creates a FishTank class with 1 class attribute (content),
    3 instance attributes (shape, w_type, color) and 1 methods.
    >>> tank = FishTank("round", "salt water", "black")
    >>> tank.content
    'water'
    >>> tank.color
    'black'
    >>> tank.w_type
    'salt water'
    >>> tank.change_shape("square")
    >>> tank.shape
    'square'
    """
    
    content = 'water'
	# Initializer (Constructor) / Instance Attributes
    

    def __init__(self, shape, w_type, color):
            self.shape = shape
            self.w_type = w_type
            self.color = color
   	 

    def change_shape(self, new_shape):
        self.shape = new_shape


# Question 7

class VendingMachine: 
    """ A vending machine that vends some product for some price. 
    >>> v = VendingMachine('candy', 10) 
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15) 
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2) 
    'Current candy stock: 2.'
    >>> v.vend() 
    'You must deposit $10 more.'
    >>> v.deposit(7) 
    'Current balance: $7.'
    >>> v.vend() 
    'You must deposit $3 more.'
    >>> v.deposit(5) 
    'Current balance: $12.'
    >>> v.vend() 
    'Here is your candy and $2 change.'
    >>> v.deposit(10) 
    'Current balance: $10.'
    >>> v.vend() 
    'Here is your candy.'
    >>> v.deposit(15) 
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2) 
    >>> w.restock(3)
    'Current soda stock: 3.'
    >>> w.restock(3) 
    'Current soda stock: 6.'
    >>> w.deposit(2) 
    'Current balance: $2.'
    >>> w.vend() 
    'Here is your soda.'
    """
    content=0
    balance=0
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def vend(self):
        if self.content==0:
            return 'Machine is out of stock.'
        else:
            if self.balance<self.price:
                return 'You must deposit $'+str(self.price-self.balance)+' more.'
            elif self.balance==self.price:
                self.balance=0
                self.content=self.content-1
                return 'Here is your '+self.item+'.'
            else:
                change=str(self.balance-self.price)
                self.balance=0
                self.content=self.content-1
                return 'Here is your '+self.item+' and $'+change+' change.'        
    def deposit(self,money):
        if self.content==0:
            return 'Machine is out of stock. Here is your $'+str(money)+'.'
        else:
            self.balance=self.balance+money
            return 'Current balance: $'+str(self.balance)+'.'
    def restock(self,amount):
        self.content=self.content+amount
        return 'Current '+self.item+' stock: '+str(self.content)+'.'
    
