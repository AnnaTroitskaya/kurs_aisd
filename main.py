import pygame
import numpy as np
import sys
from button import Button
from button import Text
from input_box import InputBox


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 40, 40
CELL_SIZE = WIDTH // COLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (240, 128, 128)
HZ = (255, 255, 235)
GREY = (30,  40 , 20)

cells = np.zeros((ROWS, COLS))
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(window, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(window, GREY, (0, y), (WIDTH, y))

def draw_cells():
    for row in range(ROWS):
        for col in range(COLS):
            cell_color = PINK if cells[row, col] else HZ
            pygame.draw.rect(window, cell_color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid(list_s, list_b):
    new_grid = np.copy(cells)

    for row in range(ROWS):
        for col in range(COLS):
            neighbors = count_neighbors(row, col)

            if cells[row, col] == 1:
                if not (neighbors in list_s):
                    new_grid[row, col] = 0
            else:
                if neighbors in list_b:
                    new_grid[row, col] = 1

    return new_grid

def count_neighbors(row, col):
    count = 0

    count += cells[(row - 1) % ROWS, (col - 1) % COLS]
    count += cells[(row - 1) % ROWS, col]
    count += cells[(row - 1) % ROWS, (col + 1) % COLS]
    count += cells[row, (col - 1) % COLS]
    count += cells[row, (col + 1) % COLS]
    count += cells[(row + 1) % ROWS, (col - 1) % COLS]
    count += cells[(row + 1) % ROWS, col]
    count += cells[(row + 1) % ROWS, (col + 1) % COLS]

    return count


def menu_screen():
    start_button = Button(PINK, HEIGHT // 2 - 75, 200, 150, 70, 'START')
    text_sur = Text('Number of neighbors to survive:', 23, GREY, HEIGHT // 2 - 170, 307)
    text_bir = Text('Number of neighbors to be born:', 23, GREY, HEIGHT // 2 - 170, 407)
    text_mess = Text('(Enter the numbers separated by SPACE)', 25, GREY, HEIGHT // 2 - 250, 600)
    input_sur = InputBox(HEIGHT // 2 - 100, 340, 100, 50)
    input_bir = InputBox(HEIGHT // 2 - 100, 440, 100, 50)
    running = True
    survival = []
    birth = []

    while running:
        window.fill(HZ)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            input_sur.handle_event(event, survival)
            input_bir.handle_event(event, birth)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    print('Button clicked!')
                    game_of_life(survival, birth)

        start_button.draw(window)
        text_sur.draw(window)
        text_bir.draw(window)
        text_mess.draw(window)
        input_sur.update()
        input_sur.draw(window)
        input_bir.update()
        input_bir.draw(window)
        pygame.display.flip()


    pass


def game_of_life(list1, list2):
    running = True
    start_simulation = False
    global cells
    while running:
        clock.tick(70)  # Adjust this value to control the speed of the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not start_simulation:
                    pos = pygame.mouse.get_pos()
                    col = pos[0] // CELL_SIZE
                    row = pos[1] // CELL_SIZE
                    cells[row, col] = 1 - cells[row, col]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_simulation = True

        if start_simulation:
            cells = update_grid(list1, list2)


        window.fill(HZ)
        # draw_grid()
        draw_cells()
        draw_grid()
        pygame.display.update()

menu_screen()