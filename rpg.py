import pygame, sys #Imports the required libraries

pygame.init()

#Screen Creation
screenSize = screenWidth, screenHeight = 1120, 630 #16:9
surface = pygame.display.set_mode(screenSize)
pygame.display.set_caption("RPG")

#Game Area
board = pygame.Rect(0, 0, screenWidth, screenHeight)


#Game Loop
#Using "while 1" instead of "while True" is more efficient
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((36, 36, 36)) #Temporary background

    pygame.display.update(board)
