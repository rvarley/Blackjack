
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

            Outputs - Tuple containing rank and suit of card at self.cards[index]
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

    def drawCardRank(self):
        """ 
        Called when initial 2 cards are dealt and if player or dealer request additional cards
        Arugments - none

        Returns - A card from the top of the deck

        """
        return self.cards.pop().rank

    def drawCardSuitRank(self):
        """ 
        Called when initial 2 cards are dealt and if player or dealer request additional cards
        Arugments - none

        Returns - A card from the top of the deck

        """
        return self.cards.pop().suit, self.cards.pop().rank

    def sortDeck(self):
        """
        Arguments - A deck object.
        Returns - A deck deck sorted by suit and value.

        Questions - Why is this necessary?  Does the deck need to be sorted even when it is missing cards?
        """

if __name__ == '__main__':
    pass
    # print("tests might go here if script file were run as python deck.py")
