import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle with User Input")
WHITE = (255, 255, 255)
BLUE = (0, 102, 255)


x, y = WIDTH // 2, HEIGHT // 2 
radius = 50
speed_x, speed_y = 3, 2 

clock = pygame.time.Clock()

print("Controls:")
print("Arrow Keys: Move circle")
print("W/S: Increase/Decrease radius")
print("Q: Quit")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_w]:
        radius += 2
    if keys[pygame.K_s] and radius > 5:
        radius -= 2
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    x += speed_x
    y += speed_y

    if x - radius <= 0 or x + radius >= WIDTH:
        speed_x = -speed_x
    if y - radius <= 0 or y + radius >= HEIGHT:
        speed_y = -speed_y

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
