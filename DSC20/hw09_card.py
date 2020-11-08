"""
DSC 20 HW 09 CARD
NAME: Maxwell Levitt
PID: A15788481
"""

import numpy as np

## Question 4.1 ##
class card:
    """
    This class represents a single card.

    >>> c1 = card(4, "Clubs")
    >>> print(c1)
    4 of Clubs
    >>> c2 = card(3, "Hearts")
    >>> print(c2)
    3 of Hearts
    >>> c1 < c2
    True
    >>> c1 > c2
    False
    >>> c1 == c2
    False

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> d1 = card('A', "Diamonds")
    >>> d1
    A of Diamonds
    >>> print(d1)
    A of Diamonds
    >>> d2 = card(5, "Spades")
    >>> d2
    5 of Spades
    >>> print(d2)
    5 of Spades
    >>> d1 < d2
    True
    >>> d1 > d2
    False
    >>> d1 <= d2
    True
    >>> d1 >= d2
    False
    >>> d1 == d2
    False
    >>> d1 != d2
    True
    >>> d1 = card('J', "Diamonds")
    >>> d1
    J of Diamonds
    >>> print(d1)
    J of Diamonds
    >>> d2 = card('J', "Diamonds")
    >>> d2
    J of Diamonds
    >>> print(d2)
    J of Diamonds
    >>> d1 < d2
    False
    >>> d1 > d2
    False
    >>> d1 <= d2
    True
    >>> d1 >= d2
    True
    >>> d1 == d2
    True
    >>> d1 != d2
    False
    >>> d1 = card('J', "Spades")
    >>> d1
    J of Spades
    >>> print(d1)
    J of Spades
    >>> d2 = card(10, "Spades")
    >>> d2
    10 of Spades
    >>> print(d2)
    10 of Spades
    >>> d1 < d2
    False
    >>> d1 > d2
    True
    >>> d1 <= d2
    False
    >>> d1 >= d2
    True
    >>> d1 == d2
    False
    >>> d1 != d2
    True
    """
    c=1
    d=2
    h=3
    s=4
    
    sd={'Clubs':c,'Diamonds':d,'Hearts':h,'Spades':s}
    
    def __init__(self, rank, suit):
        """Initializes the function's variables including the rank, suit, \
        and num which is the all number version of rank."""
        j=11
        q=12
        k=13
        rd={'A':1,'J':j,'Q':q,'K':k}
        self.rank=rank
        self.suit=suit
        if isinstance(self.rank,int):
            self.num=self.rank
        else:
            self.num=rd[self.rank]
    def __repr__(self):
        """Returns the representation of card."""
        return str(self.rank)+' of '+self.suit

    def __str__(self):
        """Returns the string that will be printed for card."""
        return str(self.rank)+' of '+self.suit

    def __eq__(self, other):
        """Returns the boolean of whether the two cards are equal."""
        if self.num==other.num and self.suit==other.suit:
            return True
        else:
            return False

    def __ne__(self, other):
        """Returns the boolean of whether the two cards are not equal."""
        if self.num==other.num and self.suit==other.suit:
            return False
        else:
            return True

    def __lt__(self, other):
        """Returns the boolean of whether the first card is less than the \
        second card."""
        if card.sd[self.suit]<card.sd[other.suit]:
            return True
        elif card.sd[self.suit]>card.sd[other.suit]:
            return False
        elif self.num<other.num:
            return True
        else:
            return False
    def __gt__(self, other):
        """Returns the boolean of whether the first card is greater than the \
        second card."""
        if card.sd[self.suit]>card.sd[other.suit]:
            return True
        elif card.sd[self.suit]<card.sd[other.suit]:
            return False
        elif self.num>other.num:
            return True
        else:
            return False

    def __le__(self, other):
        """Returns the boolean of whether the first card is less than or \
        equal to the second card."""
        if card.sd[self.suit]<card.sd[other.suit]:
            return True
        elif card.sd[self.suit]>card.sd[other.suit]:
            return False
        elif self.num<=other.num:
            return True
        else:
            return False

    def __ge__(self, other):
        """Returns the boolean of whether the first card is greater than or \
        equal to the second card."""
        if card.sd[self.suit]>card.sd[other.suit]:
            return True
        elif card.sd[self.suit]<card.sd[other.suit]:
            return False
        elif self.num>=other.num:
            return True
        else:
            return False
    
            
