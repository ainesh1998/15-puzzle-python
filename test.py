from pygame.locals import *
import pygame, sys
from random import randint

def randomnumber():
    return str(randint(1,11))

pygame.init()
x = 200
y = 200
pygame.font.get_fonts()
font = pygame.font.SysFont("Times New Roman", 30)
number = font.render(randomnumber(),5, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT and x != 50:
                x -= 10
            elif event.key == K_RIGHT and x != 350:
                x += 10
            elif event.key == K_UP and y != 50:
                y -= 10
            elif event.key == K_DOWN and y != 350:
                y += 10

    if x == 50 or x == 350 or y == 50 or y == 350:
        number = font.render(randomnumber(),5,(255,255,255))
        if x == 50:
            x = 60
        elif x == 350:
            x = 340
        elif y == 50:
            y = 60
        elif y == 350:
            y = 340

        
    screen = pygame.display.set_mode((400,400))
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,255),(x,y),50)
    screen.blit(number, (x-5,y-5))
    pygame.display.update()
