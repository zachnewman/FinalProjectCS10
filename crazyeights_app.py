"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""

from Cards_and_Deck import Card
from Cards_and_Deck import Deck
import random

class CrazyEights:
    def __init__(self):
        self.cards = Deck()
        self.cards.shuffle()

    def user_wins_function(self):
        print("You Win!")
        print("Refresh the Page to Play Again!")
        return True

    def computer_wins_function(self):
        print("You Lost!")
        print("Refresh the Page to Play Again!")
        return True

    def sortValue(self,x):
        sortvalue = Card.val(x)
        return sortvalue

    def sortSuit(self,x):
        return x.suit

    def print_human_hand(self):
        global human
        count = 0
        human.sort(key=b.sortValue)
        human.sort(key=b.sortSuit)
        print("")
        print("--------------------")
        print("TURN",turn)
        print("")
        print("Human Player's Hand:")
        print("--------------------")
        for x in human:
            count += 1
            print("Choice",count,end="")
            print(": ",end="")
            print(x)
        print("")
        print("TURN OPTIONS:")
        print("- Play a card")
        if pile != []:
            print("- Draw a card")
        print("--------------------")

    def human_playhand(self):
        global declaredsuit
        global human
        global pile
        global topcard
        while pile != []:
            self.print_human_hand()
            while True:
                choice = input("Type the number of the Choice you would like or type 'draw' to draw a card.")
                if choice.lower() == "draw":
                    print("Human Player draws a card.")
                    print("The top card is",topcard)
                    human.append(pile[0])
                    pile = pile[1:]
                    continue
                try:
                    int(choice)
                except ValueError:
                    continue
                if int(choice) > len(human):
                    continue
                break
            answer = human[int(choice)-1]
            if answer.suit.lower() == topcard.suit.lower():
                if answer.value == "8":
                    while True:
                        declaredsuit = input("Declare a suit: Clubs, Diamonds, Hearts, or Spades.")
                        if declaredsuit.lower() not in "clubs diamonds hearts spades".split():
                            print("Please select a valid suit.")
                            continue
                        print("Human Player declares the suit",declaredsuit)
                        break
                pile.insert((len(pile)+1),answer)
                human.remove(answer)
                return answer
            elif answer.value == topcard.value:
                if answer.value == "8":
                    while True:
                        declaredsuit = input("Declare a suit: Clubs, Diamonds, Hearts, or Spades.")
                        if declaredsuit.lower() not in "clubs diamonds hearts spades".split():
                            print("Please select a valid suit.")
                            continue
                        print("Human Player declares the suit",declaredsuit)
                        break
                pile.insert((len(pile)+1),answer)
                human.remove(answer)
                return answer
            else:
                print("")
                print("")
                print("MESSAGE:")
                print("That card cannot be played here.")
                print("")
                print("")
                continue


    def computer_playhand(self):
        global declaredsuit
        global computer
        global pile
        global topcard
        while pile != []:
            print("Computer Player has",len(computer),"cards.")
            for answer in computer:
                if answer.suit.lower() == topcard.suit.lower():
                    print("Computer Player put down",answer)
                    print("")
                    if answer.value == "8":
                        suitlist = ['Clubs','Hearts','Diamonds','Spades']
                        declaredsuit = random.choice(suitlist)
                        print("Computer Player has declared the suit",declaredsuit)
                    pile.insert((len(pile)+1),answer)
                    computer.remove(answer)
                    return answer
                elif answer.value == topcard.value:
                    print("Computer Player put down",answer)
                    print("")
                    if answer.value == "8":
                        suitlist = ['Clubs','Hearts','Diamonds','Spades']
                        declaredsuit = random.choice(suitlist)
                        print("Computer Player has declared the suit",declaredsuit)
                    pile.insert((len(pile)+1),answer)
                    computer.remove(answer)
                    return answer
            print("Computer Player draws a card.")
            computer.append(pile[0])
            pile = pile[1:]
            continue


    def play(self):
        global finalCount
        global human
        global computer
        global pile
        global topcard
        global turn
        global declaredsuit
        turn = 0
        human = self.cards.drawN(7)
        computer = self.cards.drawN(7)
        pile = self.cards.drawN(38)
        topcard = pile[0]
        pile = pile[1:]
        while True:
            turn += 1
            print("Current Top Card:",topcard)
            topcard = self.human_playhand()
            if topcard.value == "8":
                topcard.suit = declaredsuit
            print("")
            print("Human Player put down",topcard)
            print("")
            if human == []:
                gameOver = self.user_wins_function()
                if gameOver == True:
                    return
            topcard = self.computer_playhand()
            if topcard.value == "8":
                topcard.suit = declaredsuit
            if computer == []:
                gameOver = self.computer_wins_function()
                if gameOver == True:
                    return
            continue






if __name__ == '__main__':
    play_hangman()
