import pygame,os
from pygame.locals import *
import xml.etree.ElementTree as ET
from img_n_sound import *
from camera import *


black = Color("#000000")

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, tx,ty):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_tileset(25,25,tx,ty)
        self.rect = Rect(x,y,w,h)
        

    def update(self):
        pass
    
    
class Map():
    def __init__(self):
        self.platforms = []
        self.objects = []
        self.entity = []
        self.people = []
        self.camera = Camera(complex_camera,800,600)
        
    def load_map(self,folder,name):
        tree = ET.parse(os.path.join('data','maps',folder,name))
        root = tree.getroot()
        for r in root:
            
            for o in r:
                
                if o.tag == 'tile':
                    print(o.attrib)
                    
                    target = Platform(int(o.attrib['x'])*25,int(o.attrib['y'])*25,25,25,int(o.attrib['tx']),int(o.attrib['ty']))
                    self.platforms.append(target)
                
                else:
                    
                    target = Object(int(o.attrib['x']),int(o.attrib['y']),o.tag+'.png',colorkey=None,folder='maps')
                    target.set_message('This is a ' + o.tag)
                    self.objects.append(target)
                self.entity.append(target)
        return self
    
    def add_platform(self,target):
        self.entity.append(target)
        self.platforms.append(target)
        
    def add_object(self,target):
        self.entity.append(target)
        self.objects.append(target)
        
class Stage():
    def __init__(self):
        
        self.rooms = []
        #self.add_floor()
        
    def load_stage(self,stage):
       
        for room in os.listdir(os.path.join('data','maps',stage)):
            
            self.add_room(stage,room)
            
        return self.rooms
        
    def add_room(self,stage,room):
        self.rooms.append(Map().load_map(stage,room))

        
