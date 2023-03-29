import pygame, sys #Imports the required libraries

pygame.init()

#Screen Creation
screenSize = screenWidth, screenHeight = 1120, 630 #16:9
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("RPG")

#Game Area
board = pygame.Rect(0, 0, screenWidth, screenHeight)
battleground = pygame.Rect(0, screenHeight/2, screenWidth, screenHeight)

#Player Creation
playerSize = playerWidth, playerHeight = 20, 20
playerPos = playerX, playerY = screenWidth/5, 3*screenHeight/5
player = pygame.Rect(playerX, playerY, playerWidth, playerHeight)

#Enemy Creation
enemySize = enemyWidth, enemyHeight = 20, 20
enemyPos = enemyX, enemyY = 4*screenWidth/5, 3*screenHeight/5
enemy = pygame.Rect(enemyX, enemyY, enemyWidth, enemyHeight)

#Player Movement
def playerMove(player):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player.move_ip(0, -5)

#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0, 0, 125)) #Temporary background

    playerMove(player)

    pygame.draw.rect(surface, (0, 125, 0), battleground)
    pygame.draw.rect(surface, (255, 255, 255), player)
    pygame.draw.rect(surface, (255, 0, 0), enemy)

    pygame.display.update(board)
