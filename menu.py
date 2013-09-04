#A basic menu before the game starts
#There should be another menu that pops up when ESC is pressed.

import pygame,sys
from pygame.locals import *
from button import Button

class Menu:
    def __init__(self,buttons,screen):
        self.surface = pygame.Surface(screen.get_size())    
        self.buttons = self.create_buttons(buttons)
        self.cursor = 0
        self.current_button = self.buttons[self.cursor]
        
    def create_buttons(self,buttons) -> list:
        button_list = []
        button_size = 50
        
        for b in buttons:
            button_list.append(Button(b,button_size))
    
        for b in button_list:
            if max(buttons,key=len) == str(b):
                w = b.rect.w
                h = b.rect.h
                x = self.surface.get_rect().centerx - w/2
                y = self.surface.get_rect().centery - len(buttons) * button_size / 2
            
        for b in button_list:
            b.set_pos(x,y)
            y += b.rect.h
            
        for b in button_list:
            self.surface.blit(b.name,b.rect) 
        
        self.selected = pygame.Surface((w,h))
        self.selected.fill((100,100,100))
        
        return button_list
    
    def loop(self,events,screen):
        mode = self.tick(events)
        self.render(screen)
        return mode
            
    def __str__(self):
        return 'Menu'
    
    def tick(self,events):
        
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_UP:
                    self.cursor -= 1
                if e.key == K_DOWN:
                    self.cursor += 1
                if e.key == K_RETURN:
                    return str(self.current_button)
                if e.key == K_ESCAPE:
                    return 'Quit'
            elif e.type == QUIT:
                pygame.display.quit()
                sys.exit()
                
        if self.cursor <= -1:
            self.cursor = len(self.buttons)-1
        elif self.cursor >= len(self.buttons):
            self.cursor = 0
        self.current_button = self.buttons[self.cursor]
        
        return str(self)
    
    def render(self,screen):
        self.selected.fill((255,255,255))
        self.selected.set_alpha(80)
        screen.blit(self.surface,(0,0))
        screen.blit(self.selected,self.current_button.get_pos())
        
            

