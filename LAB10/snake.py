import pygame
import psycopg2
import random

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="snake_db",
    user="postgres",
    password="yourpassword"
)
cur = conn.cursor()

# Создание таблиц
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
''')
cur.execute('''
    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1
    );
''')
conn.commit()

# Запрос username
username = input("Enter your username: ")

# Проверка существующего пользователя
cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s;", (user_id,))
    data = cur.fetchone()
    if data:
        score, level = data
    else:
        score, level = 0, 1
else:
    # Создаем нового пользователя
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    score, level = 0, 1
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s);", (user_id, score, level))
    conn.commit()

# Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Snake - User: {username} Level: {level}")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Arial", 24)

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [[100, 100]]
        self.direction = [CELL_SIZE, 0]
        self.grow = False

    def move(self):
        head = self.body[0][:]
        head[0] += self.direction[0]
        head[1] += self.direction[1]

        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in self.body:
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
        if (new_dir[0] != -self.direction[0] or new_dir[1] != -self.direction[1]):
            self.direction = new_dir

def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        if [x, y] not in snake.body:
            return [x, y]

clock = pygame.time.Clock()
snake = Snake()
food = generate_food(snake)

# Скорость и уровень
speed = 10 + (level - 1) * 2
running = True
paused = False

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
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    # Сохраняем результат
                    cur.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = %s;", (score, level, user_id))
                    conn.commit()

    if paused:
        pause_text = font.render("Paused", True, WHITE)
        screen.blit(pause_text, (WIDTH//2 - 50, HEIGHT//2))
        pygame.display.flip()
        continue

    if not snake.move():
        break

    if snake.body[0] == food:
        snake.grow = True
        score += 1
        food = generate_food(snake)
        if score % 5 == 0:
            level += 1
            speed += 2

    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    snake.draw()

    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

# Финальное сохранение при завершении игры
cur.execute("UPDATE user_scores SET score = %s, level = %s WHERE user_id = %s;", (score, level, user_id))
conn.commit()

pygame.quit()
cur.close()
conn.close()
