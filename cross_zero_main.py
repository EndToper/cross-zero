import pygame
import random
import os

pygame.init()

pygame.display.set_caption("EndToper's cross-zero")
WHITE = (255,255,255)
BLACK = (0,0,0)
#рассчет отнасительных координат 2
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WIDTH, HEIGHT = width, height
width, height = round(width/2), round(height/2)
#рассчет отнасительных координат 2
stroks,stolbs = WIDTH // 90, HEIGHT // 90
ostatok_w, ostatok_h = round((width % 90)), round((height % 90))
width - ostatok_w, height - ostatok_h
#задача переменных. FPS = fragmet per second, mode - screen mode, run - game circle, clock - for FPS,layer - who's gonna to go, wins - list with lists with win combinations
FPS = 60
mode = 'first'
run = True
game_run = 0
clock = pygame.time.Clock()
player = 1
wins = None
#картинки
image_adress = os.path.join('cross_zero_images','circle1.png')
circle_image = pygame.image.load(image_adress)

image_adress_2 = os.path.join('cross_zero_images','cross.png')
cross_image = pygame.image.load(image_adress_2)
#проверка работа сиситем
print(width, height)
print(stroks,stolbs)
print(ostatok_w, ostatok_h)
print(width - ostatok_w, height - ostatok_h )
print(wins)
screen = pygame.display.set_mode((width - ostatok_w, height - ostatok_h))


class sq(pygame.sprite.Sprite):
    def __init__(self,x,y,color,x2,y2,ctype):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.pos = (x2,y2)
        self.color = color
        self.image.fill(color)
        self.image_image = self.image
        self.type = ctype
    def update(self,pos):
        global player,poses, game_run
        if player == 1 and self.type == 0:
            self.image_image = circle_image
            player = 2
            self.type = 1
            poses[(pos)] = 1
        if player == 2 and self.type == 0:
            self.image_image = cross_image
            player = 1
            self.type = 2
            poses[(pos)] = 2
        win_score = 0
        x = pos[0]
        y = pos[1]
        wins = [[(x+1,y),(x+2,y),(x+3,y),(x+4,y)],[(x-1,y),(x-2,y),(x-3,y),(x-4,y)],[(x,y+1),(x,y+2),(x,y+3),(x,y+4)],[(x,y-1),(x,y-2),(x,y-3),(x,y-4)],[(x-1,y-1),(x-2,y-2),(x-3,y-3),(x-4,y-4)],[(x+1,y+1),(x+2,y+2),(x+3,y+3),(x+4,y+4)],[(x-1,y+1),(x-2,y+2),(x-3,y+3),(x-4,y+4)],[(x+1,y-1),(x+2,y-2),(x+3,y-3),(x+4,y-4)]]
        #проверка победы кругов
        if self.type == 1:
            for i in range(len(wins)):
                for j in range(len(wins[i])):
                    if wins[i][j][0] > 0 and wins[i][j][1] > 0 and wins[i][j][0] < stroks and wins[i][j][1] < stolbs:
                        if poses[wins[i][j]] == 1:
                            win_score = win_score + 1
                if win_score >= 4:
                    if mode == 'first':
                        width, height = round(WIDTH/2), round(HEIGHT/2)
                        pygame.display.set_mode((width - ostatok_w, height - ostatok_h ))
                        game_run = 1
                    if mode == 'second':
                        pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
                        game_run = 3
                    win_score = 0
                if i == 1 or i == 3 or i == 5 or i == 7:
                    win_score = 0
            win_score = 0
        #проверка победы крестов
        if self.type == 2:
            for i in range(len(wins)):
                for j in range(len(wins[i])):
                    if wins[i][j][0] > 0 and wins[i][j][1] > 0 and wins[i][j][0] < stroks and wins[i][j][1] < stolbs:
                        if poses[wins[i][j]] == 2:
                            win_score = win_score + 1
                if win_score >= 4:
                    if mode == 'first':
                        width, height = round(WIDTH/2), round(HEIGHT/2)
                        pygame.display.set_mode((width - ostatok_w, height - ostatok_h ))
                        game_run = 2
                    if mode == 'second':
                        pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
                        game_run = 4
                    win_score = 0
                if i == 1 or i == 3 or i == 5 or i == 7:
                    win_score = 0
            win_score = 0
    def draw(self):
        screen.blit(self.image_image,(self.pos))
    def reset(self):
        self.image_image = self.image
        self.type = 0
        

all_sprites = pygame.sprite.Group()
squares = []
poses = {}
poses_mass = []
qw = 0
qw2 = 0
qw3 = 1
for i in range(1,stroks*stolbs+1):
    x = 45+90*qw2
    y = 45+90*qw
    x2 = 5+90*qw2
    y2 = 5+90*qw
    qw = qw + 1
    if qw == stolbs:
        qw = 0
        qw2 = qw2 + 1
        qw3 = qw3 + 1
    color = WHITE
    q = sq(x,y,color,x2,y2,0)
    all_sprites.add(q)
    squares.append(q)
    poses_mass.append((qw3,qw))
    poses[(qw3,qw)] = 0






while run:
    screen.fill(BLACK)
    clock.tick(FPS)
    for i2 in range(len(squares)):
        squares[i2].draw()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False
            elif i.key == pygame.K_F5 and mode == 'first' and game_run == 0:
                pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
                mode =  'second'
                pygame.display.update()
            elif i.key == pygame.K_F5 and mode == 'second' and game_run == 0:
                width, height = round(WIDTH/2), round(HEIGHT/2)
                pygame.display.set_mode((width - ostatok_w, height - ostatok_h ))
                mode =  'first'
                pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if game_run == 0:
                for i2 in range(len(squares)):
                    if squares[i2].rect.collidepoint(pygame.mouse.get_pos()) and i.button == 1 or squares[i2].rect.collidepoint(pygame.mouse.get_pos()) and i.button == 3:
                        squares[i2].update(poses_mass[i2])
            else:
                for i2 in range(len(squares)):
                    squares[i2].reset()
                    game_run = 0
                for i in poses.keys():
                    poses[i] = 0
    if game_run == 1:
        screen.fill(WHITE)
        fontObj = pygame.font.Font('freesansbold.ttf', 25)
        textSurfaceObj = fontObj.render(f'Выйграли Нолики', False, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (width/2,height/2)
        screen.blit(textSurfaceObj, textRectObj)
    if game_run == 2:
        screen.fill(WHITE)
        fontObj = pygame.font.Font('freesansbold.ttf', 25)
        textSurfaceObj = fontObj.render(f'Выйграли Крестики', False, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (width/2,height/2)
        screen.blit(textSurfaceObj, textRectObj)
    if game_run == 3:
        screen.fill(WHITE)
        fontObj = pygame.font.Font('freesansbold.ttf', 100)
        textSurfaceObj = fontObj.render(f'Выйграли Нолики', False, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH/2,HEIGHT/2)
        screen.blit(textSurfaceObj, textRectObj)
    if game_run == 4:
        screen.fill(WHITE)
        fontObj = pygame.font.Font('freesansbold.ttf', 100)
        textSurfaceObj = fontObj.render(f'Выйграли Крестики', False, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WIDTH/2,HEIGHT/2)
        screen.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()


pygame.quit()