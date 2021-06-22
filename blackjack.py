from urllib.request import urlopen
import random
import json



url = "http://nav-deckofcards.herokuapp.com/shuffle"

# open connection and read JSON data
response = urlopen(url)
data_json = json.loads(response.read())

#value mapping
values = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}

#player object
class player:
    def __init__(self,name):
        self.name = name
        self.cards = list()
        self.score = 0

#card object
class card:
    def __init__(self,suite,value):
        self.suite = suite
        self.value = value

#prints name, score and cards of a player
def print_result(player):

    print(player.name + " |" + str(player.score) + "| ", end = " ")

    for x in player.cards[:-1]:
        print(x.suite[0] + x.value,end = ",") #suite is a list with one element, so suite[0]

    if len(player.cards) > 0:#if player 1 wins before player 2 can draw cards, this need to be checked
        print(x.suite[0] + player.cards[-1].value)
    else:
        print("None")


#check if winner has been decided after a player is done drawing a card
def check_winner(draw,opponent):

    if draw.score == 21:
        print(draw.name + " wins\n")
        print_result(player1)
        print_result(player2)
        exit()

    elif draw.score > 21:
        print(opponent.name + " wins\n")
        print_result(player1)
        print_result(player2)
        exit()


#handles drawing a card from the pile
def draw_card(player,deck):
    player.cards.append(deck.pop(0))#remove from pile and add to hadnd
    player.score = player.score + values[player.cards[-1].value] #update score
    print(player.name + " drew a " + player.cards[-1].suite + " " + player.cards[-1].value + "  (value " + str(values[player.cards[-1].value]) + ")" ) #print info




deck = list()

for x in data_json: #create deck from JSON data
    deck.append(card(x["suit"],x["value"]))

random.shuffle(deck) #shuffle the deck


player1 = player("Marit")#create playter

print("What is your name ?")# get name from user
player2 = player(input())
print("Hello " + player2.name + "\n")




while True:

    print(player2.name + " draws 2 cards") #user draws 2 cards

    draw_card(player2,deck)
    draw_card(player2,deck)
    check_winner(player2,player1) #check if player1 has won

    print("\n")
    print(player1.name + " draws 2 cards") #Marit draws 2 cards
    draw_card(player1,deck)
    draw_card(player1,deck)

    check_winner(player1,player2)#check if Marit has won


    print("\n\n" + player2.name + " is drawing\n")

    while player2.score < 17: #user automatically draws cards untill score is more than 17

        draw_card(player2,deck)#user draws a card
        print(player2.name + " score is " + str(player2.score) + "\n")#print info

    check_winner(player2,player1)#check if user has won on lost


    print("\n\n" + player1.name + " is drawing\n")

    while player1.score < player2.score+1: #Marit draws card untill her score is higher than the users

        draw_card(player1,deck)#Marit draws a card
        print(player1.name + " score is " + str(player1.score) + "\n")#print info


    check_winner(player1,player2)#Check if Marit has won or lost


    #if the game has not yet been decided, the player with the higest score wins
    if player1.score > player2.score:
        print(player1.name + " wins\n")
        print_result(player1)
        print_result(player2)
        exit()
    else:
        print(player2.name + " wins\n")
        print_result(player1)
        print_result(player2)
        exit()
