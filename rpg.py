import pygame, sys #Imports the required libraries

pygame.init()


#Screen Creation
screenSize = screenWidth, screenHeight = 1120, 630 #16:9
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("MONSTER SMASH")


#Addition of images for the game
character1Sprite = pygame.image.load('character/main_char_left.png')
character1Sprite = pygame.transform.flip(character1Sprite, True, False)
character2Sprite = pygame.image.load('character_variants/main_char_02_left.png')
character2Sprite = pygame.transform.flip(character2Sprite, True, False)
enemy1Sprite = pygame.image.load('character/enemy_01_left.png')
enemy2Sprite = pygame.image.load('character_variants/enemy_02_left.png')


#Game Areas
board = pygame.Rect(0, 0, screenWidth, screenHeight)
background = pygame.image.load('screens/bkg_image.png')
titleScreen = pygame.image.load('screens/title.png').convert_alpha()
titleScreen = pygame.transform.scale(titleScreen, (1120, 210))
gameoverScreen = pygame.image.load('screens/gameover_screen-03.png').convert_alpha()
gameoverScreen = pygame.transform.scale(gameoverScreen, (1120, 630))
victoryScreen = pygame.image.load('screens/victory_screen-02.png').convert_alpha()
victoryScreen = pygame.transform.scale(victoryScreen, (1120, 630))
gameStart = 0


#Character Creation
characterSize = characterWidth, characterHeight = 20, 20

character1Pos = character1X, character1Y = 3*screenWidth/20, 3*screenHeight/5
character1 = pygame.Rect(character1X, character1Y, characterWidth, characterHeight)
character1Jumped = 0
character1JumpDirection = -1
character1Health = 50
pressedD = 0

character2Pos = character2X, character2Y = 5*screenWidth/20, 4*screenHeight/5
character2 = pygame.Rect(character2X, character2Y, characterWidth, characterHeight)
character2Jumped = 0
character2JumpDirection = -1
character2Health = 50
pressedRight = 0


#Enemy Creation
enemySize = enemyWidth, enemyHeight = 20, 20
enemy1Pos = enemy1X, enemy1Y = (15*screenWidth/20) - enemyWidth, 3*screenHeight/5
enemy1 = pygame.Rect(enemy1X, enemy1Y, enemyWidth, enemyHeight)
enemy1Health = 50
enemy2Pos = enemy2X, enemy2Y = (17*screenWidth/20) - enemyWidth, 4*screenHeight/5
enemy2 = pygame.Rect(enemy2X, enemy2Y, enemyWidth, enemyHeight)
enemy2Health = 50


#Phases and Subphases
playerPhase = 1 #If true, then it's the player phase. If false, then it's the enemy phase.
character1Animation = 1 #If true, then it's character1's turn. If false, it's character2's turn.
enemy1Animation = 1 #If true, then it's enemy1's turn to attack. If false, it's enemy2's turn.


#FPS
clock = pygame.time.Clock()


#UI
font = pygame.font.Font("Jura.ttf", 50)
character1Right = font.render("D", True, (255, 255, 255))
character2Right = font.render(">", True, (255, 255, 255))


