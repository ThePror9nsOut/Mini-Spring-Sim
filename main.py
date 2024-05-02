import pygame as pg
import time

win = pg.display.set_mode((1000,700))
run = True


distance_divider = 30
overall_divider = 40
friction_divider = 1000
bounciness_divider = 50

gravity = 0.005


char = [250,250]
dx, dy = 0, 0

last_time = time.time()

while run:
    delta = time.time() - last_time
    last_time = time.time()

    win.fill((0,0,0))

    pg.draw.rect(win,(255,255,255),(char[0]-10,char[1]-10,20,20))

    mouse = pg.mouse.get_pos()

    if pg.mouse.get_pressed()[0]:
        pg.draw.line(win,(255,255,255), char, mouse)

        # Magic
        dx += ((1 if char[0] < mouse[0] else -1)/10 * abs(char[0] - mouse[0])/distance_divider)/overall_divider
        dy += ((1 if char[1] < mouse[1] else -1)/10 * abs(char[1] - mouse[1])/distance_divider)/overall_divider

    char[0] += dx
    char[1] += dy

    # Gravity pull down
    dy += gravity

    # Declaring screen margins
    if char[0] <= 0+10 or char[0] >= 1000-10: dx = -dx - dx/bounciness_divider
    if char[1] <= 0+10 or char[1] >= 700-10: dy = -dy - dx/bounciness_divider

    # Decreasing momentum over time
    if dx > 0: dx -= dx/friction_divider
    elif dx < 0: dx -= dx/friction_divider
    if dy > 0: dy -= dy/friction_divider
    elif dy < 0: dy -= dy/friction_divider

    # Stopping momentum so it doesn't decrease infinitely
    if 0.0001 > dx > -0.0001: dx = 0
    if 0.0001 > dy > -0.0001: dy = 0

    pg.display.flip()

    if len(pg.event.get(pg.QUIT)) > 0: run = False