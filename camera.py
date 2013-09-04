from pygame.locals import *


class Camera(object):
    def __init__(self,camera_func, w, h):
        self.camera_func = camera_func
        self.state = Rect(0,0,w,h)
    
    def apply(self,target):
        return target.rect.move(self.state.topleft)
    
    def update(self,target):
        self.state = self.camera_func(self.state, target.rect)
        
def complex_camera(camera,target_rect):
    l,t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+400, -t + 300, w, h
    
    l = min(0,l)
    l = max(-(camera.w-800),l)
    t = max(-(camera.h-600),t)
    t = min(0,t)
    
    return Rect(l, t, w, h)