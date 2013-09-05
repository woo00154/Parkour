import pygame
from entity import Entity

class Shape(Entity):
    
    def __init__(self,x,y,w,h):
        Entity.__init__(self,x,y,w,h)