import pygame
import random

# initialise pygame
pygame.init()

# set screen size
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# set game title
pygame.display.set_caption("Basic Game")

# set font for game
font = pygame.font.SysFont(None, 30)

# set colours
black = (0, 0, 0)
white = (255, 255, 255)

# set initial player position
player_size = 50
player_x = screen_width / 2 - player_size / 2
player_y = screen_height / 2 - player_size - 10

# set initial enemy position
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 5

# set initial score
score = 0

# define main game loop
game_over = False
while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # move player left and right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 5
            elif event.key == pygame.K_RIGHT:
                player_x += 5

    # move the enemy down the screen
    enemy_y += enemy_speed

    # check for collision
    if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
        score += 1
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0

    # check if enemy has reached bottom
    if enemy_y > screen_height:
        score -= 1
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0

    # clear the screen
    screen.fill(white)

    # draw the player and enemy
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, black, (enemy_x, enemy_y, enemy_size, enemy_size))

    # draw the score
    score_text = font.render("Score: %d" % score, True, black)
    screen.blit(score_text, (10, 10))

    # update the screen
    pygame.display.update()

# quit pygame
pygame.quit()