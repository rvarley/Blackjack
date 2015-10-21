import random
import itertools  # see islice and link

# Credits - http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap15.html
# for card and deck classes


class Card:
    """
    Means of generating generating and dealing with individual cards
    Deck class defines a list of tuples corresponding suit and rank.  
    Cards will be sorted by rank only.
    Rank values are strings 1 - 13.  
    Ace - 1
    Jack - King are 11 - 13 

    Suites are:
    Spades ->   3
    Hearts ->   2
    Diamonds -> 1
    Clubs ->    0

    Number is a value between 0 - 52 and is used for sorting cards
    """
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["filler", "Ace", "2", "3", "4", "5", "6", "7",
                "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return(self.rankList[self.rank] + " of " +
               self.suitList[self.suit])

if __name__ == '__main__':
   pass 