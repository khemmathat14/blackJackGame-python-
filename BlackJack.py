import random
class player(object):

    def __init__(self,bankroll=100):
        self.bankroll = bankroll
        self.score = 0
    
    def add_bankroll(self,amout):
        self.bankroll += amout

    
    def minus_bankroll(self,amout):
        if self.bankroll - amout >0:
            self.bankroll -= amout
        else:
            print("You No Money to Bet")

    def scorePlayer(self,score21=0):
        self.score += score21
        return self.score



    


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
    def drawDeck(self):
        print(self.lst)
        pop_item = self.lst.pop()
        print(pop_item)
        if pop_item == "K" or pop_item == "Q" or pop_item == "J":
            pop_item = 10
            print(pop_item)
        return pop_item



amout = input("Please enter amout to bet : ")
sam = player(100)
sam.bankroll
sam.minus_bankroll(amout)
print(sam.bankroll)



num = input("Enter volum deck: ")
deck1 = setdeck(num)
deck1.createDeck()
deck1.shuffDeck()

def checkA(ch):
    print(type(sam.score))
    if ch == "A" and int(sam.score) > 11:
        sam.scorePlayer(1)
    elif ch == "A" and int(sam.score) <12:
        sam.scorePlayer(10)
    else:
        sam.scorePlayer(ch)
    
    return sam.score

checkA(deck1.drawDeck())
checkA(deck1.drawDeck())
print(sam.score)