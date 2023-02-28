import pygame, sys
from pygame.locals import *
import physics_objects as po


# Updates variables and processes stuff.
# Called once per frame.
# dt is the amount of time passed since last frame.
def update(dt):
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    po.solver.update(dt)


# Draws everything on the screen.
# Called once per frame. 
def draw(screen):
    # Clears everything on the screen by making it black. 
    screen.fill((0, 0, 0))
    
    # Display the constraint area.
    pygame.draw.circle(screen, (100, 100, 100), po.solver.constraint_center, po.solver.constraint_radius)
    
    # Display each circle. 
    for circ in po.all_circles:
        color = circ.color
        center = circ.curPos
        radius = circ.radius
        pygame.draw.circle(screen, color, center, radius)
        print(f'Drew {circ}')

    # Updates the display. 
    pygame.display.update()


def init():
    # Create a few circles. 
    for i in range(1, 4):
        po.circle(pygame.Vector2((i * 140)+400, 200), radius=i*10+10)
    po.circle.print_all()

# Runs the PyGame window.
def runPyGame():
    init()
    
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
