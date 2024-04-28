import sys
import pygame
import random
import time
from pygame.color import THECOLORS

pygame.init() # инициализация


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
CARD_WIDTH = 220
CARD_HEIGHT = 200
GRID_ROWS = 5
GRID_COLS = 6
FPS = 60

# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255),(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (36, 34, 109), (255, 125, 3), (138, 207, 190), (207, 138, 193),(221,160,221), (240, 230, 140), (165, 42, 42), (188, 143, 143)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory game")
clock = pygame.time.Clock()

attempts_true, attempts_false = 0, 0


def create_grid():
    grid = []
    colors = COLORS * 2
    random.shuffle(colors)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            index = row * GRID_COLS + col
            if index < len(colors):
                card = {
                    'color': colors[index],
                    'rect': pygame.Rect(col * (CARD_WIDTH + 5) + 50, row * (CARD_HEIGHT + 5) + 50,
                                        CARD_WIDTH, CARD_HEIGHT),
                    'matched': False,
                    'open': False
                }
                grid.append(card)
    return grid




def draw_cards(grid):
    global attempts_true
    font = pygame.font.SysFont("Comic Sans", 40)
    text = font.render('Score: ' + str(attempts_true), True, THECOLORS['orange'])
    screen.blit(text, (1500, 50))
    text2 = font.render('Attemps: ' + str(20- attempts_false), True, THECOLORS['orange'])
    screen.blit(text2, (1500, 90))

    for card in grid:
        if card['matched']:
            pygame.draw.rect(screen, (50, 50, 50), card['rect'])
        elif card['open']:
            pygame.draw.rect(screen, card['color'], card['rect'])
        else:
            pygame.draw.rect(screen, WHITE, card['rect'])
    


def main():
    global attempts_false
    global attempts_true
    grid = create_grid()
    opened_cards = []
  

    running = True
    while running:
        screen.fill(BLACK)

        draw_cards(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for card in grid:
                    if card['rect'].collidepoint(pos) and not card['open'] and not card['matched'] and len(opened_cards) < 2:
                        card['open'] = True
                        opened_cards.append(card)
                        break

        if len(opened_cards) == 2:
            if opened_cards[0]['color'] == opened_cards[1]['color']:
                attempts_true += 1
                for card in opened_cards:
                    card['open'] = False
                    card['matched'] = True
                draw_cards(grid)  # обновить отображение карт
                pygame.display.flip()
            else:
                pygame.draw.rect(screen, opened_cards[1]['color'], opened_cards[1]['rect'])
                pygame.display.flip()
                time.sleep(0.5)
                opened_cards[0]['open'] = False
                opened_cards[1]['open'] = False
                attempts_false += 1
            opened_cards = []

        if 20 - attempts_false == 0:
            pygame.display.flip()
            time.sleep(0.5)
            screen2 = pygame.display.set_mode((600, 400))
            pygame.display.set_caption('END')
            screen2.fill(BLACK)

            font2= pygame.font.SysFont('Comic Sans', 80)
            text_end = font2.render('Loser ;)', True, THECOLORS['orange'])
            screen2.blit(text_end, (120, 100))
            pygame.display.flip()
            time.sleep(4)
            running = False
        elif attempts_true == 15:
            pygame.display.flip()
            time.sleep(0.5)
            screen2 = pygame.display.set_mode((600, 400))
            pygame.display.set_caption('END')
            screen2.fill(BLACK)

            font2= pygame.font.SysFont('Comic Sans', 80)
            text_end = font2.render('Winner ;)', True, THECOLORS['orange'])
            screen2.blit(text_end, (120, 100))
            pygame.display.flip()
            time.sleep(4)
            running = False



        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()


