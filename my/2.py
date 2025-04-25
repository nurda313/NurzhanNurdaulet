# import pygame

# pygame.init()

# screen = pygame.display.set_mode(500, 500)

# image = pygame.image.load("ball1r.png")

# is_running = True

# while is_running:
#     screen.fill((255, 255, 255))

import pygame

# Инициализация
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение объекта")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры объекта
x = 300
y = 200
width = 50
height = 50
speed = 5

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - width:
        x += speed

    # Отрисовка объекта
    pygame.draw.rect(screen, BLUE, (x, y, width, height))
    pygame.display.update()

pygame.quit()
