from hw08_data import *

## Question 1 ##

CHECK_OUT = "Checking out book failed"
MEMBER_IN_SYSTEM = "Member already in the library System"
MEMBER_NOT_IN_SYSTEM = "Member is not in the library System"

class Library:
    """
    Library class as explained in HW08 writeup.

    >>> sd = Library("San Diego")
    >>> sd.add_book("Harry Potter")
    >>> sd.get_num_books()
    1
    >>> sd.catalog[0]
    'Harry Potter'
    >>> sd.check_out("Harry Potter")
    >>> sd.get_num_books()
    0
    >>> sd.check_out("Tarzan")
    Checking out book failed
    >>> sd.get_location()
    'San Diego'
    >>> la = Library("Los Angeles")
    >>> la.get_location()
    'Los Angeles'
    >>> la.add_member("Harsh")
    >>> la.add_member("Harsh")
    Member already in the library System
    >>> Library.members[0]
    'Harsh'
    >>> sd.remove_member("Harsh")
    >>> sd.remove_member("Harsh")
    Member is not in the library System
    >>> len(Library.members)
    0
    
    
    
    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc = Library("La Jolla")
    >>> doc.add_book('Peter Pan')
    >>> doc.add_book('Bible')
    >>> doc.get_num_books()
    2
    >>> doc.catalog[0]
    'Peter Pan'
    >>> doc.check_out("Bible")
    >>> doc.get_num_books()
    1
    >>> doc.check_out("The Symposium")
    Checking out book failed
    >>> doc.get_location()
    'La Jolla'
    >>> doc2 = Library("Chicago")
    >>> doc2.get_location()
    'Chicago'
    >>> doc2.add_member("Max")
    >>> doc2.add_member("Seth")
    >>> Library.members[0]
    'Max'
    >>> doc2.remove_member("Seth")
    >>> doc2.remove_member("Max")
    >>> len(Library.members)
    0
    >>> la.add_member("Brian")
    """
    members=[]
    def __init__(self,location):
        self.location=location
        self.catalog=[]
    def add_book(self,book):
        self.catalog.append(book)
    def check_out(self,book):
        check=True
        if book in self.catalog:
            for i in range(len(self.catalog)):
                while check:
                    temp=self.catalog.pop(i)
                    if temp!=book:
                        self.catalog.append(temp)
                    else:
                        check=False
        else:
            print(CHECK_OUT)
    def get_location(self):
        return self.location
    def get_num_books(self):
        return len(self.catalog)
    def add_member(self,name):
        if name in Library.members:
            print(MEMBER_IN_SYSTEM)
        else:
            Library.members.append(name)
    def remove_member(self,name):
        check=True
        if name in Library.members:
            for i in range(len(Library.members)):
                while check:
                    temp=Library.members.pop(i)
                    if temp!=name:
                        Library.members.append(temp)
                    else:
                        check=False
        else:
            print(MEMBER_NOT_IN_SYSTEM)
            


class School_Library(Library):
    """
    School_Library class as explained in HW08 writeup. Inherits from the
    Library class. Used specifically for school libraries.

    >>> geisel = School_Library("San Diego", "UCSD")
    >>> geisel.add_member("Harsh")
    >>> geisel.get_school_name()
    'UCSD'
    >>> School_Library.members
    ['Brian', 'Harsh']
    >>> Library.members
    ['Brian', 'Harsh']
    >>> geisel.members
    ['Brian', 'Harsh']

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> barns = School_Library("New York", "NYU")
    >>> barns.add_member("Ted")
    >>> barns.get_school_name()
    'NYU'
    >>> School_Library.members
    ['Brian', 'Harsh', 'Ted']
    >>> Library.members
    ['Brian', 'Harsh', 'Ted']
    >>> barns.members
    ['Brian', 'Harsh', 'Ted']
    """
    def __init__(self,location,name):
        super()
        self.name=name
    def get_school_name(self):
        return self.name

## Question 2 ##

class Counter:
    """
    Counter class as explained in HW08 writeup.

    >>> c = Counter("marina langlois")
    >>> print(c.counter_array)
    [3, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
0, 0, 1]
    >>> print(c.get_count(' '))
    1
    >>> print(c.get_count('!'))
    0
    >>> print(c.get_count('m'))
    1

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> a=Counter('wow data is pretty cool')
    >>> print(a.counter_array)
    [2, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 3, 1, 0, 1, 1, 3, 0, 0, 2, 0, \
1, 0, 4]
    >>> print(a.get_count('o'))
    3
    >>> print(a.get_count('1'))
    0
    >>> print(a.get_count(' '))
    4
    """
    def __init__(self,word):
        chars=27
        self.counter_array=[0]*chars
        self.count_us(self,word)
        
        
    def count_us(self,counter,word):
        base=97
        space=32
        space_in=26
        for i in word:
            if ord(i)==space:
                self.counter_array[space_in]+=1
            else:
                self.counter_array[ord(i)-base]+=1
    def get_count(self,char):
        base=97
        space=32
        space_in=26
        up_in=122
        if ord(char)==space:
            return self.counter_array[space_in]
        elif ord(char)<base or ord(char)>up_in:
            return 0
        else:
            return self.counter_array[ord(char)-base]
        
        


