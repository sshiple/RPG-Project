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
playerPos = playerX, playerY = 224, 378 #screenWidth/5, 3*screenHeight/5
player = pygame.Rect(playerX, playerY, playerWidth, playerHeight)
jumpDirection = -2
jumped = 0

#Enemy Creation
enemySize = enemyWidth, enemyHeight = 20, 20
enemyPos = enemyX, enemyY = 4*screenWidth/5, 3*screenHeight/5
enemy = pygame.Rect(enemyX, enemyY, enemyWidth, enemyHeight)


#Player Movement
def playerMove(player):
    global playerY, jumpDirection, jumped
    key = pygame.key.get_pressed()

    #Jump
    if jumped:
        player.move_ip(0, jumpDirection)
        playerY += jumpDirection
        if playerY == 218: #4/5th of the jump height
            if jumpDirection < 0:
                jumpDirection = jumpDirection/2 #The player slows down as they reach the top of the jump
            else:
                jumpDirection *= 2              #The player speeds up coming from the top due to gravity.
        if playerY == 178: #After 100 frames, the maximum height of the jump is reached.
            jumpDirection *= -1
        if playerY == 378: #After another 100 frames, the jump is finished
            jumped = 0
    elif key[pygame.K_w]:
        jumpDirection = -2
        jumped = 1


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
