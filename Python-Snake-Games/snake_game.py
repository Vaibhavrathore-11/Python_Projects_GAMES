import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake position
Snake_x = 400
Snake_y = 300


# Movement speed
speed = 20

running = True

while running:
    # Events check karo
    for event in pygame.event .get ():

      if event.type == pygame.QUIT:
            running = False

        # Keyboard input
    if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                snake_x -= speed

            if event.key == pygame.K_RIGHT:
                snake_x += speed 

            if event.key == pygame.K_UP:
                snake_y -= speed

            if event.key == pygame.K_DOWN:
                snake_y += speed

    #Background 
    screen .fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0),(Snake_x, Snake_y, 20, 20))

    pygame.display.update()

pygame.quit()