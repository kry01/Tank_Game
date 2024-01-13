import pygame
import math

clock = pygame.time.Clock()

class Tank:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 70
        self.height = 40
        self.turret_length = 20
        self.screen = screen
        self.health = 100  # Initial health
        self.barrel_angle = 0

    def draw(self, barrel_angle):
        pygame.draw.rect(self.screen, (100, 100, 100), [self.x, self.y, self.width, self.height], border_radius = 7)
        circle_x = self.x + (self.width // 2) 
        circle_y = self.y - self.turret_length  + (self.height // 2) 
        pygame.draw.circle(self.screen, (100, 100, 100), (circle_x, circle_y), 20)

        barrel_width = 5
        barrel_length = 40
        barrel_x = self.x  + (self.width // 2) - (barrel_width // 2)
        barrel_y = self.y - self.turret_length  - barrel_length 
        rotated_barrel = pygame.Surface((barrel_width, barrel_length), pygame.SRCALPHA)
        rotated_barrel.fill((100, 100, 100)) 
        rotated_barrel = pygame.transform.rotate(rotated_barrel, barrel_angle)
        rotated_rect = rotated_barrel.get_rect(center=(barrel_x + barrel_width // 2, barrel_y + barrel_length))
        self.screen.blit(rotated_barrel, rotated_rect.topleft)

    def fire(self, n):
        barrel_width = 5
        
        barrel_y = self.y - self.turret_length  # Adjusted to start from the barrel's head
        # check which tank to throw fire and calculate
        if n == 1:
            barrel_x = self.x + (self.width // 2) - (barrel_width // 2) + 45 // 2
        else:
            barrel_x = self.x + (self.width // 2) - (barrel_width // 2) - 45 // 2
        starting_shell_x = barrel_x + barrel_width // 2
        starting_shell_y = barrel_y
        shell_speed = 5

        print('Fire!')

            # Get the normalized direction vector of the tank's turret
        direction_vector = pygame.Vector2(1, 0).rotate(self.barrel_angle)

        # Loop for animating the fired shells
        while (starting_shell_x < 800 and starting_shell_x > 0) and (starting_shell_y < 600 and starting_shell_y > 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # Update the shell position based on the direction vector
            if n == 1:
                starting_shell_x += direction_vector.x * shell_speed
                starting_shell_y += direction_vector.y * shell_speed
            else:
                starting_shell_x -= direction_vector.x * shell_speed
                starting_shell_y -= direction_vector.y * shell_speed

            pygame.draw.circle(self.screen, (255, 0, 0), (int(starting_shell_x), int(starting_shell_y)), 5)
            # starting_shell_x -= shell_speed

            pygame.display.update()
            clock.tick(60)

        print('Hit!')
