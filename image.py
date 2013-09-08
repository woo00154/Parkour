import pygame
from entity import Entity
from img_n_sound import *

class Image(Entity):
    
    def __init__(self,x,y,image):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect = load_image(image)
        Entity.__init__(self,x,y,self.rect.w,self.rect.h)
        self.rect.left = x
        self.rect.top = y