import sys


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Board:
    def __init__(self):
        self.ships = {
            'carrier': Ship(5),
            'battleship': Ship(4),
            'cruiser': Ship(3),
            'cruiser': Ship(3),
            'destroyer': Ship(2)
        }

    def initiate_boardstate_fen(self):
        ''' initiates board to string. row is 10 zeros. 10 columns of these rows '''
        boardstate_row = "".join(["0" for i in range(10)])
        boardstate_fen = "/".join([boardstate_row for i in range(10)])
        self.boardstate_fen = boardstate_fen

    def print_board(self):
        # print first row
        sys.stdout.write("  ")
        for i in range(ord('A'), ord('K')):
            sys.stdout.write(Color.UNDERLINE + chr(i) + Color.END)
        print ""

        #print rows
        for i in range(10):
            sys.stdout.write(str(i))
            sys.stdout.write("|")
            for i in range(11):
                if i != 10:
                    sys.stdout.write(self.boardstate_fen[i])
            print ""

class Ship:
    def __init__(self, length):
        self.length = length

    def initialize_ship(self, start_row, start_column, orientation):
        self.start_row = start_row
        self.start_column = start_column
        self.orientation = orientation


class Player:
    def __init__(self):
        self.board = Board()


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.player_type = 'Human'


class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.player_type = 'Computer'


class Game:
    def __init__(self, players):
        # players is an array
        self.players = players
        self.turn = 0
        self.curplayer = players[self.turn]

    def change_player(self):
        self.turn = 1 - self.turn

    def setup_ships(self):
        '''ships should be the array from Board.ships'''
        for player in self.players:
            if player.player_type == 'Human':
                for ship_name, ship_object in player.board.ships.iteritems():
                    start_row = raw_input("What row do you want to put your " + ship_name + " in? ")
                    start_column = raw_input("What column do you want to put your " + ship_name + " in? ")
                    orientation = raw_input("What direction do you want your " + ship_name + " to point? ")
                    ship_object.initialize_ship(start_row=start_row, start_column=start_column, orientation=orientation)
            else:
                # computer players
                pass

# making players also makes boards
# making board also makes ships
player1 = HumanPlayer()
player2 = HumanPlayer()

# game needs an array of players
game = Game([player1, player2])

# setup and print board for player1
player1.board.initiate_boardstate_fen()
player1.board.print_board()

game.setup_ships()
