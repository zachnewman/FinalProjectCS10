"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

import random
class Card:
    """ Card represents a standard playing card """

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)

    def __repr__(self):
        return 'Card("'  +  self.suit +  '","'  +  self.value +  '")'

    def __eq__(self,other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.suit == other.suit and self.value==other.value
        return False

    def val(self):
        """ this returns the numeric value of a card """
        if self.value in "2 3 4 5 6 7 8 9 10".split():
            return int(self.value)
        elif self.value == "J":
            return 11
        elif self.value == "Q":
            return 12
        elif self.value == "K":
            return 13
        elif self.value == "A":
            return 14


class Deck:
    """ this represents a deck of cards """
    def __init__(self):
        self.cards = self._createDeck()
        self.discards = []

    def _createDeck(self):
        cards = []
        for suit in "Hearts Spades Diamonds Clubs".split():
            for value in "A 2 3 4 5 6 7 8 9 10 J Q K".split():
                cards.append(Card(suit,value))
        return cards

    def shuffle(self):
        """ shuffle the deck in place """
        random.shuffle(self.cards)

    def draw(self):
        """ remove top card from the deck and put in discards
            and return that top card
        """
        c = self.cards[0]
        self.cards = self.cards[1:]
        self.discards.append(c)
        return(c)

    def drawN(self,n):
        """ this returns a list of the first n cards in the deck
            and it moves them from d.cards to d.discards
        """
        c = self.cards[:n]
        self.cards = self.cards[n:]
        self.discards += c
        return(c)


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

#import random

from flask import Flask, render_template, request
#import crazyeights_app
#import Cards_and_Deck
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/about')
def about():
	return render_template('about.html')
"""
THIS IS WHERE WE INITIALIZE THE CARDS AND TELL THE PLAYER ABOUT THE GAME
"""
@app.route('/start')
def play():
	#import crazyeights_main
	#exec(open('crazyeights_main.py').read())
	#exec(open('crazyeights_app.py').read())
	#print(isHard)
	global state
	state = {'pile':[],
			 'human':[],
			 'computer':[],
			 'topcard': "",
			 'declaredsuit':"",
			 'turn': 0,
			 'gameOver': False,
			 'userWins': False,
			 'computerWins': False,
			 'message': ""
			 }
	game = CrazyEights()
	state['turn'] = 0
	state['human'] = game.cards.drawN(7)
	state['computer'] = game.cards.drawN(7)
	state['pile'] = game.cards.drawN(38)
	state['topcard'] = state['pile'][0]
	state['pile'] = state['pile'][1:]
	print(state)
	#global isHard
	return render_template("start.html",state=state)


@app.route('/play',methods=['GET','POST'])
def crazy8():




	while True:
		state['turn'] += 1
		print("Current Top Card:",state['topcard'])
		state['topcard'] = crazyeights_app.self.human_playhand()
		if state['topcard'].value == "8":
			state['topcard'].suit = state['declaredsuit']
		print("")
		print("Human Player put down",state['topcard'])
		print("")
		if state['human'] == []:
			state['gameOver'] = True
			state['userWins'] = True
			return
		state['topcard'] = crazyeights_app.self.computer_playhand()
		if state['topcard'].value == "8":
			state['topcard'].suit = state['declaredsuit']
		if state['computer'] == []:
			state['gameOver'] = True
			state['computerWins'] = True
			return
		continue
	return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
