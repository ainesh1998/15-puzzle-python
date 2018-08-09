import pygame, sys
from pygame.locals import *
from random import randint
from random import choice

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption("15 Puzzle Simulator")
pygame.font.get_fonts()
font = pygame.font.SysFont("Times New Roman",72)

class empty_square(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def drawSquare(self):
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,125,125))
        pygame.display.update()

    def coordinates(self):
        coordinates = [self.x,self.y]
        return coordinates

class square(empty_square):
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number = number

    def drawSquare(self):
        colours = [1,3,6,8,9,11,14]
        if self.number in colours:
            pygame.draw.rect(screen,(64,224,208),(self.x,self.y,125,125))
        else:
            pygame.draw.rect(screen,(0,200,0),(self.x,self.y,125,125))
        screen.blit(font.render(str(self.number),10,(0,0,0)),(self.x+55,self.y+55))
        pygame.display.update()

def drawBoard(squares):
    number = 1

    for row in range(0,500,125):
        for column in range(0,500,125):
            squares.append(square(column,row,number))
            number += 1

            if number == 16:
                break
    
    for i in squares:
        i.drawSquare()
                
def swap(x,y,dir_x,dir_y,squares):
    new_coordinates = [x+dir_x,y+dir_y]

    for i in squares:
        if i.coordinates() == new_coordinates:
            i.x = x
            i.y = y
            i.drawSquare()
            break

def scramble(squares):
    for i in range(30):
        j = randint(1,15)
        swap(squares[j-1].x, squares[j-1].y, choice(0,125,-125), choice(0,125,-125), squares)
        
        
def main():
    squares = []
    drawBoard(squares)
    emptySquare = empty_square(375,375)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_LEFT and emptySquare.x != 0:
                    swap(emptySquare.x,emptySquare.y,-125,0,squares)
                    emptySquare.x -= 125
                    emptySquare.y += 0
                    emptySquare.drawSquare()
                    
                if event.key == K_RIGHT and emptySquare.x != 375:
                    swap(emptySquare.x,emptySquare.y,125,0,squares)
                    emptySquare.x += 125
                    emptySquare.y += 0
                    emptySquare.drawSquare()
                    
                if event.key == K_UP and emptySquare.y != 0:
                    swap(emptySquare.x,emptySquare.y,0,-125,squares)
                    emptySquare.x += 0
                    emptySquare.y -= 125
                    emptySquare.drawSquare()
                    
                if event.key == K_DOWN and emptySquare.y != 375:
                    swap(emptySquare.x,emptySquare.y,0,125,squares)
                    emptySquare.x += 0
                    emptySquare.y += 125
                    emptySquare.drawSquare()
                    
main()
