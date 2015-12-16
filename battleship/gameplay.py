class Board(object):
    def __init__(self, player):
        self.player = player
        self.ships = {
            'carrier': Ship(5),
            'battleship': Ship(4),
            'cruiser': Ship(3),
            'cruiser': Ship(3),
            'destroyer': Ship(2)
        }
        self.boardstate_fen

    def initiate_boardstate_fen(self):
        ''' initiates board to string. row is 10 zeros. 10 columns of these rows '''
        boardstate_row = "".join(["0" for i in range(10)])
        boardstate_fen = "/".join([boardstate_row for i in range(10)])
        self.boardstate_fen = boardstate_fen


class Ship(object):
    def __init__(self, length):
        self.length = length
        self.start_row
        self.start_column
        self.orientation

    def initialize_ships(start_row, start_column, orientation):
        self.start_row = start_row
        self.start_column = start_column
        self.orientation = orientation


class Player(object):
    pass


class HumanPlayer(player):
    pass


class ComputerPlayer(player):
    pass


class Game(object):
    def __init__(self, players):
        self.board = Board()
        # players is an array
        self.players = players
        self.turn = 0
        self.curplayer = players[self.turn]

    def change_player(self):
        self.turn = 1 - self.turn

    def setup_ships(self, ship):



board = Board("human")
board.initiate_boardstate_fen()
print board.boardstate_fen
