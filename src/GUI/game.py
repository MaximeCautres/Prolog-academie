from copy import deepcopy

class Game:
    def __init__(self, board):
        self.board = board
        self.inGame = True
        self.check = False
        self.selected = False

    def launchGame(self):
        while self.inGame:
            self.round()

    def select(self, yPos, xPos):
        if self.board.map[yPos][xPos] != None and self.board.map[yPos][xPos].color == self.player:
            movement, eat, castling, enPassant = self.board.map[yPos][xPos].get_move(self.board)
            self.selected = [yPos, xPos]
            self.board.applySelection(self.selected, movement, eat, castling, enPassant)
            self.board.possibleAction = movement + eat + castling + enPassant

    def round(self):
        played = False
        self.player = (self.board.round_number % 2 == 0)

        while not played:
            event = self.board.getEvent()
            if event:
                j, i = event

                # If the player hasn't already chosen a piece
                if not self.selected:
                    self.select(j, i)
                else: # If a piece is already selected, the player chose the new piece's place
                    if [j, i] in possibleAction: # The player hase chosen the move
                        backUp = deepcopy(self.board)
                        if self.echec:
                            print("your are check")
                        if [j, i] in self.board.piece[self.player]: # if the self.player decide to castle
                            pass
                            # it is needed to correctly implement the castling here
                        else: # normal movement or eat
                            self.board.map[j][i] = deepcopy(self.board.map[self.selected[0]][self.selected[1]])
                            self.board.map[selected[0]][selected[1]] = None
                            self.board.piece[joueur].remove(self.selected)
                            self.board.piece[joueur] += [[j, i]]
                            self.board.map[j][i].yPos = j
                            self.board.map[j][i].xPos = i

                            # If we eat an adversary piece
                            if [j, i] in self.board.piece[not self.player]:
                                self.board.piece[not self.player].remove([j,i])

                            # Eat enPassant
                            if self.board.map[j][i].piecetype == 'pawn' and i != selected[1]:
                            #and [j - (1 if player else -1), i] in self.board.piece[not player]:
                                self.board.piece[not self.player].remove([j - (1 if self.player else -1), i])
                                self.board.map[j - (1 if self.player else - 1)][i] = 0
                                possibleAction += [[j - (1 if self.player else - 1), i]]

                            if self.board.map[j][i].piecetype == 'pawn' and abs(j - selectionee[0]) == 2:
                                self.board.map[j][i].move2 = self.board.roundNumber

                            # If we move the king the castling must be forbiden
                            if self.board.king[self.player] == selected:
                                self.board.king[self.player] = [j, i]
                                self.board.map[j][i].moved = True

                            if self.board.map[j][i] == 'rook':
                                self.board.map[j][i].moved = True

                            self.check = False
                            for y, x in self.board.piece[not self.player]:
                                _, eat, _, _ = self.board.map[y][x].getMove(self.board)
                                if self.board.king[self.player] in eat:
                                    self.check = True
                                    break

                            if self.check:
                                self.board = deepcopy(backUp)
                            else:
                                if j == (7 if self.player else 0) and self.board.map[j][i].piecetype == 'pawn':
                                    n = 0
                                    while n == 0:
                                        n = input('Promotion !!  1- Queen, 2-Bishop, 3-Knight, 4-Rook: ')
                                        try :
                                            1 <= int(n) <= 4
                                        except:
                                            print("Entry not valid (must be between 1 and 4)")
                                            n = 0
                                        if n == 1:
                                            self.board.map[j][i] = Queen(self.player)
                                        elif n == 2:
                                            self.board.map[j][i] = Bishop(self.player)
                                        elif n == 3:
                                            self.board.map[j][i] = Knoght(self.player)
                                        else:
                                            self.board.map[j][i] = Rook(self.player)
                                            self.board.map[j][i].moved = True

                                # Change round - new board
                                updateDisplay([self.selected] + actions)

                                for y, x in self.board.piece[self.player]:
                                    _, eat, _, _ = self.board.map[y][x].getMove(self.board)
                                    if self.board.king[not self.player] in eat:
                                        self.check = True
                                        break

                                self.board.roundNumber += 1
                                self.selected = False
                                self.player = not self.player
                                played = True
                                print(f"It's the round of {player} to play")

                    else: # The player decides to cancel his selection
                       self.board.update_display(self.board.possibleAction)

            else:
                played = True
                self.inGame = False
