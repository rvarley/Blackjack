from deck import Deck

deck1 = Deck()

assert (len(deck1.cards)) == 52
assert deck1.cards[0].__str__() == "Ace of Clubs"
assert deck1.cards[51].__str__() == "King of Spades"
assert deck1.printCard(0) == (1, 0)
print("Assertions for Deck __init__ Passed!!!")

assert deck1.cardsLeft() == 52
temp = deck1.drawCard()
assert deck1.cardsLeft() == 51
temp = deck1.drawCard()
# print("num cards left is: ", deck1.cardsLeft())
assert deck1.cardsLeft() == 50
print("Assertions for cardsLeft passed!!!")

deck1 = Deck()
# Draw card converts Jack - King to value 10, so we need to pop until
# Rank 9 for assertion to work
deck1.drawCard()
deck1.drawCard()
deck1.drawCard()
deck1.drawCard()
assert deck1.drawCard() == (9)
assert deck1.drawCard() != (9)  # Shouldn't be king of spades after previous pop
print("Assertions for drawCard Passed!!!")
