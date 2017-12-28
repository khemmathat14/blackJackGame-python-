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
    
    def runGame(self):
        nonStop = True
        while nonStop == True:
            playerIn = raw_input("Hit or Stand : ")
            if playerIn == 'HIT' :
                self.checkA(deck1.drawDeck())
                if self.score > 21:
                    print("You score : %s"%(self.score))
                    self.resetScore()
                    break
            elif playerIn == 'STAND':
                #com draw to 17
                while com.score < 17:
                    com.checkA(deck1.drawDeck())
                    if com.score > 21:
                        com.resetScore()
                    break
                break
            print("You score : %s"%(self.score))




    


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
        pop_item = self.lst.pop()
        if pop_item == "K" or pop_item == "Q" or pop_item == "J":
            pop_item = 10
        return pop_item








num = input("Enter volum deck: ")
deck1 = setdeck(num)
deck1.createDeck()
deck1.shuffDeck()
sam = player(100)

gameOn = True

while gameOn == True:
    amout = input("Please enter amout to bet : ")
    sam.minus_bankroll(amout)
    print("You bankroll : %s"%(sam.bankroll))
    sam.firstDraw()
    print("You score : %s" %(sam.score))

    com = player()
    com.firstDraw()
    print("Com score : %s" %(com.score))


    sam.runGame() 


    

    if sam.score == 0 or com.score == 0 :
        print("Bust")
    print("You score : %s" %(sam.score))
    print("Com score : %s" %(com.score))

    #Win
    if sam.score > com.score :
        sam.add_bankroll(amout*2)
    elif sam.score == com.score:
        sam.add_bankroll(amout)

    
    print("You bankroll : %s"%(sam.bankroll))


    if sam.bankroll <= 0:
        print("You no money to bet ")
        break