## Question 4.2 ##
class deck:
    """
    >>> cards = deck()
    >>> len(cards.deck)
    52
    >>> cards = deck()
    >>> len(cards.dealt_cards)
    0
    >>> cards = deck()
    >>> print(cards)
    In Deck:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    >>> deck_to_shuffle = deck()
    >>> np.random.seed(5)
    >>> deck_to_shuffle.shuffle()
    >>> print(deck_to_shuffle.deck[:5])
    [9 of Hearts, 4 of Hearts, 7 of Spades, 7 of Diamonds, 6 of Hearts]
    >>> deck_to_deal = deck()
    >>> hand = deck_to_deal.deal_cards(5)
    >>> np.random.seed(5)
    >>> deck_to_deal.shuffle()
    >>> deck_to_deal.deck[:5]
    [A of Spades, 9 of Hearts, Q of Spades, Q of Diamonds, J of Hearts]
    >>> cards = deck()
    >>> cards.deal_cards(5)
    [A of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs]
    >>> cards = deck()
    >>> hand = cards.deal_cards(5)
    >>> cards.deal_cards(5)
    [6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs]
    >>> cards = deck()
    >>> hand = cards.deal_cards(5)
    >>> print(cards)
    In Deck:
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> doc=deck()
    >>> doc
    In Deck:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    >>> print(doc)
    In Deck:
    A of Clubs
    2 of Clubs
    3 of Clubs
    4 of Clubs
    5 of Clubs
    6 of Clubs
    7 of Clubs
    8 of Clubs
    9 of Clubs
    10 of Clubs
    J of Clubs
    Q of Clubs
    K of Clubs
    A of Diamonds
    2 of Diamonds
    3 of Diamonds
    4 of Diamonds
    5 of Diamonds
    6 of Diamonds
    7 of Diamonds
    8 of Diamonds
    9 of Diamonds
    10 of Diamonds
    J of Diamonds
    Q of Diamonds
    K of Diamonds
    A of Hearts
    2 of Hearts
    3 of Hearts
    4 of Hearts
    5 of Hearts
    6 of Hearts
    7 of Hearts
    8 of Hearts
    9 of Hearts
    10 of Hearts
    J of Hearts
    Q of Hearts
    K of Hearts
    A of Spades
    2 of Spades
    3 of Spades
    4 of Spades
    5 of Spades
    6 of Spades
    7 of Spades
    8 of Spades
    9 of Spades
    10 of Spades
    J of Spades
    Q of Spades
    K of Spades
    Dealt Out:
    >>> doc.shuffle()
    >>> doc
    In Deck:
    4 of Spades
    K of Hearts
    10 of Spades
    7 of Hearts
    5 of Clubs
    10 of Diamonds
    J of Clubs
    8 of Diamonds
    5 of Diamonds
    3 of Hearts
    10 of Hearts
    9 of Hearts
    7 of Diamonds
    Q of Diamonds
    A of Spades
    6 of Hearts
    Q of Spades
    6 of Diamonds
    K of Clubs
    A of Clubs
    9 of Clubs
    8 of Spades
    J of Diamonds
    A of Diamonds
    3 of Clubs
    6 of Clubs
    Q of Hearts
    3 of Diamonds
    7 of Clubs
    10 of Clubs
    A of Hearts
    2 of Spades
    9 of Spades
    4 of Diamonds
    K of Spades
    9 of Diamonds
    K of Diamonds
    8 of Hearts
    4 of Hearts
    3 of Spades
    2 of Diamonds
    2 of Hearts
    J of Spades
    2 of Clubs
    4 of Clubs
    5 of Spades
    Q of Clubs
    5 of Hearts
    7 of Spades
    6 of Spades
    J of Hearts
    8 of Clubs
    Dealt Out:
    >>> doc.deal_cards(1)
    [4 of Spades]
    >>> doc.shuffle()
    >>> print(doc)
    In Deck:
    3 of Diamonds
    2 of Spades
    7 of Spades
    10 of Spades
    8 of Hearts
    6 of Hearts
    5 of Diamonds
    6 of Diamonds
    5 of Clubs
    3 of Clubs
    7 of Hearts
    J of Diamonds
    2 of Clubs
    2 of Diamonds
    Q of Diamonds
    9 of Hearts
    K of Hearts
    10 of Hearts
    4 of Clubs
    5 of Spades
    10 of Diamonds
    9 of Spades
    Q of Hearts
    4 of Spades
    3 of Spades
    9 of Clubs
    6 of Spades
    K of Clubs
    4 of Hearts
    9 of Diamonds
    2 of Hearts
    Q of Clubs
    J of Hearts
    A of Spades
    5 of Hearts
    4 of Diamonds
    3 of Hearts
    8 of Spades
    K of Diamonds
    8 of Diamonds
    Q of Spades
    10 of Clubs
    K of Spades
    6 of Clubs
    A of Hearts
    7 of Clubs
    A of Clubs
    8 of Clubs
    A of Diamonds
    J of Spades
    J of Clubs
    7 of Diamonds
    Dealt Out:
    >>> doc=deck()
    >>> doc.shuffle()
    >>> doc
    In Deck:
    K of Diamonds
    7 of Clubs
    6 of Hearts
    4 of Diamonds
    5 of Hearts
    9 of Hearts
    2 of Diamonds
    Q of Spades
    Q of Clubs
    4 of Clubs
    8 of Diamonds
    9 of Spades
    3 of Hearts
    A of Spades
    6 of Diamonds
    K of Clubs
    7 of Spades
    A of Hearts
    9 of Diamonds
    5 of Diamonds
    8 of Spades
    5 of Clubs
    8 of Clubs
    10 of Spades
    4 of Hearts
    K of Hearts
    6 of Spades
    10 of Clubs
    A of Diamonds
    3 of Spades
    Q of Diamonds
    8 of Hearts
    7 of Diamonds
    J of Spades
    4 of Spades
    Q of Hearts
    J of Diamonds
    2 of Clubs
    2 of Hearts
    2 of Spades
    3 of Clubs
    A of Clubs
    J of Hearts
    5 of Spades
    10 of Hearts
    6 of Clubs
    3 of Diamonds
    7 of Hearts
    K of Spades
    10 of Diamonds
    J of Clubs
    9 of Clubs
    Dealt Out:
    >>> doc.deal_cards(48)
    [K of Diamonds, 7 of Clubs, 6 of Hearts, 4 of Diamonds, 5 of Hearts, 9 of \
Hearts, 2 of Diamonds, Q of Spades, Q of Clubs, 4 of Clubs, 8 of Diamonds, 9 o\
f Spades, 3 of Hearts, A of Spades, 6 of Diamonds, K of Clubs, 7 of Spades, A \
of Hearts, 9 of Diamonds, 5 of Diamonds, 8 of Spades, 5 of Clubs, 8 of Clubs, \
10 of Spades, 4 of Hearts, K of Hearts, 6 of Spades, 10 of Clubs, A of Diamond\
s, 3 of Spades, Q of Diamonds, 8 of Hearts, 7 of Diamonds, J of Spades, 4 of \
Spades, Q of Hearts, J of Diamonds, 2 of Clubs, 2 of Hearts, 2 of Spades, 3 \
of Clubs, A of Clubs, J of Hearts, 5 of Spades, 10 of Hearts, 6 of Clubs, 3 \
of Diamonds, 7 of Hearts]
    >>> doc=deck()
    >>> doc.deal_cards(100)
    Traceback (most recent call last):
    ...
    AssertionError
    """
    def __init__(self):
        """Initializes the deck of cards."""
        t=2
        th=3
        f=4
        fi=5
        s=6
        se=7
        e=8
        n=9
        te=10
        ranks=['A',t,th,f,fi,s,se,e,n,te,'J','Q','K']
        suits=['Clubs','Diamonds','Hearts','Spades']
        self.deck=[card(i,j) for j in suits for i in ranks]
        self.dealt_cards=[]

    def shuffle(self):
        """This method shuffles the deck using np.random.choice."""
        self.deck+=self.dealt_cards
        l=len(self.deck)
        self.dealt_cards=[]
        self.deck=list(np.random.choice(self.deck,l,replace=False))

    def deal_cards(self, n):
        """
        This method deals out n cards and sends them all to the dealt cards list.
        It also returns the list of the cards.
        """
        assert n<=len(self.deck)
        self.dealt_cards=[]
        [self.dealt_cards.append(self.deck[i]) for i in range(n)]
        self.deck=self.deck[n:]
        return self.dealt_cards

    def __repr__(self):
        """Returns the representation of deck."""
        out='In Deck:'
        for i in self.deck:
            out+='\n'+i.__repr__()
        out+='\n'+'Dealt Out:'
        for i in self.dealt_cards:
            out+='\n'+i.__repr__()
        return out

    def __str__(self):
        """Returns the string that is printed for deck."""
        out='In Deck:'
        for i in self.deck:
            out+='\n'+i.__repr__()
        out+='\n'+'Dealt Out:'
        for i in self.dealt_cards:
            out+='\n'+i.__repr__()
        return out
        
