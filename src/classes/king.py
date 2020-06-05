from classes.piece import Piece

class King(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.moved = False
        self.piecetype = 'king'

    # Return the king position with or without eating
    def getMove(self, game, check):
        yPos, xPos = self.yPos, self.xPos
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        for y, x in cases:
            if 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x] == None:
                movement += [[yPos + y, xPos + x]]
            elif 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x].color != self.color:
                eat += [[yPos + y, xPos + x]]
        
        def is_check(j, i):

            check_confirmation = False
                  
            for y, x in game.pieces[not self.color]:
                movement, _, _, _ = mapGame[y][x].getMove(game, True)
                if [j, i] in movement:
                    return True
            return False

        # small castling (right one)
        
        if not check and not self.moved and mapGame[yPos][7] != None and mapGame[yPos][7].piecetype == 'rook' and not mapGame[yPos][7].moved and mapGame[yPos][7].color == self.color and mapGame[yPos][5] == None and mapGame[yPos][6] == None and not is_check(yPos, 5) and not is_check(yPos, 6):
            castling += [[yPos, 6]]
            print(is_check(yPos, 5), is_check(yPos, 6))

        # big casling (left one)

        if not check and not self.moved and mapGame[yPos][0] != None and mapGame[yPos][0].piecetype == 'rook' and not mapGame[yPos][0].moved and mapGame[yPos][0].color == self.color and mapGame[yPos][1] == None and mapGame[yPos][2] == None and mapGame[yPos][3] == None and not is_check(yPos, 2) and not is_check(yPos, 3):
            castling += [[yPos, 2]]
        
        
        return movement, eat, castling, []