## Question 3.1 ##

def street_fighter_champ(tutors):
    """
    Determines the winner of the street fighter championship. The nested list
    'tutors' shows all the matchups.
    Consider tutor tutor1 = ('Dragon', 10, 10)
    tutor1[1] is the skill level
    tutor1[2] is the tie breaker level. In case skills are tied between two
    tutors, the one with the higher tie breaker score wins. If both skill
    level and tie breaker score is the same, the tutor on the left wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: winner(tuple) The winner of the tournament, in tuple form.
    Restrictions: You should use recursion.

    >>> tutors1 = [Arda]
    >>> tutors2 = [Yuxuan, Arda]
    >>> tutors3 = [[Yuxuan, Arda],[Etsu, Nabi]]
    >>> tutors4 = [[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]]
    >>> tutors5 = [[[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]], [[[Chase, Sudiksha],[Jonathan, Iman]],\
[[Aragorn, Sauron],[Neo, Morpheus]]]]
    >>> street_fighter_champ(tutors1)
    ('Arda', 5, 10)
    >>> street_fighter_champ(tutors2)
    ('Yuxuan', 6, 5)
    >>> street_fighter_champ(tutors3)
    ('Nabi', 7, 5)
    >>> street_fighter_champ(tutors4)
    ('Wesley', 9, 5)
    >>> street_fighter_champ(tutors5)
    ('Neo', 10, 7)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc1=[[[[Arda, Arda],[Jonathan, Iman]],\
[[Prem, Cecilia],[Aaron, Prem]]], [[[Arda, Nabi],[Jonathan, Nabi]],\
[[Cecilia, Aaron],[Neo, Iman]]]]
    >>> doc2=[[[[Iman, Arda],[Wesley, Arda]],\
[[Morpheus, Iman],[Aaron, Prem]]], [[[Sudiksha, Nabi],[Morpheus, Nabi]],\
[[Nabi, Cecilia],[Arda, Sauron]]]]
    >>> doc3=[[[[Chase, Morpheus],[Nabi, Iman]],\
[[Prem, Aaron],[Wesley, Yuxuan]]], [[[Chase, Yuxuan],[Iman, Arda]],\
[[Iman, Cecilia],[Sudiksha, Yuxuan]]]]
    >>> street_fighter_champ(doc1)
    ('Neo', 10, 7)
    >>> street_fighter_champ(doc2)
    ('Sauron', 10, 6)
    >>> street_fighter_champ(doc3)
    ('Morpheus', 9, 10)
    """
    if len(tutors)==1:
        return tutors[0]
    else:
        if isinstance(tutors[0],list):
            win1=street_fighter_champ(tutors[0])
            win2=street_fighter_champ(tutors[1])
            return street_fighter_champ([win1,win2])
        if tutors[0][1]>tutors[1][1]:
            return tutors[0]
        elif tutors[0][1]<tutors[1][1]:
            return tutors[1]
        elif tutors[0][-1]>=tutors[1][-1]:
            return tutors[0]
        else:
            return tutors[1]
        
        
## Question 3.2 ##

