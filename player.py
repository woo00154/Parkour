import pygame
from person import Person
from img_n_sound import *
from inputhandler import InputHandler

class Player(Person):
    
    def __init__(self,x=100,y=100):
        Person.__init__(self,x,y,'player.png')
        self.inputhandler = InputHandler()
        self.admin = False
        self.add_basic_movement()
        
    def add_basic_movement(self):
        self.jumping = self.onGround = False
        self.inputhandler.add_button('right')
        self.inputhandler.add_button('left')
        self.inputhandler.add_button('up')
        self.inputhandler.add_button('run')
        self.inputhandler.add_button('down')
        
    def get_button(self,button):
        return self.inputhandler.button_list[button]
    
    def set_button(self,button,state):
        self.inputhandler.button_list[button] = state
        
    def set_pos(self,x,y):
        self.rect.left = x
        self.rect.top = y
        
    def admin_tick(self):
        self.xvel = self.yvel = 0
        if self.get_button('right'):
            self.xvel = 5
        if self.get_button('left'):
            self.xvel = -5
        if self.get_button('up'):
            self.yvel = -5
        if self.get_button('down'):
            self.yvel = 5
            
        self.rect.left += self.xvel
        self.rect.top += self.yvel
        
    def tick(self,platforms):
        
        if self.get_button('right'):
            self.xvel = 4
        elif self.get_button('left'):
            self.xvel = -4
        else:
            self.xvel = 0
        if self.get_button('run'):
            self.xvel*=2
            
        if self.onGround:
            self.jumping = False
            
        if self.get_button('up') and self.onGround:
            self.yvel = -10
            self.set_button('up',False)


            
        

        
        
        Person.tick(self,platforms)