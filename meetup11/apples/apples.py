import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, RLEACCEL

import config
from sprites import Apple, Basket


# Setup for sounds. Defaults are good.
pygame.mixer.init()

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Timer
counter, counter_text = 60, '60'.rjust(3)
COUNTDOWN = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWN, 1000)

# Create a custom event for adding a new enemy
ADDAPPLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDAPPLE, 1000)

# Instantiate the sprites
basket = Basket()

# Sprite groups
apples = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(basket)

# Sounds
yeah_sound = pygame.mixer.Sound("yeah.ogg")

# Run until the user asks to quit
running = True
while running:

    # Font init
    pygame.font.init()
    myfont = pygame.font.SysFont('Consolas', 30)

    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

        # Add a new enemy?
        if event.type == ADDAPPLE:
            # Create the new enemy and add it to sprite groups
            new_apple = Apple()
            apples.add(new_apple)
            all_sprites.add(new_apple)

        # Timer event
        if event.type == COUNTDOWN:
            counter -= 1
            if counter > 0:
                counter_text = str(counter).rjust(3)
            else:
                running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    basket.update(pressed_keys)

    # Update enemy position
    apples.update()

    # Fill the background with white
    screen.fill(config.BACKGROUND_COLOR)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any apples have collided with the basket
    apple_in_basket = pygame.sprite.spritecollideany(basket, apples)
    if apple_in_basket:
        # If so, then remove the player and stop the loop
        config.APPLES_IN_BASKET += 1
        yeah_sound.play()
        apple_in_basket.kill()

    # Show the amount of apples in the basket and the fallen ones
    apple_basket_counter = myfont.render(str(config.APPLES_IN_BASKET), False, (0, 128, 0))
    apple_floor_counter = myfont.render(str(config.APPLES_ON_FLOOR), False, (255, 0, 0))
    screen.blit(apple_basket_counter, (config.SCREEN_WIDTH - 40, 10))
    screen.blit(apple_floor_counter, (10, 10))
    # Show the time
    screen.blit(myfont.render(counter_text, True, (255, 255, 255)), (config.SCREEN_WIDTH / 2, 10))

    # Flip everything into the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
print("You caught {} apples".format(config.APPLES_IN_BASKET))
print("You dropped {} apples".format(config.APPLES_ON_FLOOR))
pygame.quit()