def street_fighter_detect_spy(tutors):
    """
    Detect the spy from the street fighter tournament. The worst player wins
    the tournament. ie. lower skill player always wins any matchup. In case of
    skill tie, lower tie breaker score always wins. In case of ties in both,
    the tutor on the right wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: spy(str) The absolute loser of the tournament, in string form.
    Restrictions: You should use recursion.

    >>> tutors0 = [('Pla3', 4, 1)]
    >>> tutors1 = [[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]]
    >>> tutors2 = [[[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]], [[('Pla5', 9, 5), ('Pla8', 8, 3)],[('Pla6', 7, 10),\
('Pla7', 8, 5)]]]
    >>> street_fighter_detect_spy(tutors0)
    'Etsu'
    >>> street_fighter_detect_spy(tutors1)
    'Etsu'
    >>> street_fighter_detect_spy(tutors2)
    'Etsu'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc1=[[[('Pla6', 7, 10), ('Pla1', 5, 10)],[('Pla2', 6, 5),\
('Pla3', 4, 1)]], [[('Pla5', 9, 5), ('Pla4', 4, 2)],[('Pla8', 8, 3),\
('Pla7', 8, 5)]]]
    >>> doc2=[[[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla1', 5, 10),\
('Pla3', 4, 1)]], [[('Pla5', 9, 5), ('Pla1', 5, 10)],[('Pla8', 8, 3),\
('Pla4', 4, 2)]]]   
    >>> doc3=[[[('Pla2', 6, 5), ('Pla2', 6, 5)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]], [[('Pla5', 9, 5), ('Pla8', 8, 3)],[('Pla6', 7, 10),\
('Pla1', 5, 10)]]]
    >>> street_fighter_detect_spy(doc1)
    'Etsu'
    >>> street_fighter_detect_spy(doc2)
    'Etsu'
    >>> street_fighter_detect_spy(doc3)
    'Etsu'
    """
    if len(tutors)==1:
        return secret_dict[tutors[0][0]]
    else:
        if isinstance(tutors[0],list) and isinstance(tutors[1],list):
            win1=street_fighter_detect_spy(tutors[0])
            win2=street_fighter_detect_spy(tutors[1])
            if isinstance(win1,str):
                if secret_dict[win1][1]>secret_dict[win2][1]:
                    return win2
                elif secret_dict[win1][1]<secret_dict[win2][1]:
                    return win1
                elif secret_dict[win1][-1]>=secret_dict[win2][-1]:
                    return win2
                else:
                    return win1
        elif isinstance(tutors[0],tuple) and isinstance(tutors[1],tuple):
            first=secret_dict[secret_dict[tutors[0][0]]]
            second=secret_dict[secret_dict[tutors[1][0]]]
            if first[1]>second[1]:
                return secret_dict[tutors[1][0]]
            elif first[1]<second[1]:
                return secret_dict[tutors[0][0]]
            elif first[-1]>=second[-1]:
                return secret_dict[tutors[1][0]]
            else:
                return secret_dict[tutors[0][0]]
        

## Question 4 ##

def make_reviews_list(dining_hall, ratings):
    """
    Creates a list of reviews for a particular dining hall given a list of
    ratings.

    Try using list comprehesions!

    >>> make_reviews_list('A', [123])
    [['A', 123]]
    >>> make_reviews_list('B', [0, 1])
    [['B', 0], ['B', 1]]
    >>> make_reviews_list('7th College Dining Hall', [])
    []
    >>> make_reviews_list('Foodworx', ["Best food", 5, ":)", 100, 1, 1, 5])
    [['Foodworx', 'Best food'], ['Foodworx', 5], ['Foodworx', ':)'], \
['Foodworx', 100], ['Foodworx', 1], ['Foodworx', 1], ['Foodworx', 5]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> make_reviews_list('bop', [1,8,7,3,4,6,2])
    [['bop', 1], ['bop', 8], ['bop', 7], ['bop', 3], ['bop', 4], ['bop', 6], \
['bop', 2]]
    >>> make_reviews_list('poo', [0,0,0,0,'bad','no'])
    [['poo', 0], ['poo', 0], ['poo', 0], ['poo', 0], ['poo', 'bad'], ['poo'\
, 'no']]
    >>> make_reviews_list('what', ['?'])
    [['what', '?']]
    """
    assert isinstance(dining_hall,str) and isinstance(ratings,list)
    out=[]
    for i in ratings:
        review=make_review(dining_hall,i)
        out.append(review)
    return out


## Question 5 ##

def average_rating(dining_hall, reviews=google_reviews):
    """
    Finds the average rating for a particular dining hall. The list of
    reviews is given as the second parameter. The average rating should be
    returned as its own review.

    >>> average_rating('Canyon Vista')
    2.2
    >>> average_rating('64 Degrees')
    4.2
    >>> average_rating('Foodworx')
    3.4
    >>> average_rating('Pines')
    3.6

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> average_rating('OVT')
    4.0
    >>> average_rating('Cafe Ventanas')
    3.4
    >>> average_rating('food')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(dining_hall,str)
    total=0
    count=0
    for i in reviews:
        if get_place(i)==dining_hall:
            total+=get_rating(i)
            count+=1
    assert count>0
    return total/count


## Question 6 ##

def better_dining_hall(first, second):
    """
    Returns the name of the better dining hall between the two given
    dining halls. The better dining hall is the dining hall with a higher
    average review.

    >>> better_dining_hall('OVT', 'Pines')
    'OVT'
    >>> better_dining_hall('Canyon Vista', 'Pines')
    'Pines'
    >>> better_dining_hall('Cafe Ventanas', '64 Degrees')
    '64 Degrees'
    >>> better_dining_hall('64 Degrees', 'OVT')
    '64 Degrees'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> better_dining_hall(5, 'OVT')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> better_dining_hall('big', 'Pines')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> better_dining_hall('OVT', 'Canyon Vista')
    'OVT'
    """
    if average_rating(first)>=average_rating(second):
        return first
    else:
        return second
