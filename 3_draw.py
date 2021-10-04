import pygame

pygame.init()

FPS = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
screen.fill((85, 68, 0))
pygame.draw.rect(screen, (128, 102, 0), pygame.Rect(0, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT / 2))
BLU = (0, 0, 255)
ORANG = (200, 113, 55)
BLAC = (0, 0, 0)
GREE = (0, 255, 0)
PINK = (222, 170, 135)
LIGHT_BLUE = (135, 205, 222)

def eye(x, y, scale):
    pygame.draw.ellipse(screen, GREE, pygame.Rect(x - 20 * scale, y - 20 * scale, 40 * scale, 40 * scale))
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x + 10 * scale, y - 16 * scale, 5 * scale, 32 * scale))

def ear(x, y, scale, color):
    pygame.draw.polygon(screen, color, [(x, y), (x + 20 * scale, y + 50 * scale), (x - 20 * scale, y + 50 * scale)])
    pygame.draw.polygon(screen, BLAC, [(x, y), (x + 20 * scale, y + 50 * scale), (x - 20 * scale, y + 50 * scale)], width = 1)
    pygame.draw.polygon(screen, PINK, [(x, y + 10 * scale), (x + 10 * scale, y + 40 * scale), (x - 10 * scale, y + 40 * scale)])
def cat(x_center, y_center, scale, color):
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center + 150 * scale, y_center - 40 * scale, 200 * scale, 80 * scale))  #хвост
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center + 150 * scale, y_center - 40 * scale, 200 * scale, 80 * scale), width = 1)
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center - 200 * scale, y_center - 100 * scale, 400 * scale, 200 * scale))  #туловище
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center - 200 * scale, y_center - 100 * scale, 400 * scale, 200 * scale), width = 1)
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center - 220 * scale, y_center, 40 * scale , 80 * scale))  #лапка
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center - 220 * scale, y_center, 40 * scale , 80 * scale), width = 1)
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center - 250 * scale, y_center - 100 * scale, 160 * scale, 160 * scale))  #голова
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center - 250 * scale, y_center - 100 * scale, 160 * scale, 160 * scale), width = 1)
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center + 80 * scale, y_center, 120 * scale, 120 * scale))  #ЛАПА
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center + 80 * scale, y_center, 120 * scale, 120 * scale), width = 1)
    pygame.draw.ellipse(screen, color, pygame.Rect(x_center + 180 * scale, y_center + 60 * scale, 40 * scale, 120 * scale))
    pygame.draw.ellipse(screen, BLAC, pygame.Rect(x_center + 180 * scale, y_center + 60 * scale, 40 * scale, 120 * scale), width = 1)
    eye(x_center - 210 * scale, y_center - 20 * scale, scale)
    eye(x_center - 130 * scale, y_center - 20 * scale, scale)
    ear(x_center - 210 * scale, y_center - 120 * scale, scale, color)
    ear(x_center - 130 * scale, y_center - 120 * scale, scale, color)
    
def window(x, y, scale):
    pygame.draw.rect(screen, (213, 255, 230), (x, y, 200 * scale, 300 * scale))
    pygame.draw.rect(screen, LIGHT_BLUE, (x + 20 * scale, y + 20 * scale, 70 * scale, 80 * scale))
    pygame.draw.rect(screen, LIGHT_BLUE, (x + 110 * scale, y + 20 * scale, 70 * scale, 80 * scale))
    pygame.draw.rect(screen, LIGHT_BLUE, (x + 20 * scale, y + 110 * scale, 70 * scale, 160 * scale))
    pygame.draw.rect(screen, LIGHT_BLUE, (x + 110 * scale, y + 110 * scale, 70 * scale, 160 * scale))
    
window(500, 100, 1)
window(100, 100, 0.8)
window(300, 100, 0.9)
cat(150, 500, 0.5, ORANG)
cat(500, 450, 0.6, LIGHT_BLUE)
cat(500, 650, 0.3, BLAC)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
