from hand import Hand


def init_test():
    hand1 = Hand()
    assert type(hand1.cards) == list
    print("Hand init method passed")

def getCard_test():
    hand2 = Hand()
    hand2.getCard(3)
    assert hand2.cards == [3]
    print("Hand getCard method passed")

def handSum_test():
    hand3 = Hand()
    hand3.getCard(3)
    hand3.getCard(3)
    assert hand3.handSum() == 6
    print("Hand handSum method passed")


def main():
    init_test()
    getCard_test()
    handSum_test()

if __name__ == '__main__':
    main()
