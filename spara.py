import pygame, sys
#from pygame.local import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

Screen = pygame.display.set_mode((1900, 1280)) #grandezza finestra
pygame.display.set_caption("Goku") #titolo della finestra 

bg = pygame.image.load('sfondo.png').convert()

sky = (0, 255, 255) #colore di sfondo
Screen.fill(sky)

gokuImg = pygame.image.load('goku1.png') #immagine del personaggio
nemicoImg = pygame.image.load('nemico.png')
sferaImg = pygame.image.load('sfera.png')
gokux = 900
gokuy = 750
nemicox = 10
nemicoy = 10
sferax = 935
sferay = 635
sferaxx=0
sferayy=0
direzione = 'right'
while True: #gameloop


	 attacca=10
         for event in pygame.event.get():
             if event.type == pygame.QUIT: #se X premuta chiude il gioco
                pygame.quit()
                sys.exit()
	     if event.type == pygame.KEYDOWN: #se l'evento e' di pressione di     un tasto allora 
                if event.key == pygame.K_UP:
			sferayy -= attacca
	 sferay += sferayy
         if direzione == 'right':
             nemicox += 5
	     if nemicox == 1850:
		nemicox = 0
         Screen.blit(bg, (0, 0))
         Screen.blit(nemicoImg, (nemicox, nemicoy))
         Screen.blit(gokuImg, (gokux, gokuy))
         Screen.blit(sferaImg, (sferax, sferay))
        





         pygame.display.update() #aggiorna la finestra
