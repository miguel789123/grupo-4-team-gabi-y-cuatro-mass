class ShotInvaders:
  def __init__(self,win,x,y):
      self.x=x
      self.y=y
      self.w=4
      self.h=10
      self.win=win
  def show(self,cor):
      self.y +=1
      self.win.fill(cor,rect=[self.x,self.y,self.w,self.h])
