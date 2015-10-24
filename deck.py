
# import itertools  # see islice and link
from card import Card


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def printDeck(self):
        for card in self.cards:
            print(card.suit, card.rank)

    def printCard(self, index):
        """ Input - interger value to index into a deck of cards

            Returns - Tuple containing rank and suit of card at self.cards[index]
        """
        return (self.cards[index].rank, self.cards[index].suit)

    def shuffle(self):
        """ Takes a deck object and shuffles it into random order
        Arguments - a deck object
        Returns - a deck object shuffeled in random order

        """
        import random
        nCards = len(self.cards)
        for i in range(nCards):
            j = random.randrange(i, nCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def drawCard(self):
        """
        Called when initial 2 cards are dealt and if player or dealer request additional cards
        Arugments - none

        Returns - A card tuple from the top of the deck
        """
        card = self.cards.pop().rank
        if card > 10:
            card = 10  # converts jack, queen, king values to 10
        return card

    """ May not need this function
    def drawCardSuitRank(self):
        Called when initial 2 cards are dealt and if player or dealer request additional cards
        Arugments - none

        Returns - A card tuple of Suit and Rank from the top of the deck

        return self.cards.pop()
        """

    def cardsLeft(self):
        """
        Arguments - None.

        Returns and integer value equal to the number of cards currently in the deck.

        Method can be used to test if the deck is empty prior to calling drawCard.
        """
        return len(self.cards)

    def mergSortDeck(self, num):
        """
        Arguments - A deck object.

        Returns - A deck deck sorted by suit and value.

        This method is not currently working 

        """
        # n = len(self.cards)
        n = num
        print("value of n before div 2 is: ", n)
        if n > 1:
            m = n // 2
            print("value of n after div 2 is: ", n)
            nums1, nums2 = (self.cards[:m]), (self.cards[m:])
            # print("value of nums1 and nums2 are: ", nums1, nums2)
            return self.sortDeck(n)
            return self.sortDeck(n)
            self.merge(nums1, nums2)

    def merge(lst1, lst2, self):
        i1, i2, i3 = 0, 0, 0
        n1, n2 = len(lst1), len(lst2)

        while i1 < n1 and i2 < n2:
            if lst1[i1].rank < lst2[i2].rank:
                self.cards[i3] = lst1[i1]
                i1 = i1 + 1
            else:
                self.cards[i3] = lst2[i2]
                i2 = i2 + 1
            i3 = i3 + 1
        while i1 < n1:
            self.cards[i3] = lst1[i1]
            i1 = i1 + 1
            i3 = i3 + 1

        while i2 < n2:
            self.cards[i3] = lst2[i2]
            i2 = i2 + 1
            i3 = i3 + 1

    def sortDeck(self):
        """
        Function to use built in sort to sort deck by rank only.

        Inputs - Deck object

        Returns - None

        Side effects - Sorts calling deck object by rank.
        """
        self.cards.sort()

if __name__ == '__main__':
    pass
    # print("tests might go here if script file were run as python deck.py")
