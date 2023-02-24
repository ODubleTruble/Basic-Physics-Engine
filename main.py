import pygame, sys
from pygame.locals import *


# Updates variables and processes stuff.
# Called once per frame.
# dt is the amount of time passed since last frame.
def update(dt):
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


# Draws everything on the screen.
# Called once per frame. 
def draw(screen):
    # Clears everything on the screen by making it black. 
    screen.fill((0, 0, 0))

    # Updates the display. 
    pygame.display.update()


# Runs the PyGame window.
def runPyGame():
    pygame.init()
    
    FPS = 60
    fpsClock = pygame.time.Clock()
    
    WINDOW_SIZE = (pygame.display.get_desktop_sizes()[0][0]/1.5, pygame.display.get_desktop_sizes()[0][1]/1.5)
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption('Dislpay Name')

    dt = 0
    
    # The main game loop.
    while True:
        update(dt)
        draw(screen)

        # dt is time since the last frame.
        # Pauses the program to create the correct FPS. 
        dt = fpsClock.tick(FPS)


runPyGame()
