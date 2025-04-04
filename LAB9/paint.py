import pygame
import math

# Функция рисования фигуры
def draw_shape(screen, tool, x, y, color, radius):
    if tool == 'circle':
        pygame.draw.circle(screen, color, (x, y), radius)
    elif tool == 'rect':
        size = 2 * radius
        rect = pygame.Rect(x - radius, y - radius, size, size)
        pygame.draw.rect(screen, color, rect)
    elif tool == 'eraser':
        pygame.draw.circle(screen, (0, 0, 0), (x, y), radius)
    elif tool == 'right_triangle':
        points = [(x, y), (x, y + 2 * radius), (x + 2 * radius, y + 2 * radius)]
        pygame.draw.polygon(screen, color, points)
    elif tool == 'equilateral_triangle':
        height = int(math.sqrt(3) * radius)
        points = [(x, y - height), (x - radius, y), (x + radius, y)]
        pygame.draw.polygon(screen, color, points)
    elif tool == 'rhombus':
        points = [(x, y - radius), (x - radius, y), (x, y + radius), (x + radius, y)]
        pygame.draw.polygon(screen, color, points)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    radius = 20
    tool = 'circle'
    color = (0, 0, 255)
    drawing = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Переключение инструментов
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    tool = 'rect'
                elif event.key == pygame.K_2:
                    tool = 'circle'
                elif event.key == pygame.K_3:
                    tool = 'eraser'
                elif event.key == pygame.K_4:
                    tool = 'right_triangle'
                elif event.key == pygame.K_5:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_6:
                    tool = 'rhombus'
                elif event.key == pygame.K_r:
                    color = (255, 0, 0)
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)

            # Начало и конец рисования
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False

        if drawing:
            x, y = pygame.mouse.get_pos()
            draw_shape(screen, tool, x, y, color, radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
