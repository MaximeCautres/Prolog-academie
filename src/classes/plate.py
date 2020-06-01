class Plate:
    def __init__(self):

        # Create the table which represents the plate
        self.map = [[0 for _ in range(8)] for _ in range(8)]

        # Initialization of the plate with all the pieces
        for x in range(8):
            self.map[1][x] = Pawn('white')
            self.map[6][x] = Pawn('black')
        self.map[0][0] = Rook('white')
        self.map[0][7] = Rook('white')
        self.map[7][0] = Rook('black')
        self.map[7][7] = Rook('black')
        self.map[0][1] = Knight('white')
        self.map[0][6] = Knight('white')
        self.map[7][1] = Knight('black')
        self.map[7][6] = Knight('black')
        self.map[0][2] = Bishop('white')
        self.map[0][5] = Bishop('white')
        self.map[7][2] = Bishop('black')
        self.map[7][5] = Bishop('black')
        self.map[0][3] = Queen('white')
        self.map[7][3] = Queen('black')
        self.map[0][4] = King('white')
        self.map[7][4] = King('black')

        # Initialization of the round_number
        self.round_number = 0

        # Positions of all the pieces at the beginning of the games. It changes with pieces' moves
        self.pieces = {'white': [[0, x] for x in range(8)] + [[1, x] for x in range(8)],
                      'black': [[6, x] for x in range(8)] + [[7, x] for x in range(8)]
        }

        # The kings will need to be track during the game for the check detection
        self.king = {'white': [0, 4], 'black': [7, 4]}
