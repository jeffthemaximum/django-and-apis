class Board:
    def __init__(self):
        self.ships = {
            'carrier': Ship(5),
            'battleship': Ship(4),
            'cruiser': Ship(3),
            'cruiser': Ship(3),
            'destroyer': Ship(2)
        }
        self.boardstate_fen = ""

    def initiate_boardstate_fen(self):
        ''' initiates board to string. row is 10 zeros. 10 columns of these rows '''
        boardstate_row = "".join(["0" for i in range(10)])
        boardstate_fen = "/".join([boardstate_row for i in range(10)])
        self.boardstate_fen = boardstate_fen


class Ship:
    def __init__(self, length):
        self.length = length
        self.start_row = ""
        self.start_column = ""
        self.orientation = ""

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
                    start_row = raw_input("What row do you want to put your " + ship_name + " in?")
                    start_column = raw_input("What column do you want to put your " + ship_name + " in?")
                    orientation = raw_input("What direction do you want your " + ship_name + " to point?")
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

print player1.board.boardstate_fen

game.setup_ships()
