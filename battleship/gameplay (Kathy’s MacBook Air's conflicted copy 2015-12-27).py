import sys
import pudb


# Define a class inherit from an exception type
class CustomError(Exception):
    def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg


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
            'carrier': Ship(length=5, sid=5),
            'battleship': Ship(length=4, sid=4),
            'cruiser1': Ship(length=3, sid=3),
            'cruiser2': Ship(length=3, sid=2),
            'destroyer': Ship(length=2, sid=1)
        }
        self.rows_as_list = self.instantiate_rows_as_list()
        self.rows_as_dict = self.instantiate_rows_as_dict()

    def instantiate_rows_as_dict(self):
        rows = {}
        for i in range(10):
            rows[i] = {}
            for j in range(10):
                rows[i][j] = 0
        return rows

    def instantiate_rows_as_list(self):
        rows = [[] for x in range(10)]
        for i in range(10):
            for j in range(10):
                rows[i].append([])
                rows[i][j] = 0
        return rows

    def map_fen_helper(self, x):
        if isinstance(x, int):
            return str(x)
        else:
            return str(x[1])

    def make_boardstate_fen(self):
        ''' initiates board to string. row is 10 zeros.
        10 columns of these rows '''
        rows = []
        for i in range(10):
            str_row = map(self.map_fen_helper, self.rows_as_list[i])
            row = "".join(str_row)
            rows.append(row)
        for j in range(10):
            fen = "/".join(rows)
        self.boardstate_fen = fen
        # for i in range(len(self.rows_as_list)):
        #     boardstate_row = "".join([str(self.rows_as_list[i][j]) for j in
        # range(len(self.rows_as_list))])
        # boardstate_fen = "/".join([boardstate_row for i in
        # range(len(self.rows_as_list))])
        # self.boardstate_fen = boardstate_fen

    def get_boardstate_fen(self):
        return self.boardstate_fen

    def print_board(self):
        self.make_boardstate_fen()
        # print first row
        sys.stdout.write("  ")
        for i in range(ord('A'), ord('K')):
            sys.stdout.write(Color.UNDERLINE + chr(i) + Color.END)
        print ""

        # print rows
        for j in range(10):
            sys.stdout.write(str(j))
            sys.stdout.write("|")
            for k in range(11):
                if k != 10:
                    sys.stdout.write(self.boardstate_fen[k + (11 * j)])
            print ""


class Ship:
    ''' orientation is 1, 2, 3, or 4 for north, east, south, west,
    respectively '''
    def __init__(self, length, sid):
        self.length = length
        self.sid = sid

    def initialize_ship(self, start_row, start_column, orientation):
        self.start_row = start_row
        self.start_column = start_column
        self.orientation = orientation
        self.name = self.initialize_ship_name()

    def initialize_ship_name(self):
        names = {
            2: 'destroyer',
            3: 'cruiser',
            4: 'battleship',
            5: 'carrier'
        }
        return names[self.length]

    def add_to_board(self, board):
        ''' ships get added to board as 1's '''
        try:
            if self.orientation == 1:
                # check if spot is empty
                for i in range(self.length):
                    if board.rows_as_list[self.start_row - i][self.start_column] != 0:
                        raise CustomError(
                            'There\'s already a ship there! Try a different spot.'
                        )
                for i in range(self.length):
                    board.rows_as_list[self.start_row - i][self.start_column] = [1, self.sid]
            if self.orientation == 2:
                for i in range(self.length):
                    if board.rows_as_list[self.start_row][self.start_column + i] != 0:
                        raise CustomError(
                            'There\'s already a ship there! Try a different spot.'
                        )
                for i in range(self.length):
                    board.rows_as_list[self.start_row][self.start_column + i] = [1, self.sid]
            if self.orientation == 3:
                for i in range(self.length):
                    if board.rows_as_list[self.start_row + i][self.start_column] != 0:
                        raise CustomError(
                            'There\'s already a ship there! Try a different spot.'
                        )
                for i in range(self.length):
                    board.rows_as_list[self.start_row + i][self.start_column] = [1, self.sid]
            if self.orientation == 4:
                for i in range(self.length):
                    if board.rows_as_list[self.start_row][self.start_column - i] != 0:
                        raise CustomError(
                            'There\'s already a ship there! Try a different spot.'
                        )
                for i in range(self.length):
                    board.rows_as_list[self.start_row][self.start_column - i] = [1, self.sid]
            return True
        except CustomError, arg:
            # Catch the custom exception
            print 'Error: ', arg.msg
            return False
        except:
            return False


class Player:
    def __init__(self, name):
        self.board = Board()
        self.name = name


class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
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

    def get_input(self, question_string, ship_name):
        n = None
        while n is None:
            a = raw_input(question_string % ship_name)
            try:
                n = int(a)
                return n
            except ValueError:
                print "Not a number."

    def setup_ships(self, seed=None):
        if seed != None:
            setup_ships_from_seed()
        else:
            ask_flag = False
            '''ships should be the array from Board.ships'''
            for player in self.players:
                # set up human ships
                if player.player_type == 'Human':
                    for ship_name, ship_object in player.board.ships.iteritems():
                        print player.name + " is setting up ships!"
                        while (ask_flag is False):
                            start_row = self.get_input(
                                question_string="What row do you want to put your %s in? ",
                                ship_name=ship_name
                            )
                            start_column = self.get_input(
                                question_string="What column do you want to put your %s in? ",
                                ship_name=ship_name
                            )
                            orientation = self.get_input(
                                question_string="What direction do you want your %s to point? ",
                                ship_name=ship_name
                            )
                            ship_object.initialize_ship(start_row=start_row, start_column=start_column, orientation=orientation)
                            # ship_object.add_to_board(board) returns true on successful add, else false and loop repeats
                            ask_flag = ship_object.add_to_board(player.board)
                            if (ask_flag is False):
                                print("Error addding " + ship_name + " to board. Check your coordinates and try again!")
                        player.board.print_board()
                        ask_flag = False
                else:
                    # computer players
                    pass

    def shoot(self):
        player = self.players[turn]
        print "ready to shoot %s?" % player.name

# making players also makes boards
# making board also makes ships
player1_name = raw_input("Enter name for player 1: ")
player1 = HumanPlayer(player1_name)
player2_name = raw_input("Enter name for player 2: ")
player2 = HumanPlayer(player2_name)

# game needs an array of players
game = Game([player1, player2])

# setup and print board for player1
player1.board.make_boardstate_fen()
player1.board.print_board()

game.setup_ships()
game.shoot()
