import pygame
import requests
import json


pink = '#223322'
white = '#ffffff'
red = '#ffd00f'
black = '#000000'
yellow = '#ffff00'
orange = '#ff9900'
pygame.init()
screen = pygame.display.set_mode([303,350])
pygame.display.set_caption('Pathforia')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(pink)
pygame.font.Font('freesansbold.ttf', 24)
all_sprites = pygame.sprite.Group()
commonVar = 50
thicc = 5
otheCommonVar = 43


data = {"model": "default"}
response = requests.post("http://colormind.io/api/", data=json.dumps(data))
palette = response.json()['result']
colorlist = []
c1 = ''
c2 = ''
colorlist.append(c1)
colorlist.append(c2)
for i in range(2):
    hexstring = '#'
    for y in range(3):
        hexstring+=f'{palette[i][y]:02x}'
    colorlist[i] = hexstring

wordsIKnow = {'poop':'poop', 'frog':'frog'}


verticalWallLength = [400,50,300,150,130,97,200]
horizontalWallLength = [100,75,89,150,100,150,100]
cornerLengths = [300,100,69,45,500,56,200,34]
topFauxPathsLengths = [69,400,50,89,69,300,200]
bottomFauxPathsLengths = [85,69,69,50,200,69,100]


class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x
        self.speed = 3
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
    def get_position(self):
        return (self.rect.x, self.rect.y)


def endPoint(x,y):
    global position
    end = Wall(x,y-50, 50,50,red)
    all_sprites.add(end)

def restart():
    print('restart')
def verticalPairedWalls(x,y,w,h,c):
    global all_sprites, commonVar, positionx, positiony
    vwall = Wall(x,y,w,h,c)
    vpair = Wall(x+commonVar,y-commonVar,w,h,c)
    all_sprites.add(vwall)
    all_sprites.add(vpair)
    positionx = x
    positiony = y

def horizontalPairedWalls(x,y,w,h,c):
    global all_sprites, commonVar, positionx
    hwall = Wall(x, y, w, h, c)
    hpair = Wall(x+commonVar, y-commonVar, w, h, c)
    all_sprites.add(hwall)
    all_sprites.add(hpair)
    positionx = x+w

positionx = 0
positiony = 0
def dropACorner(x,y,g):
    global positiony, positionx
    fixingit = Wall(x,y+1,commonVar*2,thicc,white)
    vcorner = Wall(x+commonVar,y-otheCommonVar-g,thicc,g,white)
    vcornerPair = Wall(x+(commonVar*2),y-g+thicc+1,thicc,g,white)
    moreFixing = Wall(x+commonVar,y-otheCommonVar-g,commonVar*2,thicc,white)
    all_sprites.add(fixingit)
    all_sprites.add(vcorner)
    all_sprites.add(vcornerPair)
    all_sprites.add(moreFixing)
    positiony = y-otheCommonVar+commonVar-g
    positionx = x+commonVar*2
    horizontalPairedWalls(positionx, positiony, g+commonVar-1, thicc, white)
    positiony = y - otheCommonVar + commonVar - g
    positionx = x + (commonVar*2) + g + otheCommonVar

def fauxTopPath(x,y,l):
    global positionx, positiony
    equalVWall = Wall(x+(commonVar),y-l-commonVar,thicc,l+5,white)
    secondEqualVWall = Wall(x+(commonVar*2),y-l-commonVar,thicc,l+5,white)
    bottomTopPart = Wall(x-(l-commonVar),y-commonVar-l,l,thicc,white)
    secondBottomTopPart = Wall(x+commonVar+commonVar, y-commonVar-l, l,thicc, white)
    topPartConnector = Wall(x-l+(commonVar),y-l-(commonVar*2),thicc,commonVar,white)
    secondTopPartConnector = Wall(x+l+(commonVar*2),y-l-(commonVar*2),thicc,commonVar+5,white)
    topTopPart = Wall(x-(l-commonVar),y-(commonVar*2)-l,(l*2)+commonVar,thicc,white)
    lastfix = Wall(x,y-commonVar,commonVar,thicc,white)
    probLastFix = Wall(positionx+commonVar+commonVar,positiony-commonVar,l+commonVar,thicc,white)
    sikeFix = Wall(positionx-commonVar,positiony,l+(commonVar*3),thicc,white)
    all_sprites.add(equalVWall)
    all_sprites.add(secondEqualVWall)
    all_sprites.add(bottomTopPart)
    all_sprites.add(secondBottomTopPart)
    all_sprites.add(topPartConnector)
    all_sprites.add(secondTopPartConnector)
    all_sprites.add(topTopPart)
    all_sprites.add(lastfix)
    all_sprites.add(probLastFix)
    all_sprites.add(sikeFix)
    positionx = x + l


