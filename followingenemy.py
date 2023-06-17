#essentially a snake
import os.path

import pygame

class Snake(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.length = 1
        self.size = 25
        self.body = [(x,y)]
        self.head_img = img

    def get_head(self):
        return (self.x, self.y)

    def get_length(self):
        return self.length

    def move(self, x,y,speed):
        dx = x*speed
        sy = y*speed

        self.body.append((self.x, self.y))
        if len(self.body)>self.length:
            del self.body[0]

    def draw(self, game_display, direction, color):
        head = self.head_img
        if direction == 'right':
            head = pygame.transform.rotate(self.head_img, 270)
        if direction == 'left':
            head = pygame.transform.rotate(self.head_img, 90)
        if direction == 'down':
            head = pygame.transform.rotate(self.head_img, 180)

        game_display.blit(head, (self.body[-1][0], self.body[-1][1]))

        for part in self.body[:-1]:
            pygame.draw.rect(game_display,color,(part[0],part[1], self.size,self.size))

    def increment_length(self):

        self.length += 1

head_path = os.path.join('Assets', 'Images', 'head.png')
img = pygame.image.load(head_path)
snake = Snake(2000,200, img)
width, height = 600,600
game_display = pygame.display.set_mode((width,height))
dirn = 'right'
clock = pygame.time.Clock()
#font = pygame.font.SysFont('comicsansms', 35)
FPS  = 25
snake.draw(game_display, dirn, (0,155,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_display.fill('white')
    snake.draw(game_display, dirn, (0, 155, 0))
    pygame.display.flip()


pygame.quit()




