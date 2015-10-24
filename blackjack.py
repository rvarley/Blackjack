from deck import Deck
from hand import Hand
import os


def startGame(d_hand, p_hand, deck1):
    """
    Deal initial 2 cards to dealer and player

    Arguments - dealer and player hand objects, deck object

    Returns - Nothing
    """
    NUM_CARDS = 2

    for i in range(NUM_CARDS):
        d_hand.getCard(deck1.drawCard())
        p_hand.getCard(deck1.drawCard())


def hitMe(hand, deck):
    """
    Move another card from the deck object to the hand object.
    Inputs - hand and deck objects

    Returns - True if deck has cards left.  False if deck has no cards left.

    Side effects - Card removed from deck object and added to hand object.

    """
    if deck.cardsLeft == 0:
        return False
    hand.getCard(deck.drawCard())
    return True


def stand(p_hand, d_hand):
    """
    End game.  Compare hands return game result.

    Arguments - player and dealer hand objects

    Returns - String 'Player Wins', 'Dealer Wins or 'Draw'
    """

    PLAYER_WIN = "Player Wins!\n\n\n"
    DEALER_WIN = "Dealer Wins!\n\n\n"
    DRAW = "Game a draw\n\n\n"
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


def displayHands(p_hand, d_hand):
    """
    Displays cards and sum of cards in player and dealer hands.

    Arguments:  player and dealer hand objects

    Returns: Nothing

    Prints a formatted string showing player hand and score and dealer hand and score.
    """
    os.system('clear')  # Call to OS clear the screen to clean up output
    print("\nPlayer hand: ", p_hand.showHand())
    print("Player score: ", p_hand.handSum())

    print("\nDealer hand: ", d_hand.showHand())
    print("Dealer score: ", d_hand.handSum())


def evalHand(hand):
    """
    Called to evaluate current hand -  Ace can be either 1 or 11.  This function
    contains logic to determine which value is most advantageous.

    Inputs - hand objects

    Returns - hand score

    """
    # os.system("clear")
    #print("dealer hand before evalHand is: ", hand.showHand())
    if (1 in hand.cards) and (21 - hand.handSum() >= 10):
        print("found a 1 value Ace in the hand")
        hand.cards[hand.cards.index(1)] = 11  # Change the first ace from value 1
                                              # to value 11
    if (11 in hand.cards) and (hand.handSum() >= 22):
        print("found an 11 value Ace in the hand and sum > 21")
        hand.cards[hand.cards.index(11)] = 1  # Change the first ace from value 1
                                              # to value 11


def main():
    """
    Doc string coming later
    """

    deck1 = Deck()
    deck1.shuffle()

    dealerHand = Hand()
    playerHand = Hand()

    startGame(dealerHand, playerHand, deck1)
    while dealerHand.handSum() < 16:
        evalHand(dealerHand)
        hitMe(dealerHand, deck1)
        # print("dealer hand after evalHand is: ", dealerHand.showHand())
    if dealerHand.handSum() > 21:
        os.system("clear")
        displayHands(playerHand, dealerHand)
        print("Dealer sum exceeded 21."
              " Dealer hand {}.  Dealer sum {}.  Player wins!!".format(dealerHand.handSum(), dealerHand.showHand()))
        return

    displayHands(playerHand, dealerHand)
    evalHand(dealerHand)

    """
        if dealerHand.handSum() > 21:
        game_status = stand(playerHand, dealerHand)
        print("Game status is: ", game_status)
    """
    # print("\nYour hand score is: ", playerHand.handSum())
    displayHands(playerHand, dealerHand)
    ans = input("\nDo you want another card (y or n)? ")

    while ans == 'y':
        hitMe(playerHand, deck1)
        evalHand(playerHand)
        displayHands(playerHand, dealerHand)
        if playerHand.handSum() > 21:
            os.system("clear")
            displayHands(playerHand, dealerHand)
            print("Player exceeded 21.  "
                "Player hand {}. Dealer sum {}.  Dealer wins!!".format(playerHand.showHand(), playerHand.handSum()))
            return
        ans = input("Do you want another card (y or n)?")

    displayHands(playerHand, dealerHand)
    print("\nGame outcome is:  ", stand(playerHand, dealerHand))

if __name__ == "__main__":
    main()
