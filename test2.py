import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))


class bread(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print(self.x)
        print(self.y)
        print(self.z)

class bun(bread):
    def __init__(self,x,y,z,a):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

breads = []

for i in range(15):
    breads.append(bread(i,i+1,i+2))

breads[3].print()
breads[3].x = 10000
breads[3].print()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
