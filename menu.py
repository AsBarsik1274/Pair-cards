import pygame
import sys
import os

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Меню")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифты
font = pygame.font.SysFont("Comic Sans", 20)
menu_font = pygame.font.SysFont("Comic Sans", 40)

# Переменные для кнопок
play_button1 = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 80, 100, 50)
play_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)
play_button2 = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 30, 100, 50)

# Функция отрисовки текста
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Функция отрисовки меню
def draw_menu():
    screen.fill(WHITE)
    draw_text("Меню", menu_font, BLACK, screen, WIDTH // 2, 50)

    # Отрисовка кнопок

    pygame.draw.rect(screen, (0, 255, 0), play_button1)
    draw_text(" ", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 - 55)

    pygame.draw.rect(screen, (255, 255, 0), play_button)
    draw_text(" ", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
    
    pygame.draw.rect(screen, (255, 0, 0), play_button2)
    draw_text(" ", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 52.5)

    pygame.display.flip()

# Функция для переключения в игру
def switch_to_8():
    pygame.quit()
    os.system('python low.py')
    # sys.exit()

def switch_to_12():
    pygame.quit()
    os.system('python normal.py')
    # sys.exit()

def switch_to_24():
    pygame.quit()
    os.system('python high.py')
    # sys.exit()


# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Проверяем нажатие кнопки
                if play_button1.collidepoint(event.pos):
                    switch_to_8()
                if play_button.collidepoint(event.pos):
                    switch_to_12()
                if play_button2.collidepoint(event.pos):
                    switch_to_24()
                

    draw_menu()

pygame.quit()