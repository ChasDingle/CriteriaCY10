import pygame as p


a1 = input("A1 ")
a2 = input("A2 ")
a3 = input("A3 ")
a4 = input("A4 ")
a5 = input("A5 ")
a6 = input("A6 ")
a7 = input("A7 ")
a8 = input("A8 ")

b1 = input("B1 ")
b2 = input("B2 ")
b3 = input("B3 ")
b4 = input("B4 ")
b5 = input("B5 ")
b6 = input("B6 ")
b7 = input("B7 ")
b8 = input("B8 ")

c1 = input("C1 ")
c2 = input("C2 ")
c3 = input("C3 ")
c4 = input("C4 ")
c5 = input("C5 ")
c6 = input("C6 ")
c7 = input("C7 ")
c8 = input("C8 ")

d1 = input("D1 ")
d2 = input("D2 ")
d3 = input("D3 ")
d4 = input("D4 ")
d5 = input("D5 ")
d6 = input("D6 ")
d7 = input("D7 ")
d8 = input("D8 ")


e1 = input("E1 ")
e2 = input("E2 ")
e3 = input("E3 ")
e4 = input("E4 ")
e5 = input("E5 ")
e6 = input("E6 ")
e7 = input("E7 ")
e8 = input("E8 ")

f1 = input("F1 ")
f2 = input("F2 ")
f3 = input("F3 ")
f4 = input("F4 ")
f5 = input("F5 ")
f6 = input("F6 ")
f7 = input("F7 ")
f8 = input("F8 ")

g1 = input("G1 ")
g2 = input("G2 ")
g3 = input("G3 ")
g4 = input("G4 ")
g5 = input("G5 ")
g6 = input("G6 ")
g7 = input("G7 ")
g8 = input("G8 ")

h1 = input("H1 ")
h2 = input("H2 ")
h3 = input("H3 ")
h4 = input("H4 ")
h5 = input("H5 ")
h6 = input("H6 ")
h7 = input("H7 ")
h8 = input("H8 ")
class GameState():
    def __init__(self):
        """
        Board is an 8x8 2d list, each element in list has 2 characters.
        The first character represents the color of the piece: 'b' or 'w'.
        The second character represents the type of the piece: 'R', 'N', 'B', 'Q', 'K' or 'p'.
        "--" represents an empty space with no piece.
        """
        self.board = [
            [a8, b8, c8, d8, e8, f8, g8, h8],
            [a7, b7, c7, d7, e7, f7, g7, h7],
            [a6, b6, c6, d6, e6, f6, g6, h6],
            [a5, b5, c5, d5, e5, f5, g5, h5],
            [a4, b4, c4, d4, e4, f4, g4, h4],
            [a3, b3, c3, d3, e3, f3, g3, h3],
            [a2, b2, c2, d2, e2, f2, g2, h2],
            [a1, b1, c1, d1, e1, f1, g1, h1]]
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}



def loadImages():
#Initialize a global directory of images.This will be called exactly once in the main.

    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
 #The main driver for our code. This will handle user input and updating the graphics.

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameState()
    loadImages()
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT: 
                running = False
           # elif e.type == p.K_KP_ENTER:
           #   y=true
                #FEN to Board
        
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
            
            


    

def drawGameState(screen,gs):
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares

def drawBoard(screen):
    colors = [p.Color("white smoke"), p.Color("olivedrab")]
    for r in range(DIMENSION):
            for c in range(DIMENSION):
                color = colors [((r+c) %2)]
                p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__ == "__main__":
    main()