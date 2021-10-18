import pygame
from pygame.draw import *
import random
from random import *
import json

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:

	def __init__(self, screen, color = (0, 0, 255)):
		self.coord = [randint(100, 1100), randint(100, 700)]
		self.color = color
		self.velocity = [randint(-7, 7), randint(-7, 7)]
		self.r = randint(20, 40)
		self.flag = True

	def appear(self, screen):
		circle(screen, self.color, self.coord, self.r)
	
	def move(self):
		self.coord[0] += self.velocity[0]
		self.coord[1] += self.velocity[1]

	def event(self, event_pos_x, event_pos_y):
		x0, y0 = self.coord
		pos_x, pos_y = event_pos_x, event_pos_y
		if x0 - self.r <= pos_x <= x0 + self.r and y0 - self.r <= pos_y <= y0 + self.r:
			return True
	
	def collision(self):
		x0, y0 = self.coord
		if 0 >= x0 - self.r or x0 + self.r >= 1200:
			self.velocity[0] *= -1
		elif 0 >= y0 - self.r or y0 + self.r >= 800:
			self.velocity[1] *= -1

class Square:

	def __init__(self, screen, color = (255, 0, 0)):
		self.coord = [randint(100, 1100), randint(100, 700)]
		self.color = color
		self.r = randint(20, 40)
		self.velocity = [randint(-10, 10), randint(-10, 10)]

	def appear(self, screen):
		rect(screen, self.color, (self.coord[0] - self.r, self.coord[1] - self.r, 2 * self.r, 2 * self.r))
	
	def move(self):
		self.coord[0] += self.velocity[0]
		self.coord[1] += self.velocity[1]

	def event(self, event_pos_x, event_pos_y):
		x0, y0 = self.coord
		pos_x, pos_y = event_pos_x, event_pos_y
		if x0 - self.r <= pos_x <= x0 + self.r and y0 - self.r <= pos_y <= y0 + self.r:
			return True
	
	def collision(self):
		x0, y0 = self.coord
		if 0 >= x0 - self.r or x0 + self.r >= 1200:
			self.velocity[0] *= -1
		elif 0 >= y0 - self.r or y0 + self.r >= 800:
			self.velocity[1] *= -1

balls = []

rects = []

counted = 0

name = input()

FPS = 30
screen = pygame.display.set_mode((1200, 800))

pygame.font.init()
score = 0 
text = pygame.font.SysFont('arial', 20)
text1 = text.render('Счёт:' + str(score), False, (0, 0, 0))

pygame.display.update()
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
finished = False
num = 0


while not finished and num <= 500:
    
    clock.tick(FPS)
    num += 1
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            finished = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
        	for ball in balls:
        		if ball.event(event.pos[0], event.pos[1]):
        			balls.pop(balls.index(ball))
        			balls.append(Ball(screen))
        			score += 1
        			break
        	for square in rects:
        		if square.event(event.pos[0], event.pos[1]):
        			rects.pop(rects.index(square))
        			rects.append(Square(screen))
        			score -= 1
        			break
        
        elif event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_ESCAPE:
        		finished = True

    if num % 40 == 0:
    	if num >= 200:
    		balls.pop(0)
    	ball = Ball(screen)
    	balls.append(ball)
    elif num % 40 == 20:
    	if num >= 220:
    		rects.pop(0)
    	square = Square(screen)
    	rects.append(square)
    
    for square in rects:
    	square.collision()
    	square.move()
    	square.appear(screen)

    for ball in balls:
    	ball.collision()
    	ball.move()
    	ball.appear(screen)
    	text1 = text.render('Счёт:' + str(score), False, (0, 0, 0))
    	screen.blit(text1, (0, 200))
    
    pygame.display.update()
    screen.fill((255, 255, 255))

with open("Results.json", 'r') as f:
	loaded = json.load(f)

loaded['results'].append({'name': name, 'result': score})

loaded['games_played'] += 1

with open("Results.json", 'w') as f:
	json.dump(loaded, f)

pygame.quit()