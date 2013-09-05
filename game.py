import pygame,sys
from mode import Mode
from pygame.locals import *
from map import *
from fade import Fade
from loading import Loading
from player import Player

        
class Game(Mode):
    def __init__(self,screen):
        Mode.__init__(self,screen)
        #create a loading screen
        Loading(screen)
        #now do all the intial stuff
        self.surface.fill((255,255,255))
        screen.blit(self.surface,(0,0))
        self.stage = Stage()
        self.stage.load_stage('parkour')
        self.map = self.stage.rooms[0]
        self.fade = Fade(screen,'in',3)
        #add player
        self.player = Player(50,200)
        self.map.entity.append(self.player)
    
    def set_button(self,button,state):
        self.player.inputhandler.button_list[button] = state
        
    def tick(self,events):
        
        for e in events:
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.set_button('right',True)
                if e.key == K_LEFT:
                    self.set_button('left',True)
                if e.key == K_UP:
                    self.set_button('up',True)
                    self.player.jumping = True
                if e.key == K_LSHIFT:
                    self.set_button('run',True)
                if e.key == K_DOWN:
                    self.set_button('down',True)
                if e.key == K_r:
                    self.player.set_pos(50,200)
                if e.key == K_t:
                    if not self.player.admin:
                        self.player.admin = True
                    else:
                        self.player.admin = False
                
                if e.key == K_ESCAPE:
                    return 'Quit'

            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.set_button('right',False)
                if e.key == K_LEFT:
                    self.set_button('left',False)
                if e.key == K_LSHIFT:
                    self.set_button('run',False)
                if e.key == K_UP:
                    self.set_button('up',False)
                if e.key == K_DOWN:
                    self.set_button('down',False)


            elif e.type == QUIT:
                pygame.display.quit()
                sys.exit()
        if self.fade.loop():
            self.map.camera.update(self.player)
            if not self.player.admin:
                self.player.tick(self.map.platforms)
            elif self.player.admin:
                self.player.admin_tick()
    
    def render(self,screen):
        Mode.render(self,screen)
        for e in self.map.entity:
            screen.blit(e.image, self.map.camera.apply(e))
        screen.blit(self.fade.surface,(0,0))
    
    def __str__(self):
        return 'Game'
    