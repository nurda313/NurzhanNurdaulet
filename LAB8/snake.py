import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.SysFont("Arial", 24)

# Класс Змейки
class Snake:
    def __init__(self):
        self.body = [[100, 100]]
        self.direction = [CELL_SIZE, 0]  # Изначально вправо
        self.grow = False

    def move(self):
        head = self.body[0][:]
        head[0] += self.direction[0]
        head[1] += self.direction[1]

        # Проверка выхода за пределы экрана
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return False

        # Проверка на столкновение с собой
        if head in self.body:
            return False

        self.body.insert(0, head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    def change_direction(self, new_dir):
        # Чтобы нельзя было повернуть в противоположную сторону
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.direction = new_dir

# Функция генерации еды

def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if [x, y] not in snake.body:
            return [x, y]

# Основной цикл игры
clock = pygame.time.Clock()
snake = Snake()
food = generate_food(snake)
speed = 10
score = 0
level = 1
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction([0, -CELL_SIZE])
            elif event.key == pygame.K_DOWN:
                snake.change_direction([0, CELL_SIZE])
            elif event.key == pygame.K_LEFT:
                snake.change_direction([-CELL_SIZE, 0])
            elif event.key == pygame.K_RIGHT:
                snake.change_direction([CELL_SIZE, 0])

    # Движение змеи
    if not snake.move():
        break  # Конец игры

    # Проверка съедания еды
    if snake.body[0] == food:
        snake.grow = True
        score += 1
        food = generate_food(snake)

        # Уровень повышается каждые 4 очка
        if score % 4 == 0:
            level += 1
            speed += 2  # Увеличиваем скорость

    # Отображение еды
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Отображение змейки
    snake.draw()

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
