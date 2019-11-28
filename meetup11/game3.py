import pygame
from pygame.locals import K_ESCAPE, K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN
from pygame.rect import Rect


# Initialize pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = 255, 255, 255  # White
CIRCLE_COLOR = 0, 0, 255
RADIUS = 10

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player variables
h_position = 10
v_position = 10


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    pass


# Run until the user asks to quit
running = True
while running:

    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            # Let's move the player
            if event.key == K_LEFT:
                h_position -= 5
            if event.key == K_RIGHT:
                h_position += 5
            if event.key == K_DOWN:
                v_position += 5
            if event.key == K_UP:
                v_position -= 5

        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, CIRCLE_COLOR, Rect(h_position, v_position, 10, 30))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
