import random
import math

class Player:
    def __init__(self,letter):
        self.letter = letter
    
    def getMove(self,game):
        pass

class ComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def getMove(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def getMove(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn.Box from 0-8.")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise KeyError
                valid_square = True
            
            except KeyError:
                print("Invalid .Try again")
        return val
    