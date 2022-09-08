import pygame
from pygame.locals import K_ESCAPE, K_LEFT, K_RIGHT, KEYDOWN, QUIT


# Initialize pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BACKGROUND_COLOR = 255, 255, 255  # White

# Set up the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# Define a Basket object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'basket'
class Basket(pygame.sprite.Sprite):
    # Basket configuration
    basket_color = 255, 0, 255  # Pink
    basket_width = 50
    basket_height = 40
    basket_size = basket_width, basket_height
    # Basket position
    h_position = 10
    v_position = SCREEN_HEIGHT - basket_height - 10
    # basket speed
    basket_step = 20

    def __init__(self):
        super(Basket, self).__init__()
        self.surf = pygame.Surface((self.basket_width, self.basket_height))
        self.surf.fill(self.basket_color)
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# Define an Apple object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'apple'
class Apple(pygame.sprite.Sprite):

    # Apple configuration
    apple_color = 153, 204, 0
    apple_diameter = 15
    # Apple position
    h_position = 150
    v_position = 0 + apple_diameter
    # Apple speed
    apple_step = 1

    def __init__(self):
        super(Apple, self).__init__()
        self.surf = pygame.Surface((self.apple_diameter, self.apple_diameter))
        self.surf.fill(self.apple_color)
        self.rect = self.surf.get_rect()


# Instantiate the sprites
basket = Basket()
apple = Apple()


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

    # Update the player sprite based on user keypresses
    basket.update(pressed_keys)

    # Fill the background with white
    screen.fill(BACKGROUND_COLOR)

    # Create a surface and pass in a tuple containing its length and width
    #basket = pygame.Surface(basket.basket_size)

    # Give the surface a color to separate it from the background
    #basket.fill(basket.basket_color)
    #rect = basket.get_rect()

    # Draw the basket
    screen.blit(basket.surf, basket.rect)

    # Draw the apple
    screen.blit(apple.surf, apple.rect)

    # Draw the apples
    #pygame.draw.circle(screen, apple.apple_color, (apple.h_apple_position, apple.v_apple_position), apple.apple_diameter)

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (400, 300), 10)
    #pygame.draw.(screen, (0, 0, 255), (400, 300), 10)

    # Flip the display
    pygame.display.flip()
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

    # Move the apple down
    apple.v_position += apple.apple_step

# Done! Time to quit.
pygame.quit()
