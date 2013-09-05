from img_n_sound import *

class Animation():
    my_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','images')
    def __init__(self,folder,name):
        self.name = name
        self.frame = 0
        self.speed = 0.1
        self.animation = self.load_frames(folder,name)
        self.finished = False
        self.image = self.animation[self.frame]
        self.wait=0
        self.run = True
        self.unfreeze = False
        
    def load_frames(self,folder,name):
        return [load_image(f,-1,folder = (folder + '/' + name))[0] for f in os.listdir(os.path.join(Animation.my_path,folder,name)) if os.path.isfile(os.path.join(Animation.my_path,folder,name,f))]

    def reset(self):
        self.frame = 0
        self.finished = False
    
    def update(self,flipped):
        self.unfreeze = False
        if self.wait != 0:
            self.run = False
            self.wait-=1
        if self.wait==0 and not self.run:
            self.unfreeze = True
            self.run = True

        if self.run:
            if self.finished:
                self.frame = 0
                self.finished = False
            self.frame += self.speed
            self.image = pygame.transform.flip(self.animation[int(self.frame)],flipped,0)
            if self.frame >= len(self.animation)-self.speed:
                self.finished = True
        
            
    def get_image(self,index,flipped=False):
        return pygame.transform.flip(self.animation[index],flipped,0)
            
    def __str__(self):
        return self.name
