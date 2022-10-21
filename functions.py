import pygame, random, os
from getfiles import Images


WINDOW_WIDTH=1000
FPS = 60

class Functioning():
    def __init__(self):
        self.level = 1
        self.level_finished = False

        self.every_card = [f for f in os.listdir('images/') if os.path.join('images/', f)]

        self.img_width, self.img_height = (80, 150)
        self.padding = 10
        self.margin_top = 160

        self.cols = 5
        self.rows = 2
        
        self.width = 1000
        self.cards_group = pygame.sprite.Group()

        self.turned = []
        self.found = []
        self.frame_count = 0
        self.stop_game = False
       
        self.start_level(self.level)
   

    def level_completed(self, listen_events):
        if not self.stop_game:
            self.frame_count = + 1 
            for event in listen_events:
                left_click = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
                if left_click:
                    for card in self.cards_group:
                        card_collision = card.rect.collidepoint(event.pos)
                        if card_collision and not card.found:
                            self.turned.append(card.name)
                            card.show()

                            if len(self.turned) == 2:
                                if self.turned[0] != self.turned[1]:
                                    self.stop_game = True

                                else:
                                    self.turned = []
                                    self.found.append(card.name)
                                    for card in self.cards_group:
                                        if card.shown:
                                            self.level_finished = True
                                        else:
                                            self.level_finished = False
                                            break


        else:
            self.frame_count += 1
            if self.frame_count == FPS:
                self.frame_count = 0
                self.stop_game = False

                for card in self.cards_group:
                    if card.name in self.turned:
                        card.hide()
                self.turned = []


    def start_level(self, level):
        self.astrocards = self.random_selecter(self.level)
        self.level_finished = False
        self.rows = self.level + 1
        self.cols = 8
        self.create_disposition(self.astrocards)

    def create_disposition(self, astrocards):
        self.cols = self.rows = self.cols if self.cols >= self.rows else self.rows

        CARDS_WIDTH = (self.img_width * self.cols + self.padding)
        MARGIN_LEFT = MARGIN_RIGHT = ((self.width - CARDS_WIDTH) // 2)

        self.cards_group.empty()

        for i in range(len(astrocards)):
            x = MARGIN_LEFT + ((self.img_width + self.padding) * (i % self.cols))
            y = self.margin_top + (i // self.rows * (self.img_height + self.padding))
            card = Images(astrocards[i], x, y)
            self.cards_group.add(card)


    def random_selecter(self, level):
        astrocards = random.sample(self.every_card, (self.level + self.level + 2))
        cards_copy = astrocards.copy()
        astrocards.extend(cards_copy)
        random.shuffle(astrocards)
        return astrocards
