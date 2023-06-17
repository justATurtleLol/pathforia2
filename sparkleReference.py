import pygame
import random

# Window size
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)
RAINBOW_COLORS = ['#ffa00f','#fa0aaf','#f005f0']

# Block properties
BLOCK_SIZE = 27

# Sparkle properties
SPARKLE_SIZE = 9
SPARKLE_LIFETIME = 15 # Frames

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed = 12


    def update(self):
        keys = pygame.key.get_pressed()
        for dx, dy, key_combinations in [(-self.speed, 0, [pygame.K_a, pygame.K_LEFT]),
                                         (self.speed, 0, [pygame.K_d, pygame.K_RIGHT]),
                                         (0, -self.speed, [pygame.K_w, pygame.K_UP]),
                                         (0, self.speed, [pygame.K_s, pygame.K_DOWN])]:
            if any(keys[key] for key in key_combinations):
                self.rect.x += dx
                self.rect.y += dy
                self.rect.x = max(0, min(WIDTH - BLOCK_SIZE, self.rect.x))
                self.rect.y = max(0, min(HEIGHT - BLOCK_SIZE, self.rect.y))
                sparkles.add(Sparkle(self.rect.x, self.rect.y))


# Sparkle class
class Sparkle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SPARKLE_SIZE, SPARKLE_SIZE))
        self.image.fill(random.choice(RAINBOW_COLORS))
        self.rect = self.image.get_rect()
        self.rect.x = x + BLOCK_SIZE / 2
        self.rect.y = y + BLOCK_SIZE / 2
        self.lifetime = SPARKLE_LIFETIME

    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


sparkles = pygame.sprite.Group()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    sparkles.update()


    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    sparkles.draw(screen)

    # Flip the display
    pygame.display.flip()

pygame.quit()
