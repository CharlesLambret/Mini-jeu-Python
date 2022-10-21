import pygame,random,os
from getfiles import Images
from functions import Functioning
from input import Input
from getfiles import Images

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (127, 0, 255)
WINDOW_WIDTH=1000
WINDOW_HEIGHT = 750
FPS=60
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Memory Game')

class Display(Input, Functioning):

    def update(self, listen_events):
        self.user_input(listen_events)
        self.draw()
        self.level_completed(listen_events)

    def draw(self):
        window.fill(PURPLE)

        Title_font = pygame.font.Font('fonts/OpenSans-Bold.ttf', 40)
        Content_font = pygame.font.Font('fonts/Kanit-regular.ttf', 25)
   
        Title = Title_font.render('Jeu de mémoire super stylé', True, WHITE)
        Level_indication = Content_font.render('Niveau ' + str(self.level), True, WHITE)
        dull_text = Content_font.render('Trouvez les paires', True, WHITE)
        Turnedcards = Content_font.render('Cartes découvertes' + str(len(self.found)), True, WHITE)

        if not self.level == 5:
            ending_text = Content_font.render('Niveau terminé. Appuyez sur espace pour continuer', True, WHITE)
        else:
            ending_text = Content_font.render('Vous avez gagné ! Appuyez sur espace pour rejouer', True, WHITE)

        Title_rectangle = Title.get_rect(midtop = (WINDOW_WIDTH // 2, 10))
        Level_rectangle = Level_indication.get_rect(midtop = (WINDOW_WIDTH // 2, 80))
        dull_rectangle = dull_text.get_rect(midtop = (WINDOW_WIDTH // 2, 120))
        ending_rectangle = ending_text.get_rect(midbottom = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 40))
        Turned_rectangle = Turnedcards.get_rect(midtop = (800, 500))

        window.blit(Title, Title_rectangle)
        window.blit(Level_indication, Level_rectangle)
        window.blit(dull_text, dull_rectangle)
        window.blit(Turnedcards, Turned_rectangle)


    
        self.cards_group.draw(window)
        self.cards_group.update()

        if self.level_finished:
            window.blit(ending_text, ending_rectangle)

   