import math

class Vector:
    
    def __init__(self,**kargs):
        for stuff in kargs:
            self.__dict__[stuff] = kargs[stuff]
        if 'magnitude' in kargs:
            self.calc_vel()
        else:
            self = self.new_vector(self.xvel,self.yvel)
        
    def calc_vel(self):
        self.radians = self.angle / 2 / math.pi
        self.xvel = self.magnitude * math.cos(self.radians)
        self.yvel = self.magnitude * math.sin(self.radians)
        
    def get_vel(self):
        return self.xvel,self.yvel
    
    def get_angle(self):
        return self.angle
    
    def get_radian(self):
        self.radians = self.angle / 2 / math.pi
        return self.radians
    
    def get_mag(self):
        return self.magnitude
    
    def new_vector(self,xvel,yvel):
        if xvel != 0:
            angle = math.tanh(yvel/xvel)
        else:
            angle = 90
        mag = math.sqrt(xvel**2 + yvel**2)
        return Vector(angle=angle,magnitude=mag)
    
    def __add__(self,target):
        if type(target) == Vector:
            return self.new_vector(self.xvel+target.xvel, self.yvel + target.yvel)
        
    def __sub__(self,target):
        if type(target) == Vector:
            return self.new_vector(self.xvel-target.xvel, self.yvel - target.yvel)