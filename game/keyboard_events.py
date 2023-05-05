import pygame

class Keyboard:

    def quit_events(self, event):
        if event.type == pygame.QUIT:
            return False
        else:
            return True

    def x_events(self, event):
        if event.type == pygame.K_w:
            return 1
        if event.type == pygame.K_s:
            return -1
        else:
            return 0

    def y_events(self, event):
        if event.type == pygame.K_a:
            return -1
        elif event.type == pygame.K_d:
            return 1
        else:
            return 0