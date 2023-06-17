import pygame
white = '#ffffff'
black = '#000000'
red = '#ffa00f'
pygame.init()
screen = pygame.display.set_mode([606,425])
RAINBOW_COLORS = ['#ffa00f','#fa0aaf','#f005f0']



def ghost(x,y):
    pygame.draw.circle(screen, white, (x, y), 20)
    pygame.draw.circle(screen, black, (x-8, y-10), 4)
    pygame.draw.circle(screen, black, (x+8, y-10), 4)
    pygame.draw.rect(screen,white,pygame.Rect(x-20,y,40,35))
    pygame.draw.polygon(screen, black, ((x+5, y), (x, y-5), (x-5, y)))
    pygame.draw.polygon(screen, black, ((x-10, y+30), (x-5, y+40), (x-15, y+40)))
    pygame.draw.polygon(screen, black, ((x, y+30), (x+5, y+40), (x-5, y+40)))
    pygame.draw.polygon(screen, black, ((x+10, y+30), (x+15, y+40), (x+5, y+40)))
    pygame.draw.polygon(screen, black, ((x+20, y+30), (x+25, y+40), (x+15, y+40)))



class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.rect = ghost(x,y)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x += self.speed
        if keys[pygame.K_d]:
            self.rect.x -= self.speed
        if keys[pygame.K_w]:  # Move up
            self.rect.y += self.speed
        if keys[pygame.K_s]:  # Move down
            self.rect.y -= self.speed

y = 0
l = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('black')
    if y!=400:
        y+=0.5
        l+=10
        pygame.draw.rect(screen, red, pygame.Rect(180, y - l, 40, l))
        pygame.draw.rect(screen, white, pygame.Rect(200, y - l, 20, l))
    trial = Player(200,y)


    pygame.display.flip()





pygame.quit()
