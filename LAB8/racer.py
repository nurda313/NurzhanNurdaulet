import pygame
import random

# Инициализируем Pygame
pygame.init()

# Размеры окна
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Установка FPS
clock = pygame.time.Clock()

# Загрузка изображений
road = pygame.image.load("road.png")       # фон дороги
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (50, 80))

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (30, 30))


# Начальные координаты машины
car_x = WIDTH // 2 - 25  # центр по горизонтали
car_y = HEIGHT - 120     # ближе к нижней части экрана
car_speed = 5

# Параметры монет
coin_list = []           # список всех монет на экране
coin_speed = 5
coin_size = 32           # размер картинки монеты
score = 0                # счётчик собранных монет

# Функция для создания новой монеты
def create_coin():
    x = random.randint(20, WIDTH - coin_size - 20)
    y = random.randint(-150, -50)
    return [x, y]

# Основной игровой цикл
running = True
while running:
    screen.blit(road, (0, 0))  # рисуем фон дороги

    # Проверка событий (нажатие на крестик)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_d] and car_x < WIDTH - car.get_width():
        car_x += car_speed

    # Отображаем машину игрока
    screen.blit(car, (car_x, car_y))
    



    # Появление новых монет (с вероятностью ~3%)
    if random.randint(1, 100) <= 3:
        coin_list.append(create_coin())
        

    # Работа со всеми монетами
    for coin_pos in coin_list[:]:  # копируем список, чтобы безопасно удалять
        coin_pos[1] += coin_speed  # монета двигается вниз

        # Проверка столкновения машины с монетой
        if (
            car_x < coin_pos[0] + coin_size and
            car_x + car.get_width() > coin_pos[0] and
            car_y < coin_pos[1] + coin_size and
            car_y + car.get_height() > coin_pos[1]
        ):
            coin_list.remove(coin_pos)  # убираем монету
            score += 1                  # увеличиваем счёт

        # Удаляем монеты, которые вышли за нижнюю границу
        elif coin_pos[1] > HEIGHT:
            coin_list.remove(coin_pos)

        # Рисуем монету
        screen.blit(coin, (coin_pos[0], coin_pos[1]))

    # Выводим счёт (в правом верхнем углу)
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render("Coins: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 120, 10))

    # Обновление экрана

    pygame.display.update()
    clock.tick(60)

# Выход из игры
pygame.quit()
