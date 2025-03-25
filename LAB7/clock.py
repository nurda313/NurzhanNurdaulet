import pygame
import sys
from datetime import datetime


pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Mickey Clock")


clock_face = pygame.image.load("mickey_clock.png")
clock_face = pygame.transform.scale(clock_face, (800, 600))

left_hand = pygame.image.load("left_hand.png")
left_hand = pygame.transform.scale(left_hand, (500, 700))

right_hand = pygame.image.load("right_hand.png")
right_hand = pygame.transform.scale(right_hand, (500, 700))

center_x = width // 2
center_y = height // 2

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = -seconds * 6
    min_angle = -minutes * 6

    rotated_sec = pygame.transform.rotate(left_hand, sec_angle)
    rotated_min = pygame.transform.rotate(right_hand, min_angle)

    sec_rect = rotated_sec.get_rect(center = (center_x, center_y))
    min_rect = rotated_min.get_rect(center = (center_x, center_y))

    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    screen.blit(rotated_min, min_rect)
    screen.blit(rotated_sec, sec_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()