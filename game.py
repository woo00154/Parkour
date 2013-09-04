import pygame,sys
from mode import Mode
from pygame.locals import *

        
class Game(Mode):
    def __init__(self,screen):
        Mode.__init__(self,screen)
        
        

    def loop(self,events,screen):
        mode = self.tick(events)
        self.render(screen)
        return mode
    
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
        return 'Game'
    