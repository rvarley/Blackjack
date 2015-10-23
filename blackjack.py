from deck import Deck
from hand import Hand


def startGame(d_hand, p_hand, deck1):
    """
    Deal initial 2 cards caller
    """
    for i in range(2):
        d_hand.getCard(deck1.drawCard())
        p_hand.getCard(deck1.drawCard())
    


def hitMe(hand, deck):
    """
    Get another card
    Inputs - hand and deck objects

    Returns -  nothing

    """
    hand.getCard(deck.drawCard())

def stand(p_hand, d_hand):
    """
    End game.  Compare hands return game result.

    Arguments - player and dealer hand objects

    Returns - 'Player Wins', 'Dealer Wins or 'Draw'
    """

    PLAYER_WIN = "\n\nPlayer Wins!\n\n\n"
    DEALER_WIN = "\n\nDealer Wins!\n\n\n"
    DRAW = "\n\nGame a draw\n\n\n"
    MAX = 22

    # Tie Game
    if p_hand.handSum() >= MAX and d_hand.handSum() >= MAX:
        return "Both lose.  Both hands over 21."

    if p_hand.handSum() == d_hand.handSum():
        return DRAW

    #  Player Wins
    if p_hand.handSum() > d_hand.handSum() and (
       p_hand.handSum() < MAX):
        return PLAYER_WIN

    if p_hand.handSum() < MAX and d_hand.handSum() >= MAX:
        return PLAYER_WIN

    #  Dealer Wins
    if d_hand.handSum() > p_hand.handSum() and (
       d_hand.handSum() < MAX):
        return DEALER_WIN

    if p_hand.handSum() > d_hand.handSum() and (
       p_hand.handSum() >= MAX):
        return DEALER_WIN


def bust():
    """
    End the game because your hand exceeds 21
    If dealer and player both exceed 21, neither wins
    """
    pass


def evalHand(hand):
    """
    Called to evaluate current hand -  Ace can be either 1 or 11.  This function
    contains logic to determine which value is most advantageous.

    Inputs - hand objects

    Returns - hand score

    """
    print("value of hand in evalHand function is: ", hand.cards)

    if (21 - hand.handSum() >= 10) and (1 in hand.cards):
        for i, elem in enumerate(hand.cards):
            hand.cards(hand.cards.index(1)) == 11  # Change the first ace from value 1
                                                   # to value 11
    # return hand


def main():
    """
    Doc string coming later
    """

    deck1 = Deck()
    deck1.shuffle()

    dealerHand = Hand()
    playerHand = Hand()


    startGame(dealerHand, playerHand, deck1)
    print("dealerHand:  {}.  playerHand: {}  ".format(dealerHand.handSum(),
          playerHand.handSum()))
    print("At start, dealer hand contains: ", dealerHand.showHand())
    print("At start, player hand contains: ", playerHand.showHand())
    while dealerHand.handSum() < 16:
        hitMe(dealerHand, deck1)
        evalHand(dealerHand)
    
    print("Dealer hand before the call to evalHand is: ", dealerHand.showHand())
    evalHand(dealerHand)
    print("dealerHand after call to evalHand is: ", dealerHand.showHand())

    """
        if dealerHand.handSum() > 21:
        game_status = stand(playerHand, dealerHand)
        print("Game status is: ", game_status)
    """
    print("Your hand score is: ", playerHand.handSum())
    ans = input("Do you want another card (y or n)?")

    while ans == 'y':
        hitMe(playerHand, deck1)
        evalHand(playerHand)
        print("Your hand score is: ", playerHand.handSum())
        ans = input("Do you want another card (y or n)?")

    result = stand(playerHand, dealerHand)
    print("Game outcome is:  ", result)

if __name__ == "__main__":
    main()
