import pygame
import math
pygame.init()

def draw_wall(screen, x,y, height):
    pygame.draw.rect(screen, (100, 100, 100), [x, y, 25, height])


# def power(screen,screen_width,level):
#     font = pygame.font.SysFont(None, 36)
#     text = font.render("Power: " + str(level) + "%", True, (245, 222, 179))
#     # text =  pygame.font.render("Power: " + str(level) + "%", True, (245,222,179))
#     screen.blit(text, [screen_width / 2, 0])
