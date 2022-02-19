import pygame
import fileseeker as fs
from pygame import mixer
import time

# importing all the variables from config file

main_window_size = fs.get_window_size()
main_window_title = fs.get_window_title()
delta_player = fs.get_player_delta()
delta_ball = fs.get_ball_delta()
boundary_player = fs.get_boundary_player()
load_sleep = fs.get_load_sleep()

# main window attributes

pygame.init()
screen = pygame.display.set_mode(main_window_size)
pygame.display.set_caption(main_window_title)
mixer.music.load('assets/audio/Funiculi Funicula.mp3')
mixer.music.play()

# load to sync the music playback
time.sleep(load_sleep)

# background
bg = pygame.image.load('assets/images/ferrari_tractor.png')
bg = pygame.transform.scale(bg, main_window_size)

# player attributes

carlos_x = 100
carlos_y = 300
carlos_delta_y = 0   #no delta x cause he will only move up and down
carlos_img = pygame.image.load('assets/images/player_55.png')

charles_x = 1000
charles_y = 300
charles_delta_y = 0 
charles_img = pygame.image.load('assets/images/player_16.png')

#ball attributes
ball_x = 640
ball_y = 360
ball_delta_x = delta_ball
ball_delta_y = delta_ball
ball_img = pygame.image.load('assets/images/sbinotto.png')

# background update
def background_update():
	screen.blit(bg, (1,0))

s55=s16=0
font_show = pygame.font.Font('freesansbold.ttf', 32)
def show_font(x, y):
	font_display = font_show.render('CARLOS: ' + str(s55) + ' CHARLES: ' + str(s16), True, (255, 255,255))
	screen.blit(font_display, (0,0))

# player update
def player_update_16(x, y):
	screen.blit(charles_img, (x, y))

def player_update_55(x ,y):
    screen.blit(carlos_img, (x, y))

def ball_update(x, y):
	screen.blit(ball_img, (x, y))

# key for game loop
while_key = True

# game loop
while while_key == True:
	background_update()
	player_update_16(charles_x, charles_y)	
	player_update_55(carlos_x, carlos_y)
	ball_update(ball_x, ball_y)
	show_font(s55, s16)

	# monitors the user inputs
	for event in pygame.event.get():
		# function enables quitting the program
		if event.type == pygame.QUIT:
			while_key = False

		# monitors key presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				charles_delta_y = -(delta_player)
			if event.key == pygame.K_DOWN:
				charles_delta_y = (delta_player)
			if event.key == pygame.K_w:
				carlos_delta_y = -(delta_player)
			if event.key == pygame.K_s:
				carlos_delta_y = (delta_player)

		# monitors key releases
		if event.type == pygame.KEYUP:
			if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
				charles_delta_y = 0
			if (event.key == pygame.K_w) or (event.key == pygame.K_s):
				carlos_delta_y = 0

	# delta gives the speed of ball movement
	ball_x += ball_delta_x
	ball_y += ball_delta_y

	# collission detection
	if (ball_x == carlos_x+64) and (carlos_y <= ball_y <= carlos_y+224):
		ball_delta_x = -(ball_delta_x)
	

	if (ball_x == charles_x-32) and (charles_y <= ball_y <= charles_y+224):
		ball_delta_x = -(ball_delta_x)
	

	if (ball_y == (main_window_size[1])-32) or (ball_y == (0)):
		ball_delta_y = -(ball_delta_y)

	# scoring mechanism
	if ball_x > 1280:
		s55 += 1
		ball_x = 640
		ball_y = 340

	if ball_x < -32:
		s16 += 1
		ball_x = 640
		ball_y = 340
	# boundary for the paddles
	if 0 > charles_y:
		charles_y = 0
	elif boundary_player < charles_y:
		charles_y = boundary_player
	else:
		charles_y += charles_delta_y
	if 0 > carlos_y:
		carlos_y = 0
	elif boundary_player < carlos_y:
		carlos_y = boundary_player
	else:
		carlos_y += carlos_delta_y

	# display update
	pygame.display.update()

# henlo can you hear me?
