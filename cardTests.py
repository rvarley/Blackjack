from card import Card

card1 = Card(1, 1)
card2 = Card(3, 13)
card3 = Card(4, 13)
card4 = Card(3, 14)
print("card1, 1, 1 is: ", card1)
print("card2 3, 13 is: ", card2)
assert card1.__str__() == "Ace of Diamonds"
assert card2.__str__() == "King of Spades"
# The following 2 asserts will be added as an enhancement - time permitting
# assert card3.__str__() == "Suit out of range"  
# assert card4.__str__() == "Rank out of range"
print("Assertions Passed!!!")
