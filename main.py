import pygame

(width, height) = (800, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event == pygame.QUIT:
            break
