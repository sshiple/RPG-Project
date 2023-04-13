import pygame, sys #Imports the required libraries

pygame.init()

#Screen Creation
screenSize = screenWidth, screenHeight = 1120, 630 #16:9
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("RPG")

#Game Area
board = pygame.Rect(0, 0, screenWidth, screenHeight)
battleground = pygame.Rect(0, screenHeight/2, screenWidth, screenHeight)

#character Creation
characterSize = characterWidth, characterHeight = 20, 20

character1Pos = character1X, character1Y = 224, 378 #screenWidth/5, 3*screenHeight/5
character1 = pygame.Rect(character1X, character1Y, characterWidth, characterHeight)
character2Pos = character2X, character2Y = 324, 378 #screenWidth/5, 3*screenHeight/5
character2 = pygame.Rect(character1X, character1Y, characterWidth, characterHeight)

jumpDirection = -2
jumped = 0



#Enemy Creation
enemySize = enemyWidth, enemyHeight = 20, 20
enemyPos = enemyX, enemyY = 4*screenWidth/5, 3*screenHeight/5
enemy = pygame.Rect(enemyX, enemyY, enemyWidth, enemyHeight)


#Player Movement
def characterMove(character):
    global character1Y, jumpDirection, jumped
    key = pygame.key.get_pressed()

    #Jump
    if jumped:
        character1.move_ip(0, jumpDirection)
        character1Y += jumpDirection
        if character1Y == 218: #4/5th of the jump height
            if jumpDirection < 0:
                jumpDirection = jumpDirection/2 #The character slows down as they reach the top of the jump
            else:
                jumpDirection *= 2              #The character speeds up coming from the top due to gravity.
        if character1Y == 178: #After 100 frames, the maximum height of the jump is reached.
            jumpDirection *= -1
        if character1Y == 378: #After another 100 frames, the jump is finished
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

    characterMove(character1)

    pygame.draw.rect(surface, (0, 125, 0), battleground)
    pygame.draw.rect(surface, (255, 255, 255), character1)
    pygame.draw.rect(surface, (255, 0, 0), enemy)

    pygame.display.update(board)
