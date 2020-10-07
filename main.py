import pyautogui as pg
import time
import copy

top_left_x = 486
top_left_y = 223
bottom_right_x = 884
bottom_right_y = 623
box_width = (bottom_right_x - top_left_x) / 8
box_height = (bottom_right_y - top_left_y) / 8
time.sleep(2)

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def fill_cell(value, pos):
    cell_x = int((pos[0] - top_left_x + (box_width / 2)) // box_width)
    cell_y = int((pos[1] - top_left_y + (box_height / 2)) // box_width)
    grid[cell_y][cell_x] = value


def fill_board():
    for i in range(1, 10):
        for pos in pg.locateAllOnScreen(str(i) + '.png', confidence=.95):
            pg.click(pg.center(pos))
            fill_cell(i, pg.center(pos))


def print_board():
    for i in range(0, 9):
        for j in range(0, 9):
            print(grid[i][j], end=" ")
        print()


def valid(x, y, num):
    for i in range(0, 9):
        if grid[i][y] == num:
            return False
    for j in range(0, 9):
        if grid[x][j] == num:
            return False
    box_x = int(x / 3) * 3;
    box_y = int(y / 3) * 3;

    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if grid[i][j] == num:
                return False
    return True;


def find_empty():
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def solver():
    find = find_empty()  # finds an empty cell
    if find:
        x, y = find
        for num in range(1, 10):
            if valid(x, y, num):
                grid[x][y] = num
                if solver():
                    return True
                grid[x][y] = 0;
        return False
    else:
        return True


def show_board(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=" ")
        print("")


def draw(value, x, y):
    pos_x = top_left_x + (x * box_width)
    pos_y = top_left_y + (y * box_height)
    pg.click(pos_x, pos_y)
    pg.press(str(value))


def run():
    for i in range(0, 9):
        for j in range(0, 9):
            if grid_unsolved[i][j] == 0:
                draw(grid[i][j], j, i)


time.sleep(1)
fill_board()
grid_unsolved = copy.deepcopy(grid)
solver()
run()
