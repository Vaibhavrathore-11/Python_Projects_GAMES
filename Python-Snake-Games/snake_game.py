import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake position
Snake_x = 400
Snake_y = 300

# Snake body
snake_body = [
    (400, 300)
]

# Movement speed
speed = 20

# Snake direction
direction = "RIGHT"

# Snake growth
grow = False

# Score
Score = 0

# Food position
food_x = random.randrange(0, WIDTH, 20)
food_y = random.randrange(0, HEIGHT, 20)

# Game Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)

running = True
game_over = False

def restart_game():
    global Snake_x, Snake_y
    global snake_body
    global direction
    global grow
    global Score
    global food_x, food_y
    global game_over

    Snake_x = 400
    Snake_y = 300

    snake_body = [(400, 300)]

    direction = "RIGHT"

    grow = False

    Score = 0

    food_x = random.randrange(0, WIDTH, 20)
    food_y = random.randrange(0, HEIGHT, 20)

    game_over = False


while running:

    # Events check karo
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

            elif event.key == pygame.K_UP:
                direction = "UP"

            elif event.key == pygame.K_DOWN:
                direction = "DOWN"

            elif event.key == pygame.K_r and game_over:
                 restart_game()    

    # STEP 3 - Snake movement
    if not game_over:

        # Snake movement
        if direction == "LEFT":
            Snake_x -= speed

        elif direction == "RIGHT":
            Snake_x += speed

        elif direction == "UP":
            Snake_y -= speed

        elif direction == "DOWN":
            Snake_y += speed

        # Wall collision
        if Snake_x < 0:
            Snake_x = 0
            game_over = True

        elif Snake_x + 20 > WIDTH:
            Snake_x = WIDTH - 20
            game_over = True

        elif Snake_y < 0:
            Snake_y = 0
            game_over = True

        elif Snake_y + 20 > HEIGHT:
            Snake_y = HEIGHT - 20
            game_over = True

        # Food collision
        if Snake_x == food_x and Snake_y == food_y:

            print("Food eaten!")

            food_x = random.randrange(0, WIDTH, 20)
            food_y = random.randrange(0, HEIGHT, 20)

            grow = True
            Score += 1

        # Add new head position
        snake_body.insert(0, (Snake_x, Snake_y))

        # Self collision
        if (Snake_x, Snake_y)in snake_body[1:]:
            game_over = True

        # Snake growth
        if grow:
            grow = False

        else:
            snake_body.pop()

    # STEP 4 - Background
    screen.fill((0, 0, 0))

    # Snake - Green
    for x, y in snake_body:

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (x, y, 20, 20)
        )

    # Food - Red
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (food_x, food_y, 20, 20)
    )

    # Score
    score_text = font.render(
        f"Score: {Score}",
        True,
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    # GAME OVER
    if game_over:

        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            (255, 255, 255)
        )

        screen.blit(
            game_over_text,
            (WIDTH // 2 - 150, HEIGHT // 2 - 50)
        )

        # Final Score
        final_score_text = font.render(
            f"Final Score: {Score}",
            True,
            (255, 255, 255)
        )

        screen.blit(
         final_score_text,
         (WIDTH // 2 - 90, HEIGHT // 2)
       )    

        restart_text = font.render(
            "Press R to restart",
            True,
            (255, 255, 255)

        )

        screen.blit(
            restart_text,
            (WIDTH // 2 - 120, HEIGHT // 2 + 30)
        )

    # Update screen
    
    pygame.display.update()

    # Game speed
    clock.tick(10)

pygame.quit()