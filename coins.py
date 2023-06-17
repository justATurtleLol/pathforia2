import pygame
screen = pygame.display.set_mode([606,425])
black = '#000000'
yellow = '#ffff00'
orange = '#ff9900'
white = '#ffffff'
pygame.init()

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.draw.circle(screen, orange, (x, y), 20)
        pygame.draw.circle(screen, yellow, (x + 5, y), 20)
        pygame.draw.circle(screen, orange, (x + 5, y), 10)
        pygame.draw.circle(screen, yellow, (x, y), 7)
        self.x = x
        self.y = y
        self.speed = 3


    def get_position(self):
        return (self.x, self.y)


x = 200
y = 200

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    trial = Coin(x, y)
    if keys[pygame.K_a]:
        trial.x += trial.speed
    if keys[pygame.K_d]:
        trial.x -= trial.speed
    if keys[pygame.K_w]:  # Move up
        trial.y += trial.speed
    if keys[pygame.K_s]:  # Move down
        trial.y -= trial.speed


    pygame.display.flip()


pygame.quit()
