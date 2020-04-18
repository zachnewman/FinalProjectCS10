"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import crazyeights_app
app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
	return render_template('hangman.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/play',methods=['GET','POST'])
def play():
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
	state['turn'] = 0
    state['human'] = crazyeights_app.self.cards.drawN(7)
    state['computer'] = crazyeights_app.self.cards.drawN(7)
    state['pile'] = crazyeights_app.self.cards.drawN(38)
    state['topcard'] = pile[0]
    state['pile'] = state['pile'][1:]
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
