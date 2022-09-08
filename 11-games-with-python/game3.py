import pygame
from pygame.locals import K_ESCAPE, K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN
from pygame.rect import Rect


# Initialize pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = 255, 255, 255  # White
PLAYER_COLOR = 0, 0, 255  # Blue
RADIUS = 10

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill(PLAYER_COLOR)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        # Let's move the player
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)


player = Player()


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

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Draw a player
    screen.blit(player.surf, player.rect)

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
pygame.quit()
