import pygame.mixer
import pygame
import random
import invaders
import shot
import shot_invaders
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#inicializando
pygame.mixer.pre_init(44100, 16, 2, 4096) 
pygame.init()
win=pygame.display.set_mode((800,600))
font=pygame.font.SysFont("Arial",30)
inv_cor=(0,155,0)
out_screen=-100
stop_game=True
inv_speed=120
time_intro=1
blink_base=0
down=False
mov=False
game=True
done=True
h_score=0
s_step=0
bg_cor=0
vidas=-1
score=0
icol=10
ilin=5
step=1
rnd=0



game=True
#----------------- ------------------#
#s_inv =[]
#for i in range(4):
 # s_inv.append(i)
  #s_inv[i] = pygame.mixer.Sound("sonido/inv"+str(i)+".wav")
#s_explosion= pygame.mixer.Sound("sonido/explosion.wav")
#declarando objetos
inv=[]
for i in range(ilin):
  inv.append([0]*icol) 

for px in range(icol):
  for py in range(ilin):
    inv[py][px]=invaders.Invaders(win,False,0, 0,py,px*60+100,py*50+100)
#Base
base=invaders.Invaders(win,True,0,1,5,100,520)
#vidas
vida=invaders.Invaders(win,False,0,1,5,0,560)
#disco
disco =invaders.Invaders(win,False,0,0,5,1800,50)
#tiro
tiro=shot.Shot(win,1,out_screen,1) 
tiroinv1=shot_invaders.ShotInvaders (win,0,700)
tiroinv2=shot_invaders.ShotInvaders(win,0,700)
#reset game
def reset_game(next_stage):
    tiroinv1.x=out_screen
    tiroinv2.x=out_screen
    tiroinv1.y=100
    tiroinv2.y=100
    tiro.y=100
    disco.x=3000
    tiro.x=out_screen
    base.x=100
    if next_stage:
        for px in range(icol):
          for py in range(ilin):
            inv[py][px].x=px*60+100
            inv[py][px].y=py*50+100
            inv[py][px].hit=False


#colicion
def collision(A,B):
  return A.x + A.w>B.x and A.x<B.x+B.w and A.y + A.h>B.y and A.y<B.y + B.h

#2) -----------------------------------------------------#
#s_explosion.play()
#------------------------------------------------------#

while game:
  #tiempo del juego
  if step==inv_speed:
    step=0
  
  #introduccion
  if time_intro >500:
      time_intro=1
      bg_cor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  if time_intro >0:
      time_intro +=1 

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      game=False
  #color de fondo
  win.fill(bg_cor)

  #controles
  #eje x
  key=pygame.key.get_pressed()
  if key[K_LEFT] and base.x>60 and not stop_game:
    base.x -=1
  if key[K_RIGHT] and base.x<700 and not stop_game:
  
    base.x +=1

  #eje y  
  key=pygame.key.get_pressed()
  if key[K_UP] and base.x>60 and not stop_game:
    base.y -=1
  if key[K_DOWN] and base.x<700 and not stop_game:
  
    base.y +=1
    
  #disparar
    
  if key[K_SPACE] and vidas >0 and not stop_game:
    tiro.shooting=True
    
  
  #tiro invasores
    
  if tiroinv1.y >=600:
      rnd=random.randint(0,9)
  #explocion de base
  if not base.time_expl and vidas >=0 and base.hit:
      stop_game=False
      base.hit=False
      reset_game(False)
      blink_base=8
  #mostrar objetos
      
  if not(blink_base % 2):
      base.show(inv_cor)
  if blink_base:
      blink_base -=1
      pygame.time.delay(400)
  disco.show(inv_cor)

  for i in range(vidas):
      vida.x=100+i*50
      vida.show(inv_cor)

  if disco.x>800 and not disco.time_expl:
    #Texto
    font=pygame.font.SysFont("Arial",30)
    txt=font.render("SCORE",1,inv_cor)
    win.blit(txt,(20,10))
    txt=font.render(str(score),1,inv_cor)
    win.blit(txt,(50,40))
    txt=font.render("HI_SCORE",1,inv_cor)
    win.blit(txt,(350,10))
    txt=font.render(str(h_score),1,inv_cor)
    win.blit(txt,(390,40))
  elif time_intro:
      txt =font.render("......Team Gabi y sus lacayos XD...",0,inv_cor)
      win.blit(txt,(disco.x +42,44))

  tiro.show(base.x+20,base.y+10,inv_cor)  
  tiroinv1.show(inv_cor)
  tiroinv2.show(inv_cor)


  l=ilin-1
  for px in range(ilin):
    for py in range(icol):
      inv[px][py].face=(step<=inv_speed/2)
      inv[px][py].show(inv_cor)  
      if inv[px][py].x>720 and not inv[px][py].hit and not mov:
        mov=True
        down=True
      if inv[px][py].x<50 and not inv[px][py].hit and  mov:  
        mov=False
        down=True
      if mov:
        inv[px][py].x -=(not step)*15
      else:
        inv[px][py].x +=(not step)*15 
      #colicion
      if collision(tiro,inv[px][py]) and not inv[px][py].hit: 
         inv[px][py].hit=True
         inv[px][py].time_expl=30
         tiro.y=out_screen
         score +=15
      #tiro invasor aleatorio
      if not inv[l-px][rnd].hit and tiroinv1.y >600:
          tiroinv1.x=inv[l-px][rnd].x + inv[l-px][rnd].w / 2
          tiroinv1.x=inv[l-px][rnd].y + inv[l-px][rnd].h / 2
      #tiro invasor seguido
      if random.randint(0,2) and inv[l-px][rnd].x== base.x and  not inv[l-px][py].hit and tiroinv2.y > 600:
          tiroinv2.x =inv[l-px][py].x + inv[l-px][py].w / 2
          tiroinv2.y =inv[l-px][py].y + inv[l-px][py].h / 2

      #comprobar si los invasores fueron abatidos
      if not inv[px][py].hit: 
          done=False 
       

  if done:
      blink_base=10
      inv_speed -=20
      reset_game(True)
  done=True   


  #decender de los invasores
  if down:
    end=False
    for px in range(ilin):
      for py in range(icol):
         inv[px][py].y +=30
         #perder por invasor
         end=inv[px][py].y >480 and not inv[px][py].hit and not inv[px][py].time_expl
    down=False
    if end:
        time_intro= 1
        stop_game=True
        
  #atacando al disco
  if collision(tiro,disco):
      score +=100
     # s_disco.stop()
      disco.hit=True
      disco.time_expl=200
      tiro.x=out_screen
  #atacando a la nave
  if collision(tiroinv1,base) or collision(tiroinv2,base):
      base.time_expl=800
      stop_game=True
      base.hit=True
      vidas -=1
      if vidas ==0:
          time_intro=True
  if base.hit or stop_game:
      tiro.x=out_screen
      tiroinv1.x=out_screen 
      tiroinv2.x=out_screen
  if vidas < 0:
      stop_game=True
  #iniciar juego
  if  key[K_RETURN] and time_intro:
       score=0
       vidas=3
       bf_cor=0
       mov=False
       time_intro=0
       blink_base=8
       base.hit=False
       stop_game=False
       inv_speed=120
       reset_game(True)
  #Mover disco
  if disco.x<out_screen:
      disco.x=3000
      disco.hit=False
  if not disco.time_expl:
      disco.x -=1
  if not stop_game:
      step +=1
  
  if h_score<score:
      h_score=score

  
  pygame.display.update()
