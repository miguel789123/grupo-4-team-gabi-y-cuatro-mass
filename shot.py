class Shot:
  def __init__(self,win,shooting,x,y):
    self.x=x
    self.y=y
    self.w=4
    self.h=10
    self.win=win
    self.shooting=shooting
  
  def show(self, gltranlatefX, gltranlatefY,cor):
      if self.shooting:
        self.shooting=False
        if self.y <=0:
            self.x=gltranlatefX
            self.y=gltranlatefY
      if self.y>0:
          self.y -=2
      self.win.fill(cor,rect=[self.x,self.y,self.w,self.h])
      if self.y<20:
          self.y=-100
