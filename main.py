import pygame
import fileseeker as fs

# programming constants

main_window_size = fs.get_window_size()
main_window_title = fs.get_window_title()

# main window attributes

pygame.init()
screen = pygame.display.set_mode(main_window_size)
pygame.display.set_caption(main_window_title)

# background
bg = pygame.image.load('assets/images/pizza.png')
bg = pygame.transform.scale(bg, main_window_size)

# players

carlos_x = 100
carlos_y = 300
carlos_delta_y = 0   #no delta x cause he will only move up and down
carlos_img = pygame.image.load('assets/images/player_55.png')

charles_x = 1000
charles_y = 300
charles_delta_y = 0 
charles_img = pygame.image.load('assets/images/player_16.png')

#ball
ball_x = 640
ball_y = 360
ball_delta_x = 2
ball_delta_y = 2
ball_img = pygame.image.load('assets/images/sbinotto.png')

# background update
def background_update():
	screen.blit(bg, (1,0))

# player update
def player_update_16(x, y):
	screen.blit(charles_img, (x, y))

def player_update_55(x ,y):
    screen.blit(carlos_img, (x, y))

def ball_update(x, y):
	screen.blit(ball_img, (x, y))


while_key = True

while while_key == True:
	background_update()
	player_update_16(charles_x, charles_y)	
	player_update_55(carlos_x, carlos_y)
	ball_update(ball_x, ball_y)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			while_key = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				charles_delta_y = -5
			if event.key == pygame.K_DOWN:
				charles_delta_y = 5
			if event.key == pygame.K_w:
				carlos_delta_y = -5
			if event.key == pygame.K_s:
				carlos_delta_y = 5

		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
				charles_delta_y = 0
			if (event.key == pygame.K_w) or (event.key == pygame.K_s):
				carlos_delta_y = 0

	ball_x += ball_delta_x
	ball_y += ball_delta_y
	
	if 0>charles_y:
		charles_y = 0
	elif 464<charles_y:
		charles_y = 464
	else:
		charles_y += charles_delta_y
	if 0>carlos_y:
		carlos_y = 0
	elif 464<carlos_y:
		carlos_y = 464
	else:
		carlos_y += carlos_delta_y
	pygame.display.update()