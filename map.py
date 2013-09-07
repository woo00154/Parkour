import pygame,os
from pygame.locals import *
import xml.etree.ElementTree as ET
from img_n_sound import *
from camera import *
from platform import Platform
from object import Object




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
                    size = 25
                    
                    target = Platform(int(o.attrib['x'])*size,int(o.attrib['y'])*size,int(o.attrib['tx']),int(o.attrib['ty']),size)
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

        