#Player Movement
def characterMove(char1, char2, enem1, enem2, dt):
    global character1X, character1Y, character1Jumped, character1JumpDirection, character2X, character2Y, character2Jumped, character2JumpDirection
    global character1Sprite, character2Sprite, playerPhase, character1Animation, character1Right, character2Right, enemy1Health, enemy2Health
    global pressedD, pressedRight
    key = pygame.key.get_pressed()

    if playerPhase:
        #Character1 Turn
        if character1Animation:
            character1Sprite = pygame.image.load('character/main_char_01.png') #Character1 is waiting for your decision...
            surface.blit(character1Right, (character1X+50, character1Y-75)) #Onscreen button prompt
            if key[pygame.K_d] or pressedD:
                pressedD = 1
                character1Sprite = pygame.image.load('character/main_char_left.png')
                character1Sprite = pygame.transform.flip(character1Sprite, True, False)
                if char1.left < 1120:
                    char1.move_ip(1*dt, 0)
                    char1.left += dt
                else:
                    char1.update(character1X, character1Y, characterWidth, characterHeight)
                    char1.left = character1X
                    pressedD = 0
                    character1Animation = 0 #After animation is done, the char2 animation begins
            if char1.colliderect(enem1):
                    enemy1Health -= 10
            if char1.colliderect(enem2):
                    enemy2Health -= 10
        #Character2 Turn
        else:
            character2Sprite = pygame.image.load('character_variants/main_char_02.png') #Character2 is waiting for your decision...
            surface.blit(character2Right, (character2X+50, character2Y-75)) #Onscreen button prompt
            if key[pygame.K_RIGHT] or pressedRight:
                pressedRight = 1
                character2Sprite = pygame.image.load('character_variants/main_char_02_left.png')
                character2Sprite = pygame.transform.flip(character2Sprite, True, False)
                if char2.left < 1120:
                    char2.move_ip(1*dt, 0)
                    char2.left += dt
                else:
                    char2.update(character2X, character2Y, characterWidth, characterHeight)
                    char2.left = character2X
                    pressedRight = 0
                    character1Animation = 1
                    playerPhase = 0
            if char2.colliderect(enem1):
                    enemy1Health -= 10
            if char2.colliderect(enem2):
                    enemy2Health -= 10
    else:
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
                    character1JumpDirection *= 2                        #The character speeds up coming from the top due to gravity.
            if char1.top <= character1Y - 200: #The maximum height of the jump is reached.
                character1JumpDirection *= -1
            if char1.top >= character1Y: #The jump is finished.
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
            if char2.top >= character2Y:
                character2Jumped = 0


#Enemy Movement
def enemyMove(enem1, enem2, char1, char2, dt):
    global playerPhase, enemy1Animation, character1Health, character2Health

    #Glitch: If the player jumps at the end of the enemy phase, then they'll float above the ground.

    if not playerPhase:
        #Enemy1 Attack Animation
        if enemy1Animation:
            if enem1.left+enem1.width > 0:
                enem1.move_ip(-1*dt, 0) #Temporary animation. The attack will be based off rng.
                enem1.left -= dt
                if enem1.colliderect(char1):
                    character1Health -= 10
                if enem1.colliderect(char2):
                    character2Health -= 10
            else:
                enem1.update(enemy1X, enemy1Y, enemyWidth, enemyHeight)
                enem1.left = enemy1X
                enemy1Animation = 0 #After animation is done, the enemy2 animation begins
        #Enemy2 Attack Animation
        else:
            if enem2.left+enem2.width > 0:
                enem2.move_ip(-1*dt, 0)
                enem2.left -= dt
                if enem2.colliderect(char1):
                    character1Health -= 10
                if enem2.colliderect(char2):
                    character2Health -= 10
            else:
                enem2.update(enemy2X, enemy2Y, enemyWidth, enemyHeight)
                enem2.left = enemy2X
                enemy1Animation = 1
                playerPhase = 1 #After animation is done, the player phase begins


#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #print(character1Health)

    deltaTime = clock.tick(60)/2 #The time that has passed since the last call to clock.tick(), capped at 60 fps. Divided by 2 to make things slower.

    #Drawing Sprites
    if (not gameStart):
        #Title Screen
        surface.blit(titleScreen, (0, 0))
        if (key[pygame.K_SPACE]):
            gameStart = 1
    else:
        #Victory Screen
        if enemy1Health <= 0 and enemy2Health <= 0:
            surface.blit(victoryScreen, (0, 0))
        #Gameplay Loop
        elif character1Health >= 0 or character2Health >= 0:
            surface.blit(background, (0, 0))
            surface.blit(character1Sprite,(character1.left-60, character1.top-100))
            surface.blit(character2Sprite,(character2.left-60, character2.top-100))
            surface.blit(enemy1Sprite,(enemy1.left-60, enemy1.top-100))
            surface.blit(enemy2Sprite,(enemy2.left-60, enemy2.top-100))

            #Movement Animations
            characterMove(character1, character2, enemy1, enemy2, deltaTime)
            enemyMove(enemy1, enemy2, character1, character2, deltaTime)

            #Hitboxes
            pygame.draw.rect(surface, (255, 255, 255), character1)
            pygame.draw.rect(surface, (255, 255, 255), character2)
            pygame.draw.rect(surface, (255, 0, 0), enemy1)
            pygame.draw.rect(surface, (255, 0, 0), enemy2)
        #Gameover Screen
        else:
            surface.blit(gameoverScreen, (0, 0))

    pygame.display.update(board)
