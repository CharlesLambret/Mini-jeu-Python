import pygame
from functions import Functioning

class Input(Functioning):
    def user_input(self, listen_events):
        for event in listen_events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.level_finished:
                    self.level += 1
                    if self.level >= 6:
                        self.level = 1
                    self.start_level(self.level)
        
               

