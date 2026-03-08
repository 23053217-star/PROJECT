import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Endless Runner Prototype")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Player settings
player_width, player_height = 50, 70
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Obstacle settings
obstacle_width, obstacle_height = 50, 70
obstacle_speed = 10
obstacles = []

# Font for score
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def show_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

def main():
    run = True
    score = 0
    global obstacle_speed
    player_pos = player_x

    # Timer for spawning obstacles
    obstacle_timer = 0
    obstacle_interval = 1500  # milliseconds

    while run:
        dt = clock.tick(30)  # Frame rate 30 FPS
        obstacle_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos -= player_speed
            if player_pos < 0:
                player_pos = 0
        if keys[pygame.K_RIGHT]:
            player_pos += player_speed
            if player_pos > WIDTH - player_width:
                player_pos = WIDTH - player_width

        # Spawn obstacles every interval
        if obstacle_timer > obstacle_interval:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append([obstacle_x, obstacle_y])
            obstacle_timer = 0
            # Gradually increase difficulty
            if obstacle_interval > 500:
                obstacle_interval -= 20
            obstacle_speed += 0.05

        # Move and remove obstacles
        for obstacle in obstacles[:]:
            obstacle[1] += obstacle_speed
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)
                score += 1

        # Collision detection
        player_rect = pygame.Rect(player_pos, player_y, player_width, player_height)
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
            if player_rect.colliderect(obstacle_rect):
                run = False

        screen.fill(WHITE)

        # Draw player
        draw_player(player_pos, player_y)

        # Draw obstacles
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        show_text(f"Score: {score}", 10, 10)

        pygame.display.update()

    # Game over message
    screen.fill(WHITE)
    show_text(f"Game Over! Score: {score}", WIDTH // 4, HEIGHT // 2)
    pygame.display.update()
    pygame.time.delay(3000)

if __name__ == "__main__":
    main()
    pygame.quit()
