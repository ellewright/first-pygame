import pygame
import random
import math

pygame.init()

GRAY = (105, 105, 105)

TITLE_FONT = pygame.font.SysFont("arial", 24, False, False)
BODY_FONT = pygame.font.SysFont("arial", 16, False, False)

FPS = 60
WIDTH = 800
HEIGHT = 600
HITBOX = 25

PLAYER_ICON = pygame.transform.scale_by(pygame.image.load("woman.png"), 0.1)
PLAYER_WIDTH = PLAYER_ICON.get_size()[0]
PLAYER_HEIGHT = PLAYER_ICON.get_size()[1]
PLAYER_SPEED = 5
PADDING_X = (PLAYER_WIDTH // 2)
PADDING_Y = (PLAYER_HEIGHT // 2)

player_x = (WIDTH // 2) - (PADDING_X)
player_y = HEIGHT - (PADDING_Y * 3)

HEART_ICON = pygame.transform.scale_by(pygame.image.load("heart.png"), 0.1)
HEART_WIDTH = HEART_ICON.get_size()[0]
HEART_HEIGHT = HEART_ICON.get_size()[1]
heart_x = random.randint(0, WIDTH - (PADDING_X + HEART_WIDTH))
heart_y = random.randint(0, HEIGHT - ((PADDING_Y * 3) + (HEART_HEIGHT)))

SECRETS = [
    "Ellie's girlfriend always knows how to make her smile.",
    "Ellie loves that her girlfriend is as much a cat person as she.",
    "Ellie's girlfriend has the same silly sense of humor as her.",
    "Ellie loves that her girlfriend is always looking out for others.",
    "Ellie's girlfriend has the best fashion, every color looks good on her.",
    "Ellie loves when her girlfriend takes care of her and makes her food.",
    "Ellie's girlfriend has the cutest dimples which look adorable smiling.",
    "Ellie loves her girlfriend's family, who took her in without question.",
    "Ellie's girlfriend is her favorite artist and she cherishes her paintings.",
    "Ellie loves her girlfriend's contagious laugh and carefree spirit."
]

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

def draw_title_screen():
    TITLE_TEXT = "Ellie needs your help, brave hero!"
    BODY_LINES = [
        "She dropped her heart vessels - each containing",
        "a special reason she loves her girlfriend.",
        "Can you get them back for her?"
    ]

    screen.fill("thistle1")

    title = TITLE_FONT.render(TITLE_TEXT, True, GRAY)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    screen.blit(title, title_rect)

    line_level = HEIGHT // 2
    for line in BODY_LINES:
        rendered_line = BODY_FONT.render(line, True, GRAY)
        line_rect = rendered_line.get_rect(center=(WIDTH // 2, line_level))
        screen.blit(rendered_line, line_rect)
        line_level += 20

    pygame.display.flip()
    pygame.time.delay(5000)

def draw_secret(secret):
    rendered_secret = BODY_FONT.render(secret, True, GRAY)
    secret_rect = rendered_secret.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rendered_secret, secret_rect)
    pygame.display.flip()

def main():
    global player_x, player_y, heart_x, heart_y
    secret_index = 0

    draw_title_screen()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if secret_index > len(SECRETS) - 1:
            running = False
            break
        
        screen.fill("thistle1")

        draw_heart(heart_x, heart_y)
        draw_player(player_x, player_y)
        control_movement()

        if has_collided(player_x, player_y, heart_x, heart_y):
            draw_secret(SECRETS[secret_index])
            pygame.time.delay(5000)
            heart_x = random.randint(0, WIDTH - (PADDING_X + (HEART_WIDTH // 2)))
            heart_y = random.randint(0, HEIGHT - ((PADDING_Y * 3) + (HEART_HEIGHT // 2)))
            secret_index += 1

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()