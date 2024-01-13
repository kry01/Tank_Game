# main.py
import pygame
import random
from game import Game
from tank import Tank
from functions import *

background_color = (255, 255, 255)
screen_width = 800
screen_height = 600
wall_height = random.randint(100, 600)
tankOneX = 30
tankTwoX = 700
tankOneAngle = -45
tankTwoAngle = 45
fireX = 0
fireY = 0

game = Game(screen_width, screen_height, "our game", background_color)
screen = game.get_screen()


running = True
clock = pygame.time.Clock()

# Variable to keep track of the current tank's turn to fire
current_tank_turn = 1

while running:
    tankOne = Tank(x=tankOneX, y=550, screen=screen)
    tankTwo = Tank(x=tankTwoX, y=550, screen=screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # check the limits to move tanks
            if event.key == pygame.K_LEFT and tankOneX > 0:
                tankOneX -= 5
            elif event.key == pygame.K_RIGHT and tankOneX <= 320:
                tankOneX += 5
            elif event.key == pygame.K_UP and tankOneAngle <= -10:
                tankOneAngle += 5
            elif event.key == pygame.K_DOWN and tankOneAngle >= -80:
                tankOneAngle -= 5 
            elif event.key == pygame.K_q and tankTwoX >= 430:
                tankTwoX -= 5
            elif event.key == pygame.K_d and tankTwoX < 730:
                tankTwoX += 5
            elif event.key == pygame.K_w and tankTwoAngle <= 80:
                tankTwoAngle += 5
            elif event.key == pygame.K_z and tankTwoAngle >= 10:
                tankTwoAngle -= 5
            elif event.key == pygame.K_SPACE:
                # Check whose turn it is to fire
                if current_tank_turn == 1:
                    tankOne.fire(1)
                else:
                    tankTwo.fire(2)

                # Switch the turn to the other tank
                current_tank_turn = 3 - current_tank_turn  # Toggle between 1 and 2

    screen.fill(background_color)

    
    tankOne.draw(tankOneAngle)
    tankTwo.draw(tankTwoAngle)



    wall_y = screen_height - wall_height // 2
    draw_wall(screen,screen_width//2,wall_y,wall_height)

    # Display health bars
    tank_one_health_bar_width = tankOne.health * 2  # Adjust for a suitable width
    tank_two_health_bar_width = tankTwo.health * 2  # Adjust for a suitable width

    pygame.draw.rect(screen, (50, 255, 50), [20, 20, tank_one_health_bar_width, 20])  # Green bar for Tank One
    pygame.draw.rect(screen, (50, 255, 50), [screen_width - tank_two_health_bar_width - 20, 20, tank_two_health_bar_width, 20])  # Red bar for Tank Two

    pygame.display.flip()
    clock.tick(100)

pygame.quit()