import pygame
from pygame.locals import K_ESCAPE, KEYDOWN


# Initialize pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = 255, 255, 255  # White
CIRCLE_COLOR = 0, 0, 255
DIAMETER = 10

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, CIRCLE_COLOR, (300, 200), DIAMETER)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
