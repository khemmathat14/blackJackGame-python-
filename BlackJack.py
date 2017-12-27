import random
class player(object):
    def __init__(self,bankroll=100):
        self.bankroll = bankroll
    
    def add_bankroll(self,amout):
        self.bankroll += amout

    
    def minus_bankroll(self,amout):
        self.bankroll -= amout


sam = player(1000)
sam.bankroll
sam.add_bankroll(123)
sam.minus_bankroll(123)
print(sam.bankroll)


    


class setdeck(object):
    
    #Num set vol use deck
    def __init__(self,num=1):
        self.num = num

    #Create Deck
    def createDeck(self):
        self.lst = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4*self.num    
    
    #ShuffleDeck
    def shuffDeck(self):
        random.shuffle(self.lst)

    #Card use
    def drawDeck(self,first=1):
        print(self.lst)
        for x in range(1,first+1):
            pop_item = self.lst.pop()
            print(pop_item)
        print(self.lst)


num = input("Enter volum deck: ")
deck1 = setdeck(num)
deck1.createDeck()
deck1.shuffDeck()
deck1.drawDeck(1)