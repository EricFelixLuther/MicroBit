from microbit import *

while True:
    display.clear()
    p1 = pin1.read_analog()
    p2 = pin2.read_analog()
    if p1 <= 204:
        x = 0
    elif 204 < p1 <= 408:
        x = 1
    elif 408 < p1 <= 612:
        x = 2
    elif 612 < p1 <= 816:
        x = 3
    else:
        x = 4

    if p2 <= 204:
        y = 4
    elif 204 < p2 <= 408:
        y = 3
    elif 408 < p2 <= 612:
        y = 2
    elif 612 < p2 <= 816:
        y = 1
    else:
        y = 0

    display.set_pixel(x,y,9)
    