## Question 4.3 ##
class WarGame:
    """
    >>> np.random.seed(5)
    >>> game = WarGame()
    >>> game.play_rounds(5)
    Player 1's card:  9 of Hearts
    Player 2's card:  4 of Hearts
    Player 1 Won the Round
    Player 1's card:  7 of Spades
    Player 2's card:  7 of Diamonds
    Player 1 Won the Round
    Player 1's card:  6 of Hearts
    Player 2's card:  9 of Diamonds
    Player 1 Won the Round
    Player 1's card:  7 of Clubs
    Player 2's card:  8 of Hearts
    Player 2 Won the Round
    Player 1's card:  3 of Clubs
    Player 2's card:  4 of Clubs
    Player 2 Won the Round
    The score is now 3 to 2
    >>> game.declare_winner()
    The score is 3 to 2
    Player 1 Wins!

    >>> np.random.seed(15)
    >>> game = WarGame()
    >>> game.play_rounds(4)
    Player 1's card:  8 of Hearts
    Player 2's card:  4 of Diamonds
    Player 1 Won the Round
    Player 1's card:  9 of Hearts
    Player 2's card:  J of Spades
    Player 2 Won the Round
    Player 1's card:  Q of Hearts
    Player 2's card:  9 of Spades
    Player 2 Won the Round
    Player 1's card:  A of Spades
    Player 2's card:  K of Hearts
    Player 1 Won the Round
    The score is now 2 to 2
    >>> game.declare_winner()
    The score is 2 to 2
    It's a Tie!

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> game = WarGame()
    >>> game.play_rounds()
    Player 1's card:  9 of Clubs
    Player 2's card:  9 of Spades
    Player 2 Won the Round
    The score is now 0 to 1
    >>> game.declare_winner()
    The score is 0 to 1
    Player 2 Wins!
    >>> game = WarGame()
    >>> game.play_rounds(20)
    Player 1's card:  7 of Clubs
    Player 2's card:  6 of Spades
    Player 2 Won the Round
    Player 1's card:  6 of Diamonds
    Player 2's card:  10 of Hearts
    Player 2 Won the Round
    Player 1's card:  4 of Hearts
    Player 2's card:  K of Hearts
    Player 2 Won the Round
    Player 1's card:  3 of Clubs
    Player 2's card:  J of Spades
    Player 2 Won the Round
    Player 1's card:  2 of Clubs
    Player 2's card:  2 of Diamonds
    Player 2 Won the Round
    Player 1's card:  K of Spades
    Player 2's card:  10 of Diamonds
    Player 1 Won the Round
    Player 1's card:  5 of Hearts
    Player 2's card:  K of Diamonds
    Player 1 Won the Round
    Player 1's card:  Q of Hearts
    Player 2's card:  6 of Clubs
    Player 1 Won the Round
    Player 1's card:  2 of Spades
    Player 2's card:  8 of Clubs
    Player 1 Won the Round
    Player 1's card:  4 of Spades
    Player 2's card:  5 of Clubs
    Player 1 Won the Round
    Player 1's card:  A of Clubs
    Player 2's card:  5 of Diamonds
    Player 2 Won the Round
    Player 1's card:  3 of Spades
    Player 2's card:  A of Hearts
    Player 1 Won the Round
    Player 1's card:  8 of Diamonds
    Player 2's card:  10 of Clubs
    Player 1 Won the Round
    Player 1's card:  Q of Diamonds
    Player 2's card:  2 of Hearts
    Player 2 Won the Round
    Player 1's card:  10 of Spades
    Player 2's card:  9 of Spades
    Player 1 Won the Round
    Player 1's card:  4 of Clubs
    Player 2's card:  6 of Hearts
    Player 2 Won the Round
    Player 1's card:  K of Clubs
    Player 2's card:  9 of Diamonds
    Player 2 Won the Round
    Player 1's card:  Q of Spades
    Player 2's card:  7 of Spades
    Player 1 Won the Round
    Player 1's card:  A of Diamonds
    Player 2's card:  Q of Clubs
    Player 1 Won the Round
    Player 1's card:  J of Clubs
    Player 2's card:  A of Spades
    Player 2 Won the Round
    The score is now 10 to 10
    >>> game.declare_winner()
    The score is 10 to 10
    It's a Tie!
    >>> game = WarGame()
    >>> game.play_rounds(100)
    Player 1's card:  3 of Spades
    Player 2's card:  3 of Hearts
    Player 1 Won the Round
    Player 1's card:  K of Clubs
    Player 2's card:  2 of Clubs
    Player 1 Won the Round
    Player 1's card:  6 of Clubs
    Player 2's card:  8 of Diamonds
    Player 2 Won the Round
    Player 1's card:  Q of Hearts
    Player 2's card:  A of Spades
    Player 2 Won the Round
    Player 1's card:  7 of Hearts
    Player 2's card:  A of Hearts
    Player 1 Won the Round
    Player 1's card:  3 of Diamonds
    Player 2's card:  4 of Clubs
    Player 1 Won the Round
    Player 1's card:  6 of Diamonds
    Player 2's card:  Q of Spades
    Player 2 Won the Round
    Player 1's card:  2 of Hearts
    Player 2's card:  10 of Clubs
    Player 1 Won the Round
    Player 1's card:  K of Hearts
    Player 2's card:  2 of Diamonds
    Player 1 Won the Round
    Player 1's card:  A of Clubs
    Player 2's card:  8 of Hearts
    Player 2 Won the Round
    Player 1's card:  4 of Hearts
    Player 2's card:  4 of Spades
    Player 2 Won the Round
    Player 1's card:  10 of Diamonds
    Player 2's card:  9 of Hearts
    Player 2 Won the Round
    Player 1's card:  Q of Clubs
    Player 2's card:  5 of Hearts
    Player 2 Won the Round
    Player 1's card:  9 of Diamonds
    Player 2's card:  J of Diamonds
    Player 2 Won the Round
    Player 1's card:  J of Spades
    Player 2's card:  A of Diamonds
    Player 1 Won the Round
    Player 1's card:  K of Spades
    Player 2's card:  4 of Diamonds
    Player 1 Won the Round
    Player 1's card:  3 of Clubs
    Player 2's card:  J of Hearts
    Player 2 Won the Round
    Player 1's card:  J of Clubs
    Player 2's card:  2 of Spades
    Player 2 Won the Round
    Player 1's card:  5 of Clubs
    Player 2's card:  6 of Spades
    Player 2 Won the Round
    Player 1's card:  Q of Diamonds
    Player 2's card:  9 of Spades
    Player 2 Won the Round
    Player 1's card:  K of Diamonds
    Player 2's card:  8 of Clubs
    Player 1 Won the Round
    Player 1's card:  7 of Clubs
    Player 2's card:  8 of Spades
    Player 2 Won the Round
    Player 1's card:  10 of Hearts
    Player 2's card:  7 of Spades
    Player 2 Won the Round
    Player 1's card:  5 of Diamonds
    Player 2's card:  10 of Spades
    Player 2 Won the Round
    Player 1's card:  6 of Hearts
    Player 2's card:  5 of Spades
    Player 2 Won the Round
    Player 1's card:  7 of Diamonds
    Player 2's card:  9 of Clubs
    Player 1 Won the Round
    The score is now 10 to 16
    >>> game.declare_winner()
    The score is 10 to 16
    Player 2 Wins!
    """
    def __init__(self):
        """Initializes the function with a shuffled deck and scores of 0 for \
        player 1 and player 2."""
        self.cards=deck()
        self.cards.shuffle()
        self.p1=0
        self.p2=0

    def play_rounds(self, n = 1):
        """Plays n rounds or until the deck is empty and reveals the cards \
        played by each player and who wins each round."""
        for i in range(n):
            if len(self.cards.deck)>1:
                p1c=self.cards.deal_cards(1)[0]
                p2c=self.cards.deal_cards(1)[0]
                print("Player 1's card:  "+p1c.__repr__())
                print("Player 2's card:  "+p2c.__repr__())
                if p1c>p2c:
                    self.p1+=1
                    print('Player 1 Won the Round')
                else:
                    self.p2+=1
                    print('Player 2 Won the Round')
        print("The score is now {0} to {1}".format(self.p1,self.p2))

    def declare_winner(self):
        """Returns the outcome of the rounds played."""
        print("The score is {0} to {1}".format(self.p1,self.p2))
        if self.p1>self.p2:
            print('Player 1 Wins!')
        elif self.p1<self.p2:
            print('Player 2 Wins!')
        else:
            print("It's a Tie!")
