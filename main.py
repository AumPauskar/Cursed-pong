import pygame
import fileseeker as fs

# constants

main_window_size = fs.get_window_size()
main_window_title = fs.get_window_title()

# window

pygame.init()
screen = pygame.display.set_mode(main_window_size)
pygame.display.set_caption(main_window_title)

#background
bg = pygame.image.load('assets/pizza.png')
bg = pygame.transform.scale(bg, main_window_size)

#players

carlos_x = 100
carlos_y = 300
carlos_delta_y =0   #no delta x cause he will only move up and down
carlos_img = pygame.image.load('assets/player_55.png')

charles_x = 1000
charles_y = 300
charles_delta_y = 0 
charles_img = pygame.image.load('assets/player_16.png')

#background update
def background_update():
	screen.blit(bg, (1,0))

#player update
def player_update_16(x,y):
	screen.blit(charles_img, (x,y))

def player_update_55(x,y):
    screen.blit(carlos_img, (x,y))