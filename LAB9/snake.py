import pygame
import random
import time

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
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

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

        # Проверка выхода за границы
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
        # Запрещаем поворот в противоположную сторону
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.direction = new_dir

# Класс еды
class Food:
    def __init__(self, snake):
        self.weight = random.choice([1, 2, 3])  # вес еды
        self.color = RED if self.weight == 1 else ORANGE if self.weight == 2 else YELLOW
        self.spawn_time = time.time()
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if [x, y] not in snake.body:
                self.position = [x, y]
                break

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

# Основной цикл игры
clock = pygame.time.Clock()
snake = Snake()
food = Food(snake)
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

    # Движение змейки
    if not snake.move():
        break

    # Проверка съедания еды
    if snake.body[0] == food.position:
        snake.grow = True
        score += food.weight  # увеличиваем очки на вес еды
        if score // 4 + 1 > level:
            level += 1
            speed += 2
        food = Food(snake)  # новая еда

    # Если еда "протухла", появится новая
    if time.time() - food.spawn_time > 5:  # через 5 секунд исчезает
        food = Food(snake)

    # Отображение еды и змейки
    food.draw()
    snake.draw()

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
