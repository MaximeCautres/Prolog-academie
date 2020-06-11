# Server

from copy import deepcopy

from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.queen import Queen
from classes.rook import Rook


class Game:
    def __init__(self, board, server):
        self.board = board
        self.inGame = True
        self.check = False
        self.selected = False
        self.server = server
        self.move = []
        self.eat = []
        self.player = True

    def launchGame(self):
        self.server.sendYourTurn(self.player)
        while self.inGame:
            self.round()

    def select(self, yPos, xPos):
        if (
            self.board.map[yPos][xPos] != None
            and self.board.map[yPos][xPos].color == self.player
        ):
            movement, eat, castling, enPassant = self.board.map[yPos][xPos].getMove(
                self.board, self.check
            )
            self.selected = [yPos, xPos]
            
            self.server.sendApplySelection(self.player, self.selected, movement, eat, castling, enPassant) # share the change to the corresponding client

            self.possibleAction = movement + eat + castling + enPassant
            

    def round(self):
        played = False
        self.player = self.board.roundNumber % 2 == 0

        while not played:
            event = self.server.askEvent(self.player)

            if event:
                j, i = event
                # If the player hasn't already chosen a piece
                if not self.selected:
                    self.select(j, i)
                else:  # If a piece is already selected, the player chose the new piece's place
                    if [j, i] in self.possibleAction:  # The player hase chosen the move
                        self.move = []
                        self.eat = []
                        backUpMap, backUpPiece, backUpKing = (
                            deepcopy(self.board.map),
                            deepcopy(self.board.pieces),
                            deepcopy(self.board.king),
                        )
                        if self.check:
                            print("Check")
                            self.server.sendCheck(self.player)
                        if (
                            self.board.map[self.selected[0]][self.selected[1]].piecetype
                            == "king"
                            and abs(self.selected[1] - i) == 2
                        ):  # if the self.player decide to castle
                            side = i - self.selected[1]

                            self.board.map[j][4 + int(side / 2)] = deepcopy(
                                self.board.map[j][7 if side > 0 else 0]
                            )
                            self.board.map[j][4 + side] = deepcopy(self.board.map[j][4])

                            self.board.map[j][4] = None
                            self.board.map[j][7 if side > 0 else 0] = None

                            self.board.pieces[self.player].remove(self.selected)
                            self.board.pieces[self.player].remove(
                                [j, 7 if side > 0 else 0]
                            )

                            self.board.pieces[self.player] += [
                                [j, 4 + int(side / 2)],
                                [j, 4 + side],
                            ]

                            self.board.map[j][4 + int(side / 2)].xPos = 4 + int(
                                side / 2
                            )
                            self.board.map[j][4 + side].xPos = 4 + side

                            self.board.map[j][i].moved = True
                            self.board.map[j][i - int(side / 2)].moved = True

                            self.board.king[self.player] = [j, i]

                            self.move = [[self.player, j, i, *self.selected], [self.player, j, 4 + int(side/2), j, 7 if side > 0 else 0]]
                            self.eat = []

                            self.server.sendPieceMovement(self.move)

                            self.server.sendUpdateDisplay(
                                [self.selected]
                                + self.possibleAction
                                + [[j, i - int(side / 2)], [j, 7 if side > 0 else 0]]
                            )

                            for y, x in self.board.pieces[self.player]:
                                _, eat, _, _ = self.board.map[y][x].getMove(
                                    self.board, True
                                )
                                if self.board.king[not self.player] in eat:
                                    self.check = True
                                    break

                            self.board.roundNumber += 1
                            self.selected = False
                            self.player = not self.player
                            played = True
                            print(
                                f"It's the {'white' if self.player else 'black'} round"
                            )
                            self.server.sendYourTurn(self.player)

                            
                        else:  # normal movement or eat
                            self.board.map[j][i] = deepcopy(
                                self.board.map[self.selected[0]][self.selected[1]]
                            )

                            self.board.map[self.selected[0]][self.selected[1]] = None
                            self.board.pieces[self.player].remove(self.selected)

                            self.board.pieces[self.player] += [[j, i]]

                            self.board.map[j][i].yPos = j
                            self.board.map[j][i].xPos = i

                            # If we eat an adversary piece
                            if [j, i] in self.board.pieces[not self.player]:
                                self.board.pieces[not self.player].remove([j, i])

                                self.eat += [[not self.player, j, i]]

                            # Eat enPassant
                            elif (
                                self.board.map[j][i].piecetype == "pawn"
                                and i != self.selected[1]
                                and [j - (1 if self.player else -1), i]
                                in self.board.pieces[not self.player]
                            ):
                                self.board.pieces[not self.player].remove(
                                    [j - (1 if self.player else -1), i]
                                )
                                self.board.map[j - (1 if self.player else -1)][i] = None
                                self.possibleAction += [
                                    [j - (1 if self.player else -1), i]
                                ]
                                # We move the pawn one behind to have a normale heat after
                                self.move += [[not self.player, j, i, j-(1 if self.player else -1), i]]
                                self.eat += [[not self.player, j, i]]

                            # We save the move
                            self.move += [[self.player, j, i, *self.selected]]

                            if (
                                self.board.map[j][i].piecetype == "pawn"
                                and abs(j - self.selected[0]) == 2
                            ):
                                self.board.map[j][i].bigMove = self.board.roundNumber

                                # If we move the king the castling must be forbiden
                            if self.board.king[self.player] == self.selected:
                                self.board.king[self.player] = [j, i]
                                self.board.map[j][i].moved = True

                            if self.board.map[j][i].piecetype == "rook":
                                self.board.map[j][i].moved = True

                            self.check = False
                            for y, x in self.board.pieces[not self.player]:
                                _, eat, _, _ = self.board.map[y][x].getMove(
                                    self.board, True
                                )
                                if self.board.king[self.player] in eat:
                                    self.check = True
                                    break

                            if self.check:
                                self.board.map, self.board.pieces, self.board.king = (
                                    deepcopy(backUpMap),
                                    deepcopy(backUpPiece),
                                    deepcopy(backUpKing),
                                )
                            else:
                                if (
                                    j == (7 if self.player else 0)
                                    and self.board.map[j][i].piecetype == "pawn"
                                ):
                                    
                                    # Here we check the promotion case
                                    
                                    n = self.server.sendPawnArrival(self.player, j, i)
                                    # we have now the selected piece

                                    if n == 1:
                                        self.board.map[j][i] = Queen(self.player, i, j)
                                    elif n == 2:
                                        self.board.map[j][i] = Bishop(self.player, i, j)
                                    elif n == 3:
                                        self.board.map[j][i] = Knight(self.player, i, j)
                                    else:
                                        self.board.map[j][i] = Rook(self.player, i, j)
                                        self.board.map[j][i].moved = True

                                    # Time to send the chosen piece to both player
                                    self.server.sendPieceMovement(self.move)
                                    self.server.sendPieceSuppression(self.eat)
                                    
                                    self.server.sendChange(self.player, j, i, "queen" if n == 1 else ("bishop" if n == 2 else ("knight" if n == 3 else 'rook')))

                                # here we send the new positions

                                else:
                                    self.server.sendPieceMovement(self.move)
                                    self.server.sendPieceSuppression(self.eat)
                                # Change round - new board
                                self.server.sendUpdateDisplay(
                                    [self.selected] + self.possibleAction
                                )

                                for y, x in self.board.pieces[self.player]:
                                    _, eat, _, _ = self.board.map[y][x].getMove(
                                        self.board, True
                                    )
                                    if self.board.king[not self.player] in eat:
                                        self.check = True
                                        break

                                self.board.roundNumber += 1
                                self.selected = False
                                self.player = not self.player
                                played = True
                                print(
                                    f"It's the round of {'white' if self.player else 'black'} to play"
                                )
                                self.server.sendYourTurn(self.player)

                    else:  # The player decides to cancel his selection
                        self.server.sendUpdateDisplay(self.possibleAction + [self.selected])
                        self.selected = False

            else:
                played = True
                self.inGame = False
                self.server.sendEndGame()
