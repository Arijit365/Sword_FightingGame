import random

import pygame

# initialize the pygame module
pygame.init()

# create the screen
screen = pygame.display.set_mode( (800, 600) )
# add background
screen = pygame.image.load('dark-sky.jpg')
# add icon and title
pygame.display.set_caption( " Forever Knights" )
icon = pygame.image.load( 'swords.png' )
pygame.display.set_icon( icon )
# Player 1
playerImg = pygame.image.load( 'ninja.png' )
playerX = 6
playerY = 4
playerX_change = 0

def player(X, Y):
    screen.blit( playerImg, (X, Y) )
# add enemy
enemyIMG = pygame.image.load('dragon (1).png')
enemyX = random.randint(0 , 800) # random.randint--> change the position of character randomly
enemyY = random.randint(50 , 150)
enemyX_change = 0
enemyY_change = 40

def enemy(X , Y):
     screen.blit(enemyIMG, (X , Y))

# add special power in the enemy
fireIMG = pygame.image.load()
fireX = random.randint(0 ,800)
fireY = random.randint(0 , 150)
fireX_change = 4
fireY_change = 40
def fire(X , Y):
     screen.blit(fireIMG,(X , Y))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# if key is pressed then checked that the charcter posuition changed right or left
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3
        if event.key == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
# RGB color for the background changing
screen.fill( (0, 0, 0) )
#add a background image in the game
screen.blit(background , (0 , 0))
# logic on the keyboard movement
# 5 = 5 + -0.1 -> 5 = 5 - 0.1
# 5 = 5 + 0.1
playerX += playerX_change
# add boundaries of the game and the png file in screen
if playerX <= 0:
    playerX = 0
  elif playerX >= 736:
      playerX = 736
# enemy movement
enemyX += enemyX_change
# add boundaries of the game and the png file in screen
if enemyX <= 0:
    enemyX = -0.3
    enemyY += enemyY_change
  elif enemyX >= 736:
      enemyX = 0.3
      enemyY += enemyY_change


player( playerX, playerY )
enemy(enemyX , enemyY)
pygame.display.update()
