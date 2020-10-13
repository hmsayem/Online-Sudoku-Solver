import pyautogui as pg
import time
import copy

top_left_x = 1e5
top_left_y = 1e5
bottom_right_x = 0
bottom_right_y = 0
box_width = 0
box_height = 0

def get_top_bottom():
    for i in range(0, 11):
        image_file = "Images\\" + str(i) + '.png'
        for pos in pg.locateAllOnScreen(image_file, confidence=.9):
            global top_left_x, top_left_y, bottom_right_x, bottom_right_y, box_width, box_height
            X = pg.center(pos)[0]
            Y = pg.center(pos)[1]
            if((X + Y) < (top_left_x + top_left_y)):
                top_left_x = X
                top_left_y = Y
            if((X + Y) > (bottom_right_x + bottom_right_y)):
                bottom_right_x = X
                bottom_right_y = Y
            box_width = (bottom_right_x - top_left_x) / 8
            box_height = (bottom_right_y - top_left_y) / 8

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

grid_pos = [
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ],
    [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ]
]

def find_positions():
    for i in range(0, 9):
        for j in range(0, 9):
            X = top_left_x + (box_width * j)
            Y = top_left_y + (box_height* i)
            grid_pos[i][j][0] = X
            grid_pos[i][j][1] = Y

def fill_cell(value, pos):

    cell_x = int((pos[0] - top_left_x + (box_width / 2)) // box_width)
    cell_y = int((pos[1] - top_left_y + (box_height / 2)) // box_width)
    grid[cell_y][cell_x] = value

def fill_board():
    for i in range(1, 10):
        image_file = "Images\\" + str(i) + '.png'
        for pos in pg.locateAllOnScreen(image_file, confidence=.9):
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
                X = grid_pos[x][y][0]
                Y = grid_pos[x][y][1]
                pg.click(X, Y)
                pg.press(str(num))
                grid[x][y] = num
                if solver():
                    return True
                pg.click(X, Y)
                pg.press('backspace')
                grid[x][y] = 0;
        return False
    else:
        return True

time.sleep(3)
get_top_bottom()
find_positions()
fill_board()
print_board()
solver()
