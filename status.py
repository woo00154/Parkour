from image import Image
import pygame
from img_n_sound import *

class Status(Image):
    
    def __init__(self,image,color,y):
        Image.__init__(self,40,y,'status_bar.png',folder = 'status')
        self.value = pygame.Surface((2,21))
        self.value.fill(color)
        self.value = self.value.convert()
        
        self.symbol = load_image(image + '.png',folder = 'status')[0]
        #self.status_bar_rect = self.box.get_rect()
      
        self.current = 100
        self.maximum = 100

    def low(self):
        return self.current <= self.max * 0.2
    
    def update(self):
        if self.current > self.maximum:
            self.current = self.maximum
        elif self.current < 0 :
            self.current = 0

    def render(self,screen):
        x,y = self.rect.x, self.rect.y
        screen.blit(self.symbol,(x-35,y))
        screen.blit(self.image,(x,y))
        for v in range(self.current):
            screen.blit(self.value,(v*2 + x, y+2))
        
class Stamina(Status):
    
    def __init__(self):
        Status.__init__(self,'stamina',(100,149,247),45)
        self.state = True
        self.recharge_speed = 1
        
    def update(self):
        Status.update(self)
        self.exhaust()
        if not self.state:
            self.current += 1
        if self.current == self.maximum:
            self.state = True
            
        
    def cost(self,value):
        if self.current - value < 0 or not self.state:
            return False
        else:
            self.current -= value
            return True
        
    def exhaust(self):
        if self.current == 0:
            self.state = False
    
    def recover(self,value):
        if self.state:
            self.current += value
        
    
class Health(Status):
    
    def __init__(self):
        Status.__init__(self,'health',(124,252,0),10)
        
    def set(self,value):
        self.current = value
