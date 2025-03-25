import pygame
import sys
import random

pygame.init()

# Окно
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Ball Eats Dots")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Мяч
radius = 25
x, y = width // 2, height // 2
speed = 20

# Еда (точка)
dot_radius = 10
dot_x = random.randint(dot_radius, width - dot_radius)
dot_y = random.randint(dot_radius, height - dot_radius)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Рисуем мяч
    pygame.draw.circle(screen, RED, (x, y), int(radius))

    # Рисуем точку
    pygame.draw.circle(screen, BLUE, (dot_x, dot_y), dot_radius)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_d] and x + radius + speed <= width:
        x += speed
    if keys[pygame.K_w] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_s] and y + radius + speed <= height:
        y += speed

    # Проверка столкновения с точкой (еда)
    distance = ((x - dot_x)**2 + (y - dot_y)**2) ** 0.5
    if distance <= radius + dot_radius:
        radius *= 1.1  # Увеличиваем на 10%
        # Новая точка в случайном месте
        dot_x = random.randint(dot_radius, width - dot_radius)
        dot_y = random.randint(dot_radius, height - dot_radius)

    clock.tick(60)

pygame.quit()
sys.exit()