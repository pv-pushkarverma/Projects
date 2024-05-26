import random
Deck=[]#Global Deck for all Cards

class Card:
    def __init__(self,value,color):
        self.value=str(value)
        self.color=str(color)

def createCards(color):#Function to generate one color cards
    Deck.append(Card(0,color))
    cards=['1','2','3','4','5','6','7','8','9','+2','Skip','Reverse']
    Deck.extend(Card(value,color) for value in cards for _ in range(2))
    Deck.append(Card('+4','Wild'))
    Deck.append(Card('Wild','Wild'))

colors=['Red','Blue','Green','Yellow']#generate all color cards
for color in colors:
    createCards(color)

'''print(len(Deck)) #Print whole Deck
for card in Deck:
    print(f'{card.value:8s} : {card.color}')'''

class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]

    def giveCards(self):
        random.shuffle(Deck)
        for i in range(7):
            self.cards.append(Deck.pop())
    
    def printCards(self):
        print(f"{self.name}'s Cards are : ")
        for card in self.cards:
            print(f'{card.value}[{card.color}]',end=" , ")
        print("\n")

class Uno(Player):
    def __init__(self):
        self.P1=Player('Computer')
        self.P2=Player(str(input("Enter Player Name : ")))

        self.P1.giveCards()
        self.P2.giveCards()
        self.P1.printCards()
        self.P2.printCards()

        self.Playing=[]
        self.currentCard=Card(2,'Red')

    def drawCard(player,value):
        random.shuffle(Deck)
        v=int(value)
        for i in range(v):
            player.cards.append(Deck.pop())
    
    def changeColor(self,color):
        self.currentCard.color=color
    
    def checkMove(self,card):
        if self.currentCard.color==card.color or self.currentCard.value==card.value or card.color=='Wild':
            return True
        return False
    
    def play(self):
        for i in range(10):
            x=int(input("Input Card Number : "))
            if self.checkMove(self.P2.cards[x+1]):
                print("Valid")
            else:
                print("Invalid")

U=Uno()
U.play()