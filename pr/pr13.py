import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Снеговик")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
BLUE = (100, 149, 237)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLUE)

    pygame.draw.circle(screen,WHITE, (300, 450), 40, 100)
    pygame.draw.circle(screen,WHITE, (300, 300), 80, 70)
    pygame.draw.circle(screen,WHITE, (300, 180), 160, 50)

    pygame.draw.circle(screen,BLACK, (285, 170),7)
    pygame.draw.circle(screen,BLACK, (315, 170),7)

    pygame.draw.polygon(screen,ORANGE,[(300, 180), (340, 190), (340, 190)])

    pygame.draw.circle(screen,BLACK, (300, 270), 7)
    pygame.draw.circle(screen,BLACK , (300, 300), 7)
    pygame.draw.circle(screen,BLACK, (300, 330), 7)

    pygame.draw.rect(screen,BLACK, (260, 130, 80, 20))

    pygame.draw.rect(screen,BLACK, (275, 90, 50, 50))




pygame.display.flip()
clock.tick(60)