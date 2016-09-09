import pygame
from random import randint

pygame.init()

screen_width = 400
screen_height = 600
screen_caption = 'PyFly'
fps = 30

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_caption)
clock = pygame.time.Clock()

#colors
bg_color = (33, 33, 33)
cat_color = (200, 60, 80)
wall_color = (250, 250, 50)

#cat is the moving character
cat_x = 200
cat_y = 300
cat_width = 10
cat_height = 10
cat = pygame.Rect(cat_x, cat_y, cat_width, cat_height)

#change in x value
x_delta = 0
#sideways speed
x_speed = 10
#speed of incoming walls
y_speed = 7

#thickness of walls
wall_height = 5
#size of hole in the wall
hole_width = 100
#vertical gap between two walls
wall_gap = screen_height / 3

#in each item of the walls list, first element is the distance from top of screen
#second element is the distance of the hole from left side of screen
#these two values are used to draw the walls
walls = [[cat_y+wall_gap, 10], [cat_y+wall_gap*2, 20], [cat_y+wall_gap*3, 30], [cat_y+wall_gap*4, 40]]
for i in range(0, 4):
	walls[i][1] = randint(0, screen_width - hole_width)

run_game = True

#game loop
while run_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_game = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_delta = -x_speed

			if event.key == pygame.K_RIGHT:
				x_delta = x_speed

		#needs improved key handling
		if event.type == pygame.KEYUP:	
			x_delta = 0

	cat_x += x_delta 
	#wrap around back to screen
	cat_x %= screen_width

	#update wall positions
	for i in range (0, 4):
		walls[i][0] -= y_speed
		if walls[i][0] < 0:
			walls[i][0] = walls[(i-1)%4][0]+wall_gap
			walls[i][1] = randint(0, screen_width - hole_width)

	#rendering starts
	game_screen.fill(bg_color)

	cat = pygame.Rect(cat_x, cat_y, cat_width, cat_height)

	#draw walls
	for i in range (0, 4):	
		rect1 = pygame.Rect(0, walls[i][0], walls[i][1], wall_height)
		rect2 = pygame.Rect(walls[i][1]+hole_width, walls[i][0], screen_width-walls[i][1]-hole_width, wall_height)

		#check collision of walls with cat
		#only changes color for now
		if pygame.Rect(cat).colliderect(rect1) or pygame.Rect(cat).colliderect(rect2):
			cat_color = (0, 255, 0)
		game_screen.fill(wall_color, rect = rect1)
		game_screen.fill(wall_color, rect = rect2)

	#draw cat
	game_screen.fill(cat_color, rect = cat)

	pygame.display.update()
	clock.tick(fps)

pygame.quit()
quit()