
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

    def cmpSort(self, other):
        """
        inputs - card object to compare to self

        returns - 
        1 if suit or rank of self > other
        -1 if suit or rank of self < other
        if self suit == other suit, compare by rank
        if self and other suit and rank are ==, return 0

        This method may be called by the Deck class sort method

        """
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0

    def cmp(self, other):
        """
        inputs - card object to compare to self

        returns -
        1 if suit or rank of self > other
        -1 if suit or rank of self < other
        if self suit == other suit, compare by rank
        if self and other suit and rank are ==, return 0

        This method will be used for comparison operator overloading

        """
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # if self > other: return 1
        #if self < other: return -1
        return 0

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

if __name__ == '__main__':
   pass 