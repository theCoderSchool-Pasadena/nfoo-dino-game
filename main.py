from typing import Text
import pygame, sys
from pygame.locals import QUIT
# ---------------------------------------
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
dinoI = pygame.image.load("3089eee90487ab15d8c7401a2eeb04f1.png").convert_alpha()
cactusI = pygame.image.load("cactus1.png").convert_alpha()
cactus2I = pygame.image.load("cactus2.png").convert_alpha()
dino = pygame.Rect(20, 250, 20, 30)
dinoI = pygame.transform.scale_by(dinoI, 0.17)
cactusI = pygame.transform.scale_by(cactusI, 0.6)
cactus2I = pygame.transform.scale_by(cactus2I, 0.6)
clock = pygame.time.Clock()
cactus = pygame.Rect(280, 250, 25 , 40)
cactus2 = pygame.Rect(680, 250, 35, 45)
jump = 0
ground = 250
wall = 5
gravity = 0.3
MaxJump = 8
VelocityX = -2
cactusSpeed = 2
timeStamp = 0
Font = pygame.font.SysFont("arial", 30)
ScoreText = Font.render("Score: 0", False, (0,0,0))
Score = 0
Air = False
Run = True
# --------------------------------------
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
             pygame.quit()
             sys.exit()
   if not Run:
      keys=pygame.key.get_pressed() 
      if keys[pygame.K_SPACE]:
         Run = True
         Score = 0
         cactusSpeed = 2
         cactus.x = 280
         cactus2.x = 680
   if Run:        
      keys=pygame.key.get_pressed() 
      if keys[pygame.K_SPACE]:
         if dino.y >= 250:
            jump = 8
            
      DISPLAYSURF.fill("white")
      dino.y -= jump // 1
      if dino.y < ground:
         if jump > -MaxJump:
            jump -=gravity
      else:
         jump = 0;
   
      cactus.x -=cactusSpeed // 1
      cactus2.x -=cactusSpeed // 1
      if cactus.x < wall:
         cactus.x = 800
         cactus2.x = 400
         Score+=1
         print(f"Score: {Score}")
         
      if cactus2.x < wall:
         cactus2.x = 800
         cactus.x = 400
         Score+=1
         print(f"Score: {Score}")
      ticks = pygame.time.get_ticks()
      
      if ticks - timeStamp >= 10000:
         timeStamp = ticks

         print("Ten seconds have passed!")
         cactusSpeed+=0.5
         
                                                            
      
         
      
      ScoreText = Font.render(f"Score: {Score}", False, (0,0,0))
      DISPLAYSURF.fill("white")
      DISPLAYSURF.blit(ScoreText, (160,0))
      
      
         
      #pygame.draw.rect(DISPLAYSURF, "green", dino)
      #pygame.draw.rect(DISPLAYSURF, "black", cactus)
      DISPLAYSURF.blit(dinoI, dino)
      DISPLAYSURF.blit(cactusI, cactus)
      DISPLAYSURF.blit(cactus2I, cactus2)
      if dino.colliderect(cactus) or dino.colliderect(cactus2):
         Run = False
         ResetText = Font.render("SPACE to restart!", False, (0,0,0))
         DISPLAYSURF.fill("red")
         DISPLAYSURF.blit(ResetText, (80,0))
         
      pygame.display.update()
      
      clock.tick(60)