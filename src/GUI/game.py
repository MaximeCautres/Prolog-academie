from copy import deepcopy

class Game:
    def __init__(self, board):
        self.board = board
        self.inGame = True
        self.check = False

    def getEvent(self):
        for event in pygame.event.get(): # We ask the user to do something 
            if event.type == QUIT: # We close the pygame window
                pygame.quit()
                return False
            if event.type == MOUSEBOUTTONDOWN and event.button == 1: # We return the coordonate of the click
                return j, i = 7 - y // unit, x // unit

    def launchGame(self):
        while self.inGame:
            self.round()

    def select(self, yPos, xPos):
        if self.board.map[yPos][xPos] != None and self.board.map[yPos][xPos].color == player:
            movement, eat, castling, enPassant = self.board.map[yPos][xPos].get_move(self.board)
            self.board.apply_selection([yPos, xPos], movement, eat, castling, enPassant)
            self.board.selected = [j, i]
            self.board.possible_action = movement + eat + castling + enPassant

    def round(self):
        played = False
        player = (self.board.round_number % 2 == 0)

        while not played:
            event = self.getEvent()
            if event:
                j, i = event

                if not self.board.selected: # If the player hasn't already chosen a piece
                    self.select(j, i)
                else: # If a piece is already selected, the player chose the new piece's place
                    if [j, i] in role: # The player hase chosen the move

                        back_up = deepcopy(self.board)
                        if self.echec:
                            print("your are check")

                        if [j, i] in self.board.piece[player]: # if the player decide to castle
                            # it is needed to correctly implement the castling here
                        else: # normal movement or eat
                            self.board.map[j][i] = deepcopy(self.board.map[self.selected[0]][self.selected[1]])

                            self.board.map[selected[0]][selected[1]] = 0
                            self.board.piece[joueur].remove(selectionee)
                            self.board.piece[joueur]+= [[j, i]]
                            self.board.map[j][i].yPos = j
                            self.board.map[j][i].xPos = i

                            # Si on mange une piece de l'autre
                            if [j, i] in partie.piece[adversaire]:
                                partie.piece[adversaire].remove([j,i])

                            # Si l'on mange en passant
                            if partie.map[j][i].piecetype == 'pion' and i != selectionee[1] and [j - (1 if joueur == 'blanc' else -1), i] in partie.piece[adversaire]:
                                partie.piece[adversaire].remove([j - (1 if joueur == 'blanc' else -1), i])
                                partie.map[j-(1 if joueur == 'blanc' else -1)][i] = 0
                                role += [[j-(1 if joueur == 'blanc' else -1), i]]


                            if partie.map[j][i].piecetype == 'pion' and abs(j - selectionee[0]) == 2:
                                partie.map[j][i].bouge_2 = partie.numero_tour

                            # Si on bouge le roi, on doit interdire le roque
                            if partie.roi[joueur] == selectionee:
                                partie.roi[joueur] = [j, i]
                                partie.map[j][i].abouge = True

                            if partie.map[j][i] == 'tour':
                                partie.map[j][i].abouge = True

                            echec = False
                            for piece in partie.piece[adversaire]:
                                _, mangeable, _, _ = partie.map[piece[0]][piece[1]].deplacement(piece[0], piece[1], partie)
                                if partie.roi[joueur] in mangeable:
                                    echec = True
                                    break

                            if echec:
                                partie = deepcopy(backup)
                            else:

                                if j == (7 if joueur == 'blanc' else 0) and partie.map[j][i].piecetype == 'pion':
                                    n = 0
                                    while not 0 < n < 5:
                                        n = input('Promotion !! Rentre 1 pour renne, 2 pour fou, 3 pour cavalier, 4 pour tour :')
                                        try :
                                            n = int(n)
                                        except:
                                            print("il faut mettre un entier entre 1 et 4")
                                            n = 0
                                        if n == 1:
                                            partie.map[j][i] = Renne(joueur)
                                        elif n == 2:
                                            partie.map[j][i] = Fou(joueur)
                                        elif n == 3:
                                            partie.map[j][i] = Cavalier(joueur)
                                        else:
                                            partie.map[j][i] = Tour(joueur)
                                            partie.map[j][i].abouge = True

                                # On change de tour, on refait l'echequier propre
                                for j, i in [selectionee]+role:
                                    affiche_piece(j, i)

                                # Comme on change de tour on deselectionne
                                selectionee = False

                                for piece in partie.piece[joueur]:
                                    _, mangeable, _, _ = partie.map[piece[0]][piece[1]].deplacement(piece[0], piece[1], partie)
                                    if partie.roi[adversaire] in mangeable:
                                        echec = True
                                        break

                                partie.numero_tour += 1

                                joueur = not joueur

                                played = True

                                print(f'Au tour de {joueur} de joueur')

                    else: # The player decides to cancel his selection
                       self.board.update_display(self.board.possible_action)

            else:
                played = True
                self.inGame = False
