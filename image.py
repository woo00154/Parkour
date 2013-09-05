import pygame
from entity import Entity

class Image(Entity,pygame.sprite.Sprite):
    
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)