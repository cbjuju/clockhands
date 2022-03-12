import pygame
import time

current_time = 0
total_time   = 15
time_step    = 0.1

screen = pygame.display.set_mode((400, 400))

while current_time < total_time:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: exit()

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (0, 0), (50, 50))

    pygame.display.update()

    current_time += time_step
    time.sleep(0.1)

print ("finished")
