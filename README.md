# Blackjack
For Blackjack Challenge Week 5
Author:  Ransom V.
Date:  23-Oct-2015

Game logic - 

Deck and card objects are instantiated.
Cards are shuffled.
Player and dealer are dealt a hand with 2 cards.
Dealer's hand is evaluated.  If if it is < 17, program automatically deals another card.
If next card causes the dealer hand to exceed 21, dealer looses game.

If dealer hand is > 16 and < 21, player gets views player hand and decides whether or not to 
take another card.  If next card causes player hand to exceed 21, player looses.

Player can end the game and submit hands for evaluation at any time ater initial deal by
answering 'n' to prompt to take another card.


Files included with this package are - 

blackjack.py - main game logic
deck.py - creates deck class for game
deckTests.py - assertions for deck class
card.py - creates card class
cardTests.py - assertions for card class
hand.py - creates hand class
handTests.py - assertions for hand class
README.md - this readme file
