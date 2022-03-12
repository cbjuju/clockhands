import pygame
import time
from math import pi, sin, cos

current_time = 0
total_time   = 15
time_step    = 0.1

screen_width  = 400
screen_height = 400

origin  = (screen_width/2, screen_height/2)
start_x = origin[0]
start_y = origin[1]

screen = pygame.display.set_mode((screen_width, screen_height))

# while current_time < total_time:
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: exit()

    screen.fill((0, 0, 0))

    length = 50
    
    angle = current_time * (2 * pi) / total_time
    
    # Red line coding starts
    end_x = length * cos(angle)
    end_y = length * sin(angle)
    
    end_x = end_x + origin[0]
    end_y = end_y + origin[1]
    
    pygame.draw.line(screen, (255, 0, 0), (start_x, start_y), (end_x, end_y))
    # Red line coding ends

    # Blue line coding ends
    end_x = length * cos(4 * angle)
    end_y = length * sin(4 * angle)
    
    end_x = end_x + origin[0]
    end_y = end_y + origin[1]
    
    pygame.draw.line(screen, (0, 255, 0), (start_x, start_y), (end_x, end_y))
    # Blue line coding ends

    pygame.display.update()

    current_time += time_step
    time.sleep(time_step)
