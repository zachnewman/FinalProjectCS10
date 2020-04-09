"""
    War is the classic (and boring) card game
    The goal is to gain all of the cards.
    The rules are that each player puts down their top card
    The high card takes all and puts them at the bottom of their hand
    For a tie, you repeat until someone has a high card.
    Typically you say at the beginning how many "battles" you will play

"""
from Deck import Deck

class War:
    def __init__(self,max_battles=10):
        deck = Deck()
        deck.shuffle()
        self.hand1 = deck.drawN(26)
        self.hand2 = deck.drawN(26)
        self.discards = []
        self.battles = 1
        self.max_battles = max_battles
    def play_one_battle(self):
        print("====================")
        print("Battle Number",self.battles)
        self.battles += 1
        card1 = self.hand1[0]
        self.hand1=self.hand1[1:]
        card2 = self.hand2[0]
        self.hand2 = self.hand2[1:]
        self.discards += [card1,card2]
        print("Player 1 has",len(self.hand1), "cards and plays",card1)
        print("Player 2 had",len(self.hand2), "cards and plays",card2)
        if (card1.val()>card2.val()):
            print("Player 1 wins the battle")
            self.hand1 += self.discards
            self.discards = []
        elif (card1.val()<card2.val()):
            print("Player 2 wins the battle")
            self.hand2 += self.discards
            self.discards=[]
        if self.battles > self.max_battles:
            return True
        else:
            return len(self.hand1)==0 or len(self.hand2)==0

    def play_game(self):
        done = False
        while not done:
            done = self.play_one_battle()
        if (self.hand1==[]):
            print("Player 2 won!")
        else:
            print("Player 1 won!")


if __name__=="__main__":
    print("You can watch a game of War!")
    battles = int(input("How many battles? "))
    w = War(battles)
    w.play_game()
