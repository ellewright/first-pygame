import pygame

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600

PLAYER_ICON = pygame.transform.scale_by(pygame.image.load("woman.png"), 0.1)
PLAYER_WIDTH = PLAYER_ICON.get_size()[0]
PLAYER_HEIGHT = PLAYER_ICON.get_size()[1]
PLAYER_SPEED = 5

player_x = (WIDTH / 2) - (PLAYER_WIDTH / 2)
player_y = HEIGHT - (PLAYER_HEIGHT * 1.5)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_player(x, y):
    screen.blit(PLAYER_ICON, (x, y))

def control_movement():
    global player_x, player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y - PLAYER_SPEED >= 0 + PLAYER_HEIGHT / 2:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_a] and player_x - PLAYER_SPEED >= 0 + PLAYER_WIDTH / 2:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_s] and player_y - PLAYER_SPEED < HEIGHT - (PLAYER_HEIGHT * 1.5):
        player_y += PLAYER_SPEED
    if keys[pygame.K_d] and player_x + PLAYER_SPEED < WIDTH - (PLAYER_WIDTH * 1.5):
        player_x += PLAYER_SPEED

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("thistle1")

    draw_player(player_x, player_y)
    control_movement()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()