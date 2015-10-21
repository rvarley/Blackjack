from deck import Deck
from card import Card

deck1 = Deck()
# deck1.printDeck()  # prints out ... list of lists??
# print(deck1.cards[0].rank) # Prints the numeric rank of deck1.cards[0].rank
print(deck1.printCard(0))
for i in range(52):
    print("deck1 is: ", deck1.cards[i])  # prints all the cards as '$rank of $suit' 
# print("deck1.cards is: ", deck1.cards) # deck1.cards prints <card.Card object at 0x1006a69e8> 52 times
# print("deck1.cards type is: ", type(deck1.cards)) # deck1.cards type is list
# var1 = deck1.cards[0]
# print(var1) # prints Ace of Clubs

assert (len(deck1.cards)) == 52
assert deck1.cards[0].__str__()== "Ace of Clubs"
assert deck1.cards[51].__str__()== "King of Spades"
assert deck1.printCard(0) == (1, 0)
print("Assertions for Deck __init__ Passed!!!")

assert deck1.drawCardRank() == (13)
assert deck1.drawCardRank() != (13)  # Shouldn't be king of spades after previous pop
print("Assertions for drawCardRank Passed")

print("About to shuffle and print deck again . . . ")

deck1.shuffle()
for i in range(len(deck1.cards)):
    print("deck1 is: ", deck1.cards[i])

print("drawCardRank returns: ", deck1.drawCardRank())
var1 = deck1.drawCardRank()
var2 = deck1.drawCardSuitRank()
print("Value of drawCardRank is {} and drawCardSuitRank is {}".format(var1, var2))



