from idlelib.config_key import WHITESPACE_KEYS

import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/pic1.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/pic2.jpg")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running= True
while running:
    pass


pygame.quit()