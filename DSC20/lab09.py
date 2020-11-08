
# Question 1
class Product:
    """
    >>> p1 = Product("Laptop", "Apple", 999)
    >>> print(p1)
    Title: Laptop
    Made by: Apple
    Price: 999
    >>> p1
    Product(Laptop, Apple, 999)

    >>> p2 = Product("TV", "Samsung", 12456)
    >>> print(p2)
    Title: TV
    Made by: Samsung
    Price: 12456
    >>> p2
    Product(TV, Samsung, 12456)

    >>> p3 = Product("Happiness", "DSC20 Tutors", 0)
    >>> print(p3)
    Title: Happiness
    Made by: DSC20 Tutors
    Price: 0
    >>> p3
    Product(Happiness, DSC20 Tutors, 0)
    """
    def __init__(self,item,maker,price):
        self.title=item
        self.maker=maker
        self.price=price
    def __str__(self):
        ttl=self.title
        mkr=self.maker
        prc=self.price
        return 'Title: {0}\nMade by: {1}\nPrice: {2}'.format(ttl,mkr,prc)
    def __repr__(self):
        ttl=self.title
        mkr=self.maker
        prc=self.price
        return 'Product({0}, {1}, {2})'.format(ttl,mkr,prc)
        
    



# Question 2
class DataBase():
    """
    >>> db = DataBase()
    >>> db.add_product(Product("Laptop", "Apple", 976))
    >>> db.add_product(Product("TV", "Sony", 985754))
    >>> db.lookup_product("Laptop")
    Title: Laptop
    Made by: Apple
    Price: 976
    
    >>> db.add_product(Product("Laptop", "Acer", 132))
    >>> db.lookup_product("Laptop")
    Title: Laptop
    Made by: Apple
    Price: 976
    Title: Laptop
    Made by: Acer
    Price: 132
    """
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
    def lookup_product(self,name):
        for i in self.products:
            if i.title==name:
                print(i) 



# Question 3. __add__
class Square:
    """
    >>> s1 = Square(4)
    >>> s2 = Square(5)
    >>> print(s1.area())
    16
    >>> print(s2.area())
    25
    >>> s3 = s1 + s2
    >>> print(s3.side)
    9
    >>> print(s3.area())
    81
    """
    def __init__(self,num):
        self.side=num
    def __repr__(self):
        return str(self.side)
    def __add__(self,other):
        return Square(self.side+other.side)
    def area(self):
        return self.side**2

    



# Question 4
class Compare_Squares(Square):
    """
    >>> s1 = Compare_Squares(4)
    >>> s2 = Compare_Squares(7)
    >>> s3 = Compare_Squares(4)
    >>> s1 < s2
    True
    >>> s1 > s2
    False
    >>> s1 == s2
    False
    >>> s1 > s3
    False
    >>> s1 == s3
    True
    """
    def __eq__(self,other):
        return self.side==other.side
    def __lt__(self,other):
        return self.side<other.side
    def __gt__(self,other):
        return self.side>other.side



# Question 5

# bad
'''
def problem_5_1(lst1, lst2):
    loop_limit = 3
    for i in range( loop_limit ):
        print(lst1[i], '/', lst2[i], '=', lst1[i] / lst2[i] )


def problem_5_2(input_list):
    sum = 0
    sumOfPairs = []
    for i in range(len(input_list)):
        sumOfPairs.append(input_list[i] + input_list[i+1])

    print("sumOfPairs = ", sumOfPairs)


def problem_5_3(fileName):
   file = open(fileName, "r")
   for line in file:
       print(line.upper())
   file.close()


def main():
    problem_5_1([1,  2,3], [2, 3, 0])
    problem_5_2( [ 10, 3, 5, 6, "NA", 3 ] )
    problem_5_2( [ 10, 3, 5, 6 ] )

    problem_5_3( "IDoNotExist.txt" )
    problem_5_3("./Dessssktop/misspelled.txt")
    
main()
'''


# good

def problem_5_1(lst1, lst2):
    """
    >>> problem_5_1([1,2,3], [2, 3, 0])
    1 / 2 = 0.5
    2 / 3 = 0.6666666666666666
    Can't divide by 0!
    """
    loop_limit = 3
    for i in range( loop_limit ):
        try:
            print(lst1[i], '/', lst2[i], '=', lst1[i] / lst2[i] )
        except ZeroDivisionError:
            print("Can't divide by 0!")


def problem_5_2(input_list):
    """
    >>> problem_5_2( [ 10, 3, 5, 6, "NA", 3 ] )
    Danger! Type Mismatch
    Danger! Type Mismatch
    Danger! Index out of bounds
    sumOfPairs =  [13, 8, 11]
    >>> problem_5_2( [ 10, 3, 5, 6 ] )
    Danger! Index out of bounds
    sumOfPairs =  [13, 8, 11]
    """
    sum = 0
    sumOfPairs = []
    for i in range(len(input_list)):
        try:
            sumOfPairs.append(input_list[i] + input_list[i+1])
        except TypeError:
            print('Danger! Type Mismatch')
        except IndexError:
            print('Danger! Index out of bounds')
    print("sumOfPairs = ", sumOfPairs)



def problem_5_3( fileName ):
    """
    >>> problem_5_3( "IDoNotExist.txt" )
    '*Error* File IDoNotExist.txt not found!'

    >>> problem_5_3("./Dessssktop/misspelled.txt")
    '*Error* File ./Dessssktop/misspelled.txt not found!'
    
    >>> problem_5_3('problem5.txt')
    YOU DID IT!
    """
    try:
        file = open(fileName, "r")
    except:
        return'*Error* File {} not found!'.format(fileName)
    for line in file:
            print(line.upper())
    file.close()
    
    
def main():
    problem_5_1([1,2,3], [2, 3, 0])

    problem_5_2( [ 10, 3, 5, 6, 9, 3 ] )
    problem_5_2( [ 10, 3, 5, 6, "NA", 3 ] )
    problem_5_2( [ 10, 3, 5, 6 ] )

    problem_5_3("doesNotExistTest.txt")
    problem_5_3("./Dessssktop/misspelled.txt")
    

#main()
