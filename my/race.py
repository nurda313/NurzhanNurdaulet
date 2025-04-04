import pygame
import random

# Инициализируем Pygame
pygame.init()
pygame.mixer.init()

# Размеры окна
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Shashki")

# Установка FPS
clock = pygame.time.Clock()

# Загрузка изображений
road = pygame.image.load("road.png")           # фон дороги
car = pygame.image.load("car.png")             # машина игрока
car = pygame.transform.scale(car, (33, 65))    

enemy = pygame.image.load("enemy.png")         # враг
enemy = pygame.transform.scale(enemy, (30, 60))


coin = pygame.image.load("coin.png")     # монеты
coin = pygame.transform.scale(coin, (30, 30))

# Звук при столкновении
crash_sound = pygame.mixer.Sound("crash.wav")

# Фоновая музыка
# pygame.mixer.music.load("not_like_us.mp3")
# pygame.mixer.music.play(-1)

# Начальные координаты машины
car_x = WIDTH // 2 - 25
car_y = HEIGHT - 120
car_speed = 5

# Параметры врагов
enemy_list = []
enemy_speed = 5



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

def create_enemy():
    x = random.randint(0, WIDTH - enemy.get_width())
    y = random.randint(-150, -80)
    return [x, y]

bg_y = 0

# Основной игровой цикл
running = True
while running:
    screen.blit(road, (0, 0))  # фон
    screen.blit(road, (0, bg_y))
    screen.blit(road, (0, bg_y - 600))

    bg_y += 2
    if bg_y == 600:
        bg_y = 0

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_d] and car_x < WIDTH - car.get_width():
        car_x += car_speed

    # Отображение машины игрока
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

    font = pygame.font.SysFont("Arial", 24)
    street_text = font.render("Al-Farabi " , True, (255, 255, 255))
    text_rect = street_text.get_rect(center=(WIDTH // 2, 10 + street_text.get_height() // 2))
    screen.blit(street_text, text_rect)
 

    # Создание новых врагов
    if random.randint(1, 100) <= 2:
        enemy_list.append(create_enemy())

    # Работа с врагами
    for enemy_pos in enemy_list[:]:
        enemy_pos[1] += enemy_speed

        # Столкновение
        if (
            car_x < enemy_pos[0] + enemy.get_width() and
            car_x + car.get_width() > enemy_pos[0] and
            car_y < enemy_pos[1] + enemy.get_height() and
            car_y + car.get_height() > enemy_pos[1]
        ):
            pygame.mixer.music.stop()
            crash_sound.play()
            pygame.time.delay(1000)
            running = False

        elif enemy_pos[1] > HEIGHT:
            enemy_list.remove(enemy_pos)

        # Отображаем врага
        screen.blit(enemy, (enemy_pos[0], enemy_pos[1]))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
