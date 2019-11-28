import random

import pygame
from pygame.locals import K_LEFT, K_RIGHT, RLEACCEL

import config


# Define a Basket object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'basket'
class Basket(pygame.sprite.Sprite):
    # Basket configuration
    color = 255, 0, 255  # Pink
    width = 50
    height = 40
    size = width, height
    # Basket position
    h_position = int(config.SCREEN_WIDTH / 2)
    v_position = config.SCREEN_HEIGHT - height / 2
    # basket speed
    speed = 10

    def __init__(self):
        super(Basket, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(self.h_position, self.v_position))

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH:
            self.rect.right = config.SCREEN_WIDTH


# Define an Apple object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'apple'
class Apple(pygame.sprite.Sprite):

    # Apple configuration
    color = 153, 204, 0
    diameter = 15
    # Apple position
    h_position = 150
    v_position = 0 + diameter
    # Apple speed
    speed = 5

    def __init__(self):
        super(Apple, self).__init__()
        self.surf = pygame.image.load("apple.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.diameter, config.SCREEN_WIDTH),
                0,
            )
        )

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= config.SCREEN_HEIGHT:
            config.APPLES_ON_FLOOR += 1
            self.kill()
