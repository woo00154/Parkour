import pygame
from image import Image
from img_n_sound import *

class Platform(Image):
    
    def __init__(self,x,y,tx,ty,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_tileset(size,size,tx,ty)
        self.rect = Rect(x,y,size,size)
        self.type = tx,ty