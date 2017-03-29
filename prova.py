import pygame, sys
#from pygame.local import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

Screen = pygame.display.set_mode((1900, 1280)) #grandezza finestra
pygame.display.set_caption("Goku") #titolo della finestra 
sky = (0, 255, 255) #colore di sfondo
Screen.fill(sky)

gokuImg = pygame.image.load('goku.png') #immagine del personaggio
gokux = 10
gokuy = 10
direzione = 'right'
while True: #gameloop
         if direzione == 'right':
             gokux += 5
             if gokux == 200:
                 direzione == 'down'
         elif direzione == 'down':
             gokuy +=5
             if gokuy == 1260:
                 direzione == 'left'
         elif direzione == 'left':
             gokux -= 5
             if gokux == 10:
                 direzione == 'up'
         elif direzione == 'up':
             gokuy -= 5
             if gokuy == 10:
                 direzione == 'right'
         
         Screen.blit(gokuImg, (gokux, gokuy))



         for event in pygame.event.get():
             if event.type == pygame.QUIT: #se X premuta chiude il gioco
                pygame.quit()
                sys.exit()

         pygame.display.update() #aggiorna la finestra
