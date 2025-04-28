import pygame
import random
import math

pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
HITBOX = 25

PLAYER_ICON = pygame.transform.scale_by(pygame.image.load("woman.png"), 0.1)
PLAYER_WIDTH = PLAYER_ICON.get_size()[0]
PLAYER_HEIGHT = PLAYER_ICON.get_size()[1]
PLAYER_SPEED = 5
PADDING_X = (PLAYER_WIDTH / 2)
PADDING_Y = (PLAYER_HEIGHT / 2)

player_x = (WIDTH / 2) - (PADDING_X)
player_y = HEIGHT - (PADDING_Y * 3)

HEART_ICON = pygame.transform.scale_by(pygame.image.load("heart.png"), 0.1)
HEART_WIDTH = HEART_ICON.get_size()[0]
HEART_HEIGHT = HEART_ICON.get_size()[1]
heart_x = random.randint(0, WIDTH - math.floor(PADDING_X + (HEART_WIDTH / 2)))
heart_y = random.randint(0, HEIGHT - math.floor((PADDING_Y * 3) + (HEART_HEIGHT / 2)))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def draw_player(x, y):
    screen.blit(PLAYER_ICON, (x, y))

def draw_heart(x, y):
    screen.blit(HEART_ICON, (x, y))

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

def has_collided(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
    if distance < HITBOX:
        return True

    return False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("thistle1")

    draw_heart(heart_x, heart_y)
    draw_player(player_x, player_y)
    control_movement()

    if has_collided(player_x, player_y, heart_x, heart_y):
        heart_x = random.randint(0, WIDTH - math.floor(PADDING_X + (HEART_WIDTH / 2)))
        heart_y = random.randint(0, HEIGHT - math.floor((PADDING_Y * 3) + (HEART_HEIGHT / 2)))  

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()