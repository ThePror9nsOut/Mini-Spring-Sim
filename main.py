import pygame as pg
import time

win = pg.display.set_mode((1300,700))
run = True

overall_divider = 40
distance_divider = 20
friction_divider = 1000
bounciness_divider = 400

gravity = 0.01

object = [250,250]
dx, dy = 0, 0

while run:
    win.fill((0,0,0))

    pg.draw.rect(win,(255,255,255),(object[0]-10,object[1]-10,20,20))

    mouse = pg.mouse.get_pos()

    if pg.mouse.get_pressed()[0]:
        pg.draw.line(win, (255,255,255), object, mouse)

        # Magic
        dx += ((1 if object[0] < mouse[0] else -1)/10 * abs(object[0] - mouse[0])/distance_divider)/overall_divider
        dy += ((1 if object[1] < mouse[1] else -1)/10 * abs(object[1] - mouse[1])/distance_divider)/overall_divider

    object[0] += dx
    object[1] += dy

    # Gravity pull down
    dy += gravity

    # Declaring screen margins
    if object[0] <= -300+10 or object[0] >= 1600-10: dx = -dx - dx/bounciness_divider
    if object[1] <= -300+10 or object[1] >= 700-10: dy = -dy - dy/bounciness_divider

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
