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
    def getImage(self):
        "this returns the image name of the particular card"
        suit = self.suit.lower()
        suitIndex = 0
        if suit == 'clubs':
            suitIndex = 0
        elif suit == 'diamonds':
            suitIndex = 1
        elif suit == 'hearts':
            suitIndex = 2
        else:
            suitIndex = 3
        cardIndex = self.val() - 2
        masterImageList = [
        ["2C.png","3C.png","4C.png","5C.png","6C.png","7C.png","8C.png","9C.png","10C.png","JC.png","QC.png","KC.png","AC.png"],
        ["2D.png","3D.png","4D.png","5D.png","6D.png","7D.png","8D.png","9D.png","10D.png","JD.png","QD.png","KD.png","AD.png"],
        ["2H.png","3H.png","4H.png","5H.png","6H.png","7H.png","8H.png","9H.png","10H.png","JH.png","QH.png","KH.png","AH.png"],
        ["2S.png","3S.png","4S.png","5S.png","6S.png","7S.png","8S.png","9S.png","10S.png","JS.png","QS.png","KS.png","AS.png"]
        ]
        return masterImageList[suitIndex][cardIndex]


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
			 'humanForm':[],
			 'imageForm':[],
			 'computer':[],
			 'topcard': "",
			 'topImage':"",
			 'declaredsuit':"",
			 'turn': 0,
			 'gameOver': False,
			 'userWins': False,
			 'computerWins': False,
			 'message': "",
			 'computerMove': "",
			 'needNewSuit' : False,
			 'needComputer' : False,
			 'computerCount' : 7,
			 'isOver': False,
			 }
	game = CrazyEights()
	state['turn'] = 0
	state['human'] = game.cards.drawN(7)
	state['computer'] = game.cards.drawN(7)
	state['pile'] = game.cards.drawN(38)
	state['topcard'] = state['pile'][0]
	state['topImage'] = state['topcard'].getImage()
	state['pile'] = state['pile'][1:]
	count = 1
	for i in state['human']:
		state['humanForm'].append({count: str(i)})
		count +=1
	for i in state['human']:
		state['imageForm'].append(i.getImage())
	#global isHard
	return render_template("start.html",state=state)


