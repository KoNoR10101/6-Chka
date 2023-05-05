import pygame
from screen import Screen
from keyboard_events import Keyboard

screen = Screen(500, 500)
keyboard = Keyboard()
running = True

while running:
    screen.screening()
    for event in pygame.event.get():
        running = keyboard.quit_events(event)
        x = keyboard.x_events(event)
        y = keyboard.y_events(event)
