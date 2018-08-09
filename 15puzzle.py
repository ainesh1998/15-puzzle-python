import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("15 puzzle simulator")
pygame.font.get_fonts()
font = pygame.font.SysFont("Times New Roman",72)

def drawSquare(number,x,y):
    if number%2 == 0:
        pygame.draw.rect(screen,(0,200,0),(x,y,125,125))

    else:
        pygame.draw.rect(screen,(64,224,208),(x,y,125,125))
    screen.blit(font.render(str(number),5,(0,0,0)),(x+62,y+62))
    pygame.display.update()
    
def layout():
    screen.fill((255,255,255))
    number = 1
    x = 0
    y = 0
    while number < 16:
        if x == 500:
            x = 0
            y += 125
        drawSquare(number,x,y)

        x += 125
        number += 1

def swap(x,y,dir_x,dir_y):
    new_x = x + dir_x
    new_y = y + dir_y
    
    swapped_tile = screen.get_rect().clip(Rect(new_x,new_y,125,125))
    swapped_tile.move(dir_x,dir_y)
    screen.blit(swapped_tile,(375,375))
    pygame.display.update()
    
def main():
    blank_x = 375
    blank_y = 375
    layout()
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    swap(blank_x,blank_y,-125,0)
                    blank_x -= 125
                if event.key == K_RIGHT:
                    blank_x += 125
                if event.key == K_UP:
                    blank_y -= 125
                if event.key == K_DOWN:
                    blank_y += 125

main()
