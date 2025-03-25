import pygame
import os

pygame.init()
pygame.mixer.init()

# Creating window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# List of track
tracks = ["touch_the_sky.mp3", "not_like_us.mp3", "adidas.mp3"]
current_track = 0

# Function for playing music
def play_track(index):
    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()

play_track(current_track)

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

            elif event.key == pygame.K_RIGHT:  # Next track
                current_track = (current_track + 1) % len(tracks)
                play_track(current_track)
                paused = False

            elif event.key == pygame.K_LEFT:  # Previous track
                current_track = (current_track - 1) % len(tracks)
                play_track(current_track)
                paused = False

            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                paused = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