def fauxBottomPath(x,y,l):
    global positiony, positionx
    equalVWall = Wall(x+ commonVar, y, thicc, l, white)
    secondEqualVWall = Wall(x + (commonVar * 2), y, thicc, l, white)
    bottomTopPart = Wall(x -(l-commonVar), y+l, l+5, thicc, white)
    secondBottomTopPart = Wall(x + (commonVar * 2), y+l, l, thicc, white)
    topPartConnector = Wall(x - (l-commonVar), y+l, thicc, commonVar, white)
    secondTopPartConnector = Wall(x + l+(commonVar*2), y+l, thicc, commonVar, white)
    topTopPart = Wall(x - (l-commonVar), y+l+commonVar, (l * 2) + commonVar+5, thicc, white)
    fixing = Wall(x, y, commonVar, thicc, white)
    probLastFix = Wall(x+(commonVar),y-commonVar,commonVar*3,thicc,white)
    all_sprites.add(equalVWall)
    all_sprites.add(secondEqualVWall)
    all_sprites.add(bottomTopPart)
    all_sprites.add(secondBottomTopPart)
    all_sprites.add(topPartConnector)
    all_sprites.add(secondTopPartConnector)
    all_sprites.add(topTopPart)
    all_sprites.add(fixing)
    all_sprites.add(probLastFix)
    positionx = x + (commonVar*2)


def ghost(x,y):
    pygame.draw.circle(screen, white, (x, y), 20)
    pygame.draw.circle(screen, pink, (x-8, y-10), 4)
    pygame.draw.circle(screen, pink, (x+8, y-10), 4)
    pygame.draw.rect(screen,white,pygame.Rect(x-20,y,40,35))
    pygame.draw.polygon(screen, pink, ((x+5, y), (x, y-5), (x-5, y)))
    pygame.draw.polygon(screen, pink, ((x-10, y+30), (x-5, y+40), (x-15, y+40)))
    pygame.draw.polygon(screen, pink, ((x, y+30), (x+5, y+40), (x-5, y+40)))
    pygame.draw.polygon(screen, pink, ((x+10, y+30), (x+15, y+40), (x+5, y+40)))
    pygame.draw.polygon(screen, pink, ((x+20, y+30), (x+25, y+40), (x+15, y+40)))



class Player():
    def __init__(self,x,y):
        self.rect = ghost(x,y)


y = 0
l = 5
global position

for i in range(7):
    w = h2 = thicc
    h = verticalWallLength[i]
    verticalPairedWalls(positionx,positiony,w,h,white)
    positiony+=h
    w2 = horizontalWallLength[i]
    horizontalPairedWalls(positionx,positiony,w2,h2,white)
    fauxTopPath(positionx, positiony, topFauxPathsLengths[i])
    horizontalPairedWalls(positionx,positiony,w2,h2,white)
    fauxBottomPath(positionx, positiony, bottomFauxPathsLengths[i])
    horizontalPairedWalls(positionx,positiony,w2,h2,white)
    positiony -= 1
    dropACorner(positionx, positiony, cornerLengths[i])
endPoint(positionx,positiony)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(pink)
    all_sprites.draw(screen)
    if y!=212:
        y+=0.5
        l+=10
        pygame.draw.rect(screen, colorlist[0], pygame.Rect(180, y - l, 40, l))
        pygame.draw.rect(screen, colorlist[1], pygame.Rect(200, y - l, 20, l))
    trial = Player(200,y)

    pygame.display.flip()





pygame.quit()



