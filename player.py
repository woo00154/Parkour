import pygame
from person import Person
from img_n_sound import *
from inputhandler import InputHandler

class Player(Person):
    
    def __init__(self,spawn_x=100,spawn_y=100):
        Person.__init__(self,spawn_x,spawn_y,'player.png')
        self.inputhandler = InputHandler()
        self.admin = self.physics = self.parkour = False
        self.add_basic_movement()
        self.add_physics()
        self.add_parkour()
        self.add_stats()
        
    def add_basic_movement(self):
        self.jumping = self.onGround = False
        self.inputhandler.add_button('right')
        self.inputhandler.add_button('left')
        self.inputhandler.add_button('up')
        self.inputhandler.add_button('run')
        self.inputhandler.add_button('down')
        self.inputhandler.add_button('jump')
        
    def add_parkour(self):
        self.parkour = True
        self.hanging = self.onWall_R = self.onWall_L = self.climb = False
    
    def reset(self,entity):
        Person.reset(self,entity)
        self.health = 100
        self.dead = False
        self.add_physics()
        
        
    def add_physics(self):
        self.physics = True
        self.acc = 1
        self.speed_limit = 4
        self.walk_limit = 4
        self.run_limit = 8
        self.fall_time = 0
        self.wall_slide_limit = 20
        self.wall_slide_time = 0
        self.control = True
        
    def add_stats(self):
        self.health = 100
        self.exp = 0
        self.level = 1
        
        
    def get_button(self,button):
        return self.inputhandler.button_list[button]
    
    def set_button(self,button,state):
        self.inputhandler.button_list[button] = state
        

        
    def admin_tick(self):
        #allows the player to float around
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
        
    def x_movement(self):
        if self.physics:
            if self.get_button('right') and not self.get_button('left') and self.control:
                if self.xvel <= self.speed_limit:
                    self.xvel += self.acc
                else:
                    self.xvel -= self.acc
            elif self.get_button('left') and not self.get_button('right') and self.control:
                if self.xvel >= -self.speed_limit:
                    self.xvel -= self.acc
                else:
                    self.xvel += self.acc
            elif (self.get_button('left') and self.get_button('right') and self.control) or \
                (not self.get_button('left') and not self.get_button('right') and self.control):
                if self.xvel != 0:
                    self.xvel /= 2
                    if -1< self.xvel < 1:
                        self.xvel = 0
                #allows a player to run
            if self.get_button('run'):
                self.speed_limit = self.run_limit
            else:
                self.speed_limit = self.walk_limit
        else:
            if self.get_button('right') and not self.get_button('left'):
                self.xvel = 4
            elif not self.get_button('right') and self.get_button('left'):
                self.xvel = -4
            else:
                self.xvel = 0
            if self.get_button('run'):
                self.xvel *=2
                
    def wall_movement(self):
        if self.onWall and self.wall_slide_limit > self.wall_slide_time:
            #wall slide
            if self.yvel > 0:
                self.yvel = 2
                self.wall_slide_time += 1
            #if on ground, do nothing
            elif self.yvel==0 and not self.hanging:
                return
            self.jumping = True
            #wall jump
            if self.get_button('jump'):
                
                if self.onWall_R and self.get_button('right') and not self.get_button('left'):
                    self.yvel = -15
                    self.xvel = -5
                elif self.onWall_L and not self.get_button('right') and self.get_button('left'):
                    self.yvel = -15
                    self.xvel = 5
            #climb
            if self.get_button('up') and self.hanging:
                self.climb = True
                self.yvel = -15
                self.xvel = 0
        elif not self.onWall or self.hanging:
            self.wall_slide_time = 0
        
    def tick(self,platforms):
        #check if the character is dead or not
        if self.health <= 0:
            self.dead = True
        #make sure the charater has the control at certain point
        if not self.jumping or self.onWall or self.climb or self.hanging:
            self.control = True
        else:
            self.control = False
        

        self.onWall = self.onWall_L or self.onWall_R
        #all the x-component movements
        self.x_movement()
        #all wall-related movements

        self.wall_movement()
        
        #all the y-component movements    
        if self.onGround:
            self.jumping = self.climb = False

            
            
        if self.get_button('jump') and self.onGround:
            self.yvel = -15
            self.set_button('jump',False)
            self.jumping = True
        

        


        
        Person.tick(self,platforms)
        
        if self.yvel > 0 and not self.onWall:
            
            self.fall_time+=1
        elif self.onGround:
            self.health -= int(self.fall_time/25) * 100
        if self.yvel <= 0:
            self.fall_time = 0
    
