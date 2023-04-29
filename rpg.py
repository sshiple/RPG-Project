import pygame, sys #Imports the required libraries

pygame.init()


#Screen Creation
screenSize = screenWidth, screenHeight = 1120, 630 #16:9
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("RPG")

#addition of images for the game
background = pygame.image.load('bkg_image.png')
mainCharacter = pygame.image.load('main_char_01.png')


#Game Area
board = pygame.Rect(0, 0, screenWidth, screenHeight)
battleground = pygame.Rect(0, screenHeight/2, screenWidth, screenHeight)


#Character Creation
characterSize = characterWidth, characterHeight = 20, 20

character1Pos = character1X, character1Y = 4*screenWidth/20, 3*screenHeight/5
character1 = mainCharacter
mainCharacter = pygame.Rect(character1X, character1Y, characterWidth, characterHeight)
#character1 = pygame.Rect(character1X, character1Y, characterWidth, characterHeight)
character1Jumped = 0
character1JumpDirection = -1
character2Pos = character2X, character2Y = 3*screenWidth/20, 4*screenHeight/5
character2 = pygame.Rect(character2X, character2Y, characterWidth, characterHeight)
character2Jumped = 0
character2JumpDirection = -1


#Enemy Creation
enemySize = enemyWidth, enemyHeight = 20, 20
enemy1Pos = enemy1X, enemy1Y = (16*screenWidth/20) - enemyWidth, 3*screenHeight/5
enemy1 = pygame.Rect(enemy1X, enemy1Y, enemyWidth, enemyHeight)
enemy2Pos = enemy2X, enemy2Y = (17*screenWidth/20) - enemyWidth, 4*screenHeight/5
enemy2 = pygame.Rect(enemy2X, enemy2Y, enemyWidth, enemyHeight)


#FPS
clock = pygame.time.Clock()


#Player Movement
def characterMove(char1, char2):
    global character1Y, character1Jumped, character1JumpDirection, character2Y, character2Jumped, character2JumpDirection
    key = pygame.key.get_pressed()
    dt = clock.tick(60) #The time that has passed since the last call to clock.tick(), capped at 60 fps

    #Character1 Jump
    if key[pygame.K_w] and not character1Jumped:
        character1JumpDirection = -1 * dt
        character1Jumped = 1
    elif character1Jumped:
        char1.move_ip(0, character1JumpDirection)
        char1.top += character1JumpDirection
        if char1.top == character1Y - 160: #4/5th of the jump height
            if character1JumpDirection < 0:
                character1JumpDirection = character1JumpDirection/2 #The character slows down as they reach the top of the jump
            else:
                character1JumpDirection *= 2              #The character speeds up coming from the top due to gravity.
        if char1.top <= character1Y - 200: #The maximum height of the jump is reached.
            character1JumpDirection *= -1
        if char1.top == character1Y: #The jump is finished
            character1Jumped = 0

    #Character2 Jump
    if key[pygame.K_UP] and not character2Jumped:
        character2JumpDirection = -1 * dt
        character2Jumped = 1
    elif character2Jumped:
        char2.move_ip(0, character2JumpDirection)
        char2.top += character2JumpDirection
        if char2.top == character2Y - 160:
            if character2JumpDirection < 0:
                character2JumpDirection = character2JumpDirection/2
            else:
                character2JumpDirection *= 2
        if char2.top <= character2Y - 200:
            character2JumpDirection *= -1
        if char2.top == character2Y:
            character2Jumped = 0


#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0, 0, 125)) #Temporary background
    surface.blit(background, (0,0)) #new background
    surface.blit(character1,(0,0)) #

    characterMove(character1, character2)

    #pygame.draw.rect(surface, (0, 125, 0), battleground)
   #pygame.draw.rect(surface, (255, 255, 255), character1)
    pygame.draw.rect(surface, (255, 255, 255), character2)
    pygame.draw.rect(surface, (255, 0, 0), enemy1)
    pygame.draw.rect(surface, (255, 0, 0), enemy2)

    pygame.display.update(board)
