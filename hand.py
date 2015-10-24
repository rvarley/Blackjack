
from deck import Deck

# Class object instantiates a hand


class Hand(Deck):

    def __init__(self):
        """ cards is an array of integers representing card rank.
        Suit isn't needed for blackjack
        A newly instantiated hand object contains an empty list to hold integers representing
        the ranks of cards contained in the hand
        """
        self.cards = []

    def getCard(self, card):
        """
        Input - a deck attribute in the form card_object.drawCard()

        Returns - an list of integers representing card rank

        ex. hand1.getCard(deck1.drawCard())

        """

        return self.cards.append(card)

    def handSum(self):
        """
        Arguments - hand -  list of integer values representing card ranks contained in hand

        Returns - An integer equalling the sum of rank values in the cards list

        ex. hand1.handSum(hand1.cards)

        """

        return sum(self.cards)

    def showHand(self):
        """
        Shows the entire cards array for the hand object.
        Inputs - none

        Outputs - List containing card values
        """
        return self.cards

 
