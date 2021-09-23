"""
this is the main driver file. it will be responsible for handling user input and dispaying the current gameState Object.
"""

import pygame as p
import ChessEngine


WIDTH = HEIGHT = 512    # 400 is another option
DIMENSION = 8           # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15            #for animations later on
IMAGES = {}


'''
Initialize a global dictionnary of images. this will be exactelly once in the main
'''

def loadImages():
    pieces = ["wp","wR","wN","wB","wQ","wK","bp","bR","bB","bN","bR","bQ","bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieces/"+ piece + ".png"),(SQ_SIZE,SQ_SIZE))
    # We can access any image by typing 'IMAGES["wp"] 

'''
the main driver for our code. this will handle user input and updating the graphics.
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    valideMoves = gs.getValideMoves() 
    #print("valid Moves for white at the begining:")   
    #print(len(valideMoves))
    moveMade = False # Flag
    loadImages()
    running = True
    sqSelected = ()             # No square is selected, keep track of the last click of the user (tuple: (row,col))
    playerClicks = []           # Keep track of player clicks (two tuples: [(6,4),(4,4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse Handler:
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()  # (x,y) location of the mouse.
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()           # Deselct
                    playerClicks = []
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)  #Creating The Move Object As an instance of the Move Class
                    print(move.getChessNotation())
                    if move in valideMoves:
                        gs.makeMove(move)                    
                        moveMade = True                   
                    sqSelected = ()
                    playerClicks = []
            #Key Handlers:
            elif e.type == p.KEYDOWN:              
                if e.key == p.K_LEFT: #undo when left is pressed.                  
                    gs.undoMove()
                    moveMade=True
                    #print("The Number Of valid Moves For Current player:")
                    #print(len(valideMoves))

                """  if e.key == p.K_RIGHT: #redo when right is pressed.
                    gs.redoMove()                   
                    moveMade=True
                    print("The number Of Valid Moves For The current Player:")
                    print(len(valideMoves)) """

        if moveMade:
            valideMoves = gs.getValideMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Responsible for all the graphics in a current gameState.
'''

def drawGameState(screen, gs):
    drawBoard(screen)  # Draw squares on the board
    # add in piece highlighting or move suggestions(later)
    drawPieces(screen, gs.board)

'''
Draw the squares on the board.
'''
def drawBoard(screen):
    colors = [p.Color("dark grey"), p.Color("dark red")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using the current GameState.Board
'''

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":    # Not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

  

if __name__ == '__main__':
    main()


