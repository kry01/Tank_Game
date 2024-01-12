import pygame

from tank import Tank

class Game:
    def __init__(self, width, height, title, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

    # def run(self):
    #     running = True
    #     while running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 running = False

    #         self.screen.fill(self.background_color)

    #         pygame.display.flip()
    #     pygame.quit()

    def get_screen(self):
        return self.screen