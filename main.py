import pygame

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("thistle1")

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()