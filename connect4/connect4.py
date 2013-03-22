# Connect 4
# AFE Python Class Spring 2013
#
# Use Lists to represent positions of X and O's on a 7x6 Board
# [[],[],[],[]]
#
# How do we check for a winning condition (4 in a row up/down/diag)
# [[],['x','x'],['o','x'],['x','o','x'],['o','x','o','x'],[],[]]
#       0             1             2                 3
# Columns are named 1 - 7.
# To take a turn, type the column number you want to add to.  If the column is
# full, you get a message to try again.

class Board(object):
    def __init__(self, columns=7, rows=6):
        self.columns = [[] for x in range(columns)]
        self.rows = rows

    def is_full(self):
        '''Check if all the columns are full.'''
        return all(len(x) == self.rows for x in self.columns)

    def check_winner(self, col):
        '''Checks the board for a 4 in a row connection.'''
        winner = None

        # Check for 4 in a row
        win_count = 0
        row = 0
        col = self.columns[col]

        # Condition 1 - Vertical
        if len(col) >= 4:
            try:
                while win_count < 4:
                    if col[row+1] == col[row]:
                        win_count += 1
                        winner = col[row]
                    else:
                        win_count = 1
                        winner = None
                    row += 1
            except IndexError:
                winner = None
                win_count = 0

        # Condition 2 - Horizontal
        return winner
        # Condition 2 - Horizontal
        # Condition 3 - Z Diagonal
        # Condition 4 - S Diagonal

class Connect4(object):
    def __init__(self, columns=None, rows=None):
        self.board = Board()
        self.players = ["X","O"]
        self.current_player = 0

    def take_turn(self):
        '''Take a turn by slotting an "x" or "o"'''
        current_player = self.players[self.current_player]
        print "Player '{0}', your turn...".format(current_player)
        col = raw_input("Which column deserves an '{0}'??  ".format(current_player))
        self.current_col = int(col)-1
        try:
            target_col = self.board.columns[self.current_col]
        except ValueError:
            print "Oops. Looks like that's not a column number.  Try again."
        except IndexError:
            print "Whoa. That's out of my range. Try again."
        else:
            # Check if the column is full
            if len(target_col) == self.board.rows: # rows is int
                print "Dude. That column is full, brah. Try again."
            else:
                # Add player's chip to the board
                target_col.append(current_player)

                # Switch to the next player
                if self.current_player == 1:
                    self.current_player = 0
                else:
                    self.current_player = 1



    def print_board(self):
        '''prints the board so you can decide your next move.'''
        #   1   2   3   4   5   6   7
        # +===+===+===+===+===+===+===+
        # |   |   |   |   |   |   |   |5
        # | O | O |   |   |   |   |   |4
        # | O | O |   |   |   |   |   |3
        # | O | O |   |   |   |   |   |2
        # | X | X |   |   |   |   |   |1
        # | X | O |   |   |   |   |   |0
        # +===+===+===+===+===+===+===+
        cols = len(self.board.columns)
        rows = self.board.rows

        print " " + " ".join(str(x+1).center(3) for x in range(cols))
        border = "+===" * cols + "+"
        print border
        for r in reversed(range(rows)):
            # 5, 4, 3, 2, 1, 0
            row = []
            # use r as a reverse column index
            for c in range(cols):
                try:
                    value = self.board.columns[c][r].center(3)
                except IndexError:
                    value = "".center(3)
                row.append(value)
            print "|" + "|".join(row) + "|"
        print border
        print

    def check_winner(self):
        '''Checks for a winner.'''
        # Check for a winner
        winner = self.board.check_winner(self.current_col)

        # Check for a draw
        if winner is None and self.board.is_full():
            winner = "draw"

        return winner

    def run(self):
        '''Runs the game until exit or win!'''
        winner = None
        self.print_board()
        while winner is None:
            self.take_turn()
            self.print_board()
            winner = self.check_winner()

        # Break out in two cases
        # Win or Draw
        if winner == "draw":
            print "Yarrr, the cat took the game."
        else:
            print "{0} wins!".format(winner)

if __name__ == "__main__":
    game = Connect4()
    game.run()

