import pygame

pygame.init()

WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("N Queens Visualiser")

def draw_board(n):
    block_size=WIDTH//n
    colours=[(255,255,255),(0,0,0)]

    for row in range(n):
        for col in range(n):
            colour=colours[(row+col)%2]
            pygame.draw.rect(screen,colour,(col*block_size,row*block_size,block_size,block_size))

def draw_queens(board):
    n=len(board)
    block_size=WIDTH//n
    for col,row in enumerate(board):
        x=col*block_size+block_size//2
        y=row*block_size+block_size//2

        pygame.draw.circle(screen,(0,255,0),(x,y),block_size//3)

def visualiser(board):
    n=len(board)
    running=True

    while(running):
        screen.fill((0,0,0))
        draw_board(n)
        draw_queens(board)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    pygame.quit()

