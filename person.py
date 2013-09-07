from entity import Entity
import pygame
from gravity import Gravity
from img_n_sound import *
from vector import Vector

class Person(Entity):
    
    def __init__(self,x,y,image):
        self.image,self.rect = load_image(image)
        Entity.__init__(self,x,y,self.rect.w,self.rect.h)
        self.rect.left = x
        self.rect.top = y
        self.xvel = 0
        self.yvel = 0

        self.gravity = Gravity(5)
    
    def load_images(self):
        pass
    

    
    def tick(self,platforms):
        self.gravity.apply(self)
        # increment in x direction
        self.rect.left += self.xvel
        
        self.hanging = self.onWall_R = self.onWall_L = False
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)
    
    def collide(self, xvel, yvel, platforms):
        
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.onWall_R = True
                    self.xvel = 0
                    if p.type == (2,0) and -2 <= self.rect.top- p.rect.top<=2:
                        self.yvel = 0
                        self.hanging = True
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.onWall_L = True
                    self.xvel = 0
                    
                    if p.type == (2,0) and -2<=self.rect.top- p.rect.top<=2:
                        self.yvel = 0
                        self.hanging = True

                if yvel > 0:                    
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
    