@app.route('/play',methods=['GET','POST'])
def crazy8():
	global state
	if request.method == 'GET':
		return play()
	elif request.method == 'POST':
		print(state['human'])
		choice = request.form['text'].lower()
		valids = len(state['humanForm'])
		validList = []
		for i in range(1,valids+1):
			validList.append(i)
		if state['isOver'] == True:
			if choice != "again":
				state['message'] = "Invalid response"
				return render_template('play.html',state=state)
			else:
				return play()
		if state['needNewSuit'] == True:
			if choice == "clubs":
				state['topcard'].suit = "Clubs"
				state['topImage'] = state['topcard'].getImage()
				state['needNewSuit'] = False
				computerPlay()
				return render_template('play.html',state=state)
			elif choice == "diamonds":
				state['topcard'].suit = "Diamonds"
				state['topImage'] = state['topcard'].getImage()
				state['needNewSuit'] = False
				computerPlay()
				return render_template('play.html',state=state)
			elif choice == "hearts":
				state['topcard'].suit = "Hearts"
				state['topImage'] = state['topcard'].getImage()
				state['needNewSuit'] = False
				computerPlay()
				return render_template('play.html',state=state)
			elif choice == "spades":
				state['topcard'].suit = "Spades"
				state['topImage'] = state['topcard'].getImage()
				state['needNewSuit'] = False
				computerPlay()
				return render_template('play.html',state=state)
			else:
				state['message'] = "Invalid Choice"
				return render_template('play.html',state=state)
		elif choice == "draw":
			state['message'] = "You have drawn a card"
			state['human'].append(state['pile'][0])
			state['pile'] = state['pile'][1:]
			state['humanForm'].append({len(state['humanForm'])+1: str(state['human'][len(state['human'])-1])})
			reForm(state['human'])
			return render_template('play.html',state=state)
		choiceVal = 0
		try:
			choiceVal = int(choice)
		except ValueError:
			state['message'] = "invalid choice"
			return render_template('play.html',state=state)
		if choiceVal not in validList:
			state['message'] = "invalid choice"
			return render_template('play.html',state=state)
		else:
			selection = state['human'][int(choice)-1]
			print(selection.val())
			if int(selection.val()) == 8:
				state['needNewSuit'] = True
				state['pile'].insert((len(state['pile'])+1), selection)
				state['human'].remove(selection)
				#state['humanForm'].pop(int(choice)-1)
				reForm(state['human'])
				state['topcard'] = selection
				#state['topcard'].suit = "You decide"
				if state['human'] == []:
					state["message"] = "you won!"
					state['isOver'] = True
				return render_template('play.html',state=state)
			elif selection.value == state['topcard'].value:
				state['pile'].insert((len(state['pile'])+1), selection)
				state['human'].remove(selection)
				#state['humanForm'].pop(int(choice)-1)
				reForm(state['human'])
				state['topcard'] = selection
				state['topImage'] = state['topcard'].getImage()
				if state['human'] == []:
					state["message"] = "you won!"
					state['isOver'] = True
					return render_template('play.html',state=state)
				computerPlay()
				return render_template('play.html',state=state)
			elif selection.suit.lower() == state['topcard'].suit.lower():
				state['pile'].insert((len(state['pile'])+1), selection)
				state['human'].remove(selection)
				#state['humanForm'].pop(int(choice)-1)
				reForm(state['human'])
				state['topcard'] = selection
				state['topImage'] = state['topcard'].getImage()
				if state['human'] == []:
					state["message"] = "you won!"
					state['isOver'] = True
					return render_template('play.html',state=state)
				computerPlay()
				return render_template('play.html',state=state)
			elif selection.suit.lower() != state['topcard'].suit.lower() and selection.value != state['topcard'].value:
				state['message'] = "can't play that card"
				return render_template('play.html',state=state)
            #elif selection.suit.lower() == state['topcard'].suit.lower():

def computerPlay():
	global state
	for answer in state['computer']:
		already = False
		if answer.suit.lower() == state['topcard'].suit.lower():
			if answer.val() == 8:
				suitList = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
				newSuit = random.choice(suitList)
				state['message'] = "Computer has put down and 8 and declared the suit to be " + newSuit
				already = True
			state['pile'].insert((len(state['pile'])+1),answer)
			state['computer'].remove(answer)
			if already == False:
				state['message'] = "Computer has put down " + answer.__str__()
			state['topcard'] = answer
			state['topImage'] = state['topcard'].getImage()
			if already == True:
				state['topcard'].suit = newSuit
				state['topImage'] = state['topcard'].getImage()
			state['computerCount'] = len(state['computer'])
			if state['computer'] == []:
				state['message'] = "You lost"
				state['isOver'] = True
			return None
		elif answer.value == state['topcard'].value:
			state['message'] = "Computer put down " + answer.__str__()
			if answer.val() == 8:
				suitList = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
				newSuit = random.choice(suitList)
				state['message'] = "Computer has put down and 8 and declared the suit to be " + newSuit
				already = True
			state['pile'].insert((len(state['pile'])+1),answer)
			state['computer'].remove(answer)
			if already == False:
				state['message'] = "Computer has put down " + answer.__str__()
			state['topcard'] = answer
			state['topImage'] = state['topcard'].getImage()
			state['computerCount'] = len(state['computer'])
			if state['computer'] == []:
				state['message'] = "You lost"
				state['isOver'] = True
			return None
	else:
		state['computer'].append(state['pile'][0])
		state['pile'] = state['pile'][1:]
		computerPlay()
	return None

def reForm(oldList):
	state['humanForm'] = []
	count = 1
	for i in oldList:
		state['humanForm'].append({count: str(i)})
		count +=1
	state['imageForm'] = []
	for i in state['human']:
		state['imageForm'].append(i.getImage())
	return None

		#return render_template('play.html',state=state)

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
