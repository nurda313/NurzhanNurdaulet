import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600, 360))
pygame.display.set_caption("My Pygame") 
icon = pygame.image.load("myicon.png")
pygame.display.set_icon(icon)



background = pygame.image.load("background.jpg")
player1l = pygame.image.load("ball1l.png")
player1l = pygame.transform.scale(player1l, (50, 50))
player2l = pygame.image.load("ball2l.png")
player2l = pygame.transform.scale(player2l, (50, 50))
player3l = pygame.image.load("ball3l.png")
player3l= pygame.transform.scale(player3l, (50, 50))


player1r = pygame.image.load("ball1r.png")
player1r = pygame.transform.scale(player1r, (50, 50))
player2r = pygame.image.load("ball2r.png")
player2r = pygame.transform.scale(player2r, (50, 50))
player3r = pygame.image.load("ball3r.png")
player3r = pygame.transform.scale(player3r, (50, 50))

walk_left = [
    player1l, player2l, player3l
]

walk_right = [
    player1r, player2r, player3r
]

player_anim_count = 0

bg_x = 0
# bg_sound = pygame.mixer.Sound("not_like_us.mp3")
# bg_sound.play()


player_speed = 5 
player_x = 150
player_y = 250

is_jump = False
jump_count = 7


running = True
while running:

    

    screen.fill((255, 255, 255))
     
     
    
    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 600, 0))
    screen.blit(walk_right[player_anim_count], (player_x, 220))

    

    keys = pygame.key.get_pressed()
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
   
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y = player_y - (jump_count ** 2) / 2
            else:
                player_y = player_y + (jump_count ** 2) / 2
            jump_count = jump_count - 1
        else:
            is_jump = False
            jump_count = 7

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, 220))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, 220))
    
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x = player_x - player_speed
    elif keys[pygame.K_RIGHT] and player_x < 600:
        player_x = player_x + player_speed

   
   

    if player_anim_count == 2:
        player_anim_count = 0
    else:
        player_anim_count = player_anim_count + 1

     
    bg_x -= 2
    if bg_x == -600:
        bg_x = 0
    

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



    clock.tick(20)
     
   

      