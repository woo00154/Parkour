#An editor for creating an easy tile based map
from mode import Mode
import pygame,sys
from pygame.locals import *

class Editor(Mode):
    
    def __init__(self,screen):
        Mode.__init__(self,screen)
        
    def tick(self,events):
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    return 'Quit'
            elif e.type == QUIT:
                pygame.display.quit()
                sys.exit()
    
    def render(self,screen):
        Mode.render(self,screen)
    
    def __str__(self):
        return 'Editor'