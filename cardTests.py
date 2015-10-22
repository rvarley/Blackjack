from card import Card

card1 = Card(1, 1)
card2 = Card(3, 13)
card3 = Card(4, 13)
card4 = Card(3, 14)

print("card1, 1, 1 is: ", card1)
print("card2 3, 13 is: ", card2)
assert card1.__str__() == "Ace of Diamonds"
assert card2.__str__() == "King of Spades"
print("Pretty printing assertions Passed!!!")

assert card1.cmpSort(card2) == -1
assert card2.cmpSort(card1) == 1
assert card2.cmpSort(card2) == 0
print("cmpSort Assertions Passed!!!")

assert card1.cmp(card2) == -1
assert card2.cmp(card1) == 1
assert card2.cmp(card2) == 0
print("Cmp Assertions Passed!!!")

assert bool(card1.rank > card2.rank) == False
assert bool(card1.rank >= card2.rank) == False
assert bool(card1.rank < card2.rank) == True
assert bool(card1.rank <= card2.rank) == True
assert bool(card1.rank == card2.rank) == False
assert bool(card1.rank == card1.rank) == True
print("Comparison overloading assertions passed")