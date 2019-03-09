class Vector:
  def __init__(self,x=None,y=None):
    self.x,self.y = x,y
  def __add__(self,vec2):
    self.x += vec2.x
    self.y += vec2.y
    return Vector(self.x,self.y)
  def __sub__(self,vec2):
    self.x -= vec2.x
    self.y -= vec2.y 
    return Vector(self.x,self.y)
  def __mul__(self,num):
    self.x *= num 
    self.y *= num 
    return Vector(self.x,self.y)
  def __div__(self,num):
    self.x /= num 
    self.y /= num 
    return Vector(self.x,self.y)
  def __repr__(self):
    return "(%s, %s)"%(self.x, self.y)
