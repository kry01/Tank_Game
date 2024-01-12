# import math

# def calculate_coordinate_changes(radius, angle_change):
#     angle_in_radians = math.radians(angle_change)
#     delta_x = radius * math.cos(angle_in_radians)
#     delta_y = radius * math.sin(angle_in_radians)
#     return delta_x/100, delta_y/100

# # Example usage
# radius = 50  # Replace with the actual radius of your tank's barrel
# angle_change = 1  # Change in angle in degrees

# delta_x, delta_y = calculate_coordinate_changes(radius, angle_change)
# print(f"The change in x-coordinate for a 1-degree angle change is: {delta_x}")
# print(f"The change in y-coordinate for a 1-degree angle change is: {delta_y}")


import pygame
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 30))

# Function to draw fire in a circular path
def draw_circular_fire(start_tank, target_tank):
    radius = 100  # Radius of the circular path
    num_points = 100  # Number of points to draw the circular path

    for i in range(num_points):
        angle =(( 2 * math.pi * i ) //2)/ num_points
        fire_x = start_tank.x + int(radius * math.cos(angle))
        fire_y = start_tank.y - int(radius * math.sin(angle))
        
        pygame.draw.circle(screen, RED, (fire_x, fire_y), 5)
        pygame.display.flip()
        clock.tick(FPS)

# Create tanks
tank1 = Tank(100, 300, (100, 100, 100))
tank2 = Tank(600, 300, (100, 100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    tank1.draw()
    tank2.draw()

    draw_circular_fire(tank1, tank2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
