import time
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)] # it is a single list of 3*3 matrix
        self.current_winner = None  # keep track of winner

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| "+"| ".join(row) +"| ")

    @staticmethod
    def print_num_board():
        num_board = [[str(j) for j in range(i*3,(i+1)*3)]  for i in range(3)]
        for row in num_board:
            print("|"+ "|".join(row)+"|")

    def available_moves(self):
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)
        return moves


    def empty_square(self):
        return " " in self.board

    def num_empty_square(self):
        return self.board.count(" ")

    def make_move(self,square,letter):
        if self.board[square] == " ":
            self.board[square]= letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        row_ind = square // 3   #floor division 
        row = self.board[row_ind * 3 : (row_ind +1) *3]
        if all([spot == letter for spot in row]):
            return True


        col_ind = square % 3
        col = [self.board[col_ind + i *3] for i in range(3)] 
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


        

def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_num_board()

    letter = "x"
    while game.empty_square():
        if letter == "o":
            square = o_player.getMove(game)
        else:
            square = x_player.getMove(game)

        if game.make_move(square,letter):
            if print_game:
                print(letter + f"makes a move to {square}")
                game.printBoard()
                print("")

            if game.current_winner:
                #if print_game:
                print(letter + "wins")
                return letter


            if letter == "x":
                letter = "o"
            else:
                letter = "x"
                
	time.sleep(0.8)
    
    if print_game:
        print("its a tie")

if __name__ == "__main__":
    x_player = HumanPlayer("x")
    o_player = ComputerPlayer("o")
    t = TicTacToe()
    play(t,x_player,o_player,print_game = True)
