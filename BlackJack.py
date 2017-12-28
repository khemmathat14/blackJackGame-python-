import random
class player(object):

    def __init__(self,bankroll=0):
        self.bankroll = bankroll
        self.score = 0
    
    def add_bankroll(self,amout):
        self.bankroll += amout

    
    def minus_bankroll(self,amout):
        if self.bankroll - amout >=0:
            self.bankroll -= amout
        else:
            print("You No Money to Bet")

    def scorePlayer(self,score21=0):
        self.score += score21
        return self.score

    def checkA(self,ch):
        print(type(self.score))
        if ch == "A" and int(self.score) > 11:
            self.scorePlayer(1)
        elif ch == "A" and int(self.score) <12:
            self.scorePlayer(10)
        else:
            self.scorePlayer(ch)
        return sam.score

    def resetScore(self):
        self.score = 0

    def firstDraw(self):
        self.checkA(deck1.drawDeck())
        self.checkA(deck1.drawDeck())




    


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
sam.minus_bankroll(amout)
print(sam.bankroll)

com = player()



num = input("Enter volum deck: ")
deck1 = setdeck(num)
deck1.createDeck()
deck1.shuffDeck()




sam.firstDraw()
print(sam.score)


com.firstDraw()
print(com.score)


nonStop = True
while nonStop == True:
    playerIn = raw_input("Hit or Stand : ")
    print(playerIn)
    if playerIn == 'HIT' :
        sam.checkA(deck1.drawDeck())
        if sam.score > 21:
            print(sam.score)
            print("Bust You Lose")
            sam.resetScore()
            break
    elif playerIn == 'STAND':
        while com.score < 17:
            com.checkA(deck1.drawDeck())
            if com.score > 21:
            com.resetScore()
            break
        break
    print(sam.score)


 


print(com.score)
print(sam.score)

#Win
if sam.score > com.score :
    sam.add_bankroll(amout*2)

print(sam.bankroll)