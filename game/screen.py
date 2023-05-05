import pygame
from keyboard_events import Keyboard

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def screening(self):
        pygame.init()
        pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Student Nightmares")