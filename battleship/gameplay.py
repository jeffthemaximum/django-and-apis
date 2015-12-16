class Board(object):
    def __init__(self, player):
        self.player = player
        self.boardstate_fen = ""

    def initiate_boardstate_fen(self):
        ''' initiates board to string. row is 10 zeros. 10 columns of these rows '''
        boardstate_row = "".join(["0" for i in range(10)])
        boardstate_fen = "/".join([boardstate_row for i in range(10)])
        self.boardstate_fen = boardstate_fen


class Ship(object):
    def __init__(self, length):


class Player(object):
    pass


board = Board("human")
board.initiate_boardstate_fen()
print board.boardstate_fen
