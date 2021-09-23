"""
-this class is responsible for storing all the informations about the current game state.
-it will also be responsible for determining the valid moves to the current state.
-it will also keep a move log.
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]] 

        self.moveFunctions = {'p': self.getPawnMoves, 'R':self.getRookMoves, 'N':self.getNightMoves,
                              'B': self.getBishopMoves, 'Q':self.getQueenMoves, 'K':self.getKingMoves} 
        
        self.whiteToMove = True
        self.moveLog = []
        #self.movesUndoed = []
        self.whiteKingLocation = (0,4)
        self.blackKingLocation = (7,4)
         

        
    
    '''
    takes a move as a parameter and executes it, dosen't work for castlig, en passant, and pawn promotion
    '''

    def makeMove(self, move):
        #if self.whiteToMove and self.board[move.startRow][move.startCol][0]=='w':
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)           # Log The Move.        
        self.whiteToMove = not self.whiteToMove  
        # Update the kings location if moved.
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow,move.endCol)
        elif move.pieceMoved == 'bk':
            self.blackKingLocation = (move.endRow,move.endCol)


        """  elif not self.whiteToMove and self.board[move.startRow][move.startCol][0]=='b':
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move)           # Log The Move.
            print("Black Has Made His Movem, White turn Now")              
            self.whiteToMove = not self.whiteToMove     # Swap players.
        """
        


    '''
    undo last move
    '''
    def undoMove(self):
        if len(self.moveLog) != 0: #Make sure there is a move to undo. 
            #print("the number of Moves In The MoveLog Before the Last Undo is:")  
            #print(len(self.moveLog))         
            move = self.moveLog.pop()
            # print("the number of Moves Of the MoveLog after The Last Undo is:")
            #print(len(self.moveLog))
            #self.movesUndoed.append(move)
            #print("the number of Moves Undoed So Far is:")
            #print(len(self.movesUndoed))
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove     # Swap players.

    '''
    redo last move
    '''
    """ def redoMove(self):        
        if len(self.movesUndoed) != 0: #Make sure there is a move to redo.    
            print("the number of Moves In The MovesUndoed Before the Last Redo is:")         
            print(len(self.movesUndoed))
            move = self.movesUndoed.pop()
            print("the number of Moves in movesUndoed  after redo is:")
            print(len(self.movesUndoed))
            self.moveLog.append(move)
            print("the number of Moves Done Redoed so far:")
            print(len(self.moveLog))
            self.board[move.startRow][move.startCol] = move.pieceCaptured
            self.board[move.endRow][move.endCol] = move.pieceMoved
            #self.whiteToMove = not self.whiteToMove     # Swap players. """


    '''
    All Moves Considering Checks.
    '''
    def getValideMoves(self):
        #1) Generte All The possible moves For the current Player.
        moves = self.getAllPossibleMoves() 
        if self.whiteToMove:
            print("The Number Of Valid Moves For White:")
            print(len(moves))
            print("The Last white possible Move Description:")
            print(moves[len(moves)-1].pieceMoved)       
            print(moves[len(moves)-1].getChessNotation())
        else:
            print("The Number Of Valid Moves For Black:")
            print(len(moves))
            print("The Last Black possible Move Description:")
            print(moves[len(moves)-1].pieceMoved)
            print(moves[len(moves)-1].getChessNotation())
        return moves
              
        """ #2) for each move, make the move.
        for i in range(len(moves)-1,-1,-1): #When removing from a list go backwrds through that list.
            self.makeMove(moves[i])
        #3) Generate All opponents moves.
        #4) For each of your opponents moves see if they attack your king.
            self.whiteToMove = not self.whiteToMove # Switch Turns             
            if self.inCheck():
                if self.whiteToMove:
                    print("White Is In check")
                else:
                    print("Black Is In check")
                moves.remove(moves[i])#5) if they do attck your king, Not a valid move.
                print("this Move Didnt Consider Check")
            self.whiteToMove = not self.whiteToMove # Switch Turns 
            self.undoMove()         
        if self.whiteToMov
            print("The Number Of Valid Moves For White:")
            print(len(moves))
            print("The Last white possible Move Description:")
            print(moves[len(moves)-1].pieceMoved)       
            print(moves[len(moves)-1].getChessNotation())
        else:
            print("The Number Of Valid Moves For Black:")
            print(len(moves))
            print("The Last Black possible Move Description:")
            print(moves[len(moves)-1].pieceMoved)
            print(moves[len(moves)-1].endRow)
            print(moves[len(moves)-1].endCol)
        return moves """




    """
    #################Decoupling###############
    """

    '''
    Determine if the current player is in check.
    '''
    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0],self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0],self.blackKingLocation[1])



    '''
    Check if the square (r,c) is under attack.
    '''
    def squareUnderAttack(self,r ,c):
        self.whiteToMove = not self.whiteToMove # Switch Turns 
        oppMoves = self.getAllPossibleMoves()        
        self.whiteToMove = not self.whiteToMove # Switch Back Turns
        for move in oppMoves:                        
            if move.endRow == r and move.endCol == c:
                if self.whiteToMove:                    
                    print("White's King is Under Attack")  
                else:
                    print("Black's King is Under Attack")      
                return True
        return False




    '''
    All Moves Without Considering Checks.
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): # number of rows
            for c in range(len(self.board[r])): # number of cols
                turn = self.board[r][c][0] 
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves) #
        return moves




    '''
    get all the possible moves for the pawn located in (r,C) and add them to the moves list.
    '''
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove: # White Pawn Moves
            if self.board[r-1][c] =='--': # 1 square Pawn Advance
                moves.append(Move((r, c), (r-1, c), self.board ))                
                if r==6 and self.board[r-2][c] == '--': # 2 square Pawn Advance 
                    moves.append(Move((r, c), (r-2, c), self.board ))
            if c-1>=0 : # captures to the left
                if self.board[r-1][c-1][0] == 'b': # enemy piece to capture
                    moves.append(Move((r, c), (r-1, c-1), self.board ))
            if c+1<=7 : # captures to the right
                if self.board[r-1][c+1][0] == 'b': # enemy piece to capture
                    moves.append(Move((r, c), (r-1, c+1), self.board ))
        else:  # Black Pawn Moves
            if self.board[r+1][c] =='--': # 1 square Pawn Advance
                moves.append(Move((r, c), (r+1, c), self.board ))                
                if r==1 and self.board[r+2][c] == '--': # 2 squares Pawn Advance 
                    moves.append(Move((r, c), (r+2, c), self.board ))
            if c-1>=0 : # captures to the left
                if self.board[r+1][c-1][0] == 'w': # enemy piece to capture
                    moves.append(Move((r, c), (r+1, c-1), self.board ))
            if c+1<=7 : # captures to the right
                if self.board[r+1][c+1][0] == 'w': # enemy piece to capture
                    moves.append(Move((r, c), (r+1, c+1), self.board ))




    '''
    get all the possible moves for the Rook located in (r,C) and add them to the moves list.
    '''
    def getRookMoves(self, r, c, moves):   
        directions = ((-1,0), (0,-1), (1,0), (0,1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r,c), (endRow,endCol), self.board )) 
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c), (endRow,endCol), self.board ))
                        break
                    else:
                        break
                else:  #off board
                    break



    '''
    get all the possible moves for the Night located in (r,C) and add them to the moves list.
    '''
    def getNightMoves(self, r, c, moves):                            
        knightMoves = ((-2,-1), (-2,1), (-1,-2), (-1,2),(1,-2), (1,2), (2,-1), (2,1))
        print("Current Location of the Knight Is ({},{})".format(r,c) )
        if self.whiteToMove:
            enemyColor = "b" 
        else:
            enemyColor = "w"       
        for i in range(8):
            endR = r + knightMoves[i][0]
            endC = c + knightMoves[i][1]           
            if 0<=endR<8 and 0<=endC<8:
                endPiece = self.board[endR][endC]   
                print("Current Location of the End Piece Is ({},{})".format(endR,endC) )          
                if endPiece[0] == enemyColor or endPiece[0] == '-':  
                    move = Move((r,c), (endR,endC), self.board )
                    print("move {}".format(i))   
                    print(move.getChessNotation())   
                    moves.append(move) 
            
                    
                                  
                     
                    


             
            

    '''
    get all the possible moves for the Bishop located in (r,C) and add them to the moves list.
    '''
    def getBishopMoves(self, r, c, moves):          
        directions = ((-1,-1), (-1,1), (1,-1), (1,1))
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1,8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--":
                        moves.append(Move((r,c), (endRow,endCol), self.board )) 
                    elif endPiece[0] == enemyColor:
                        moves.append(Move((r,c), (endRow,endCol), self.board ))
                        break
                    else:
                        break
                else:  #off board
                    break




    '''
    get all the possible moves for the Queen located in (r,C) and add them to the moves list.
    '''
    def getQueenMoves(self, r, c, moves):
        self.getBishopMoves(r, c, moves)
        self.getRookMoves(r, c, moves)

  


    '''
    get all the possible moves for the King located in (r,C) and add them to the moves list.
    '''
    def getKingMoves(self, r, c, moves):
        kingMoves= ((-1,-1), (-1,0), (-1,1), (0,-1),(0,1), (1,-1), (1,0), (1,1))
        print("Current Location of the King Is ({},{})".format(r,c) )
        if self.whiteToMove:
            allyColor = "w"
            print("Possible King Moves For White")
        else:
            allyColor = "b"       
        for  i in range(8) :
            endR = r + kingMoves[i][0]
            endC = c + kingMoves[i][1]
            if 0<=endR<8 and 0<=endC<8:
                endPiece = self.board[endR][endC]
                move = Move((r,c), (endR,endC), self.board ) 
                print("move {}".format(i))   
                print(move.getChessNotation())                          
                if  endPiece[0] != allyColor :                   
                    moves.append(move) 
                          
                    
                
 

          


class Move():
    # maps keys to values
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,"5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,"e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}



    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        


    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID    
        return False



    

    def getChessNotation(self):
        #you can add to make this a real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

































