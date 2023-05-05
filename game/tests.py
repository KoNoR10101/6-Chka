import pygame

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode(500, 500)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()