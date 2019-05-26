from microbit import display, Image, pin2, button_a, button_b
import neopixel
import random
import music
import itertools


class Color():
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

    def color(self):
        return (self.r, self.g, self.b)

    def __call__(self):
        yield self.color()

class White(Color):
    def __init__(self):
        self.r = 255
        self.g = 255
        self.b = 255

class DimWhite(Color):
    def __init__(self):
        self.r = 100
        self.g = 100
        self.b = 100

class Red(Color):
    def __init__(self):
        self.r = 255
        self.g = 0
        self.b = 0
        
class Blue(Color):
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 255

class Purple(Color):
    def __init__(self):
        self.r = 255
        self.g = 0
        self.b = 255
        
class Rainbow(Color):
    def __call__(self):
        while self.r < 255:     # add red
            self.r += 1
            yield self.color()
        while self.b > 0:       # remove blue
            self.b -= 1
            yield self.color()
        while self.g < 255:     # add green
            self.g += 1
            yield self.color()
        while self.r > 0:       # remove red
            self.r -= 1
            yield self.color()
        while self.b < 255:     # add blue
            self.b += 1
            yield self.color()
        while self.g > 0:       # remove green
            self.g -= 1
            yield self.color()

class Colors(): 
    def __init__(self):
        self.colors = (White, DimWhite, Red, Blue, Purple, Rainbow)
        self.i = -1

    def get_next_color(self):
        self.i += 1
        if self.i >= len(self.colors):
            self.i = 0
        return self.colors[self.i]()

class Index():
    def __init__(self):
        self.i = -1
    
    def __call__(self):
        self.i += 1
        if self.i >= 24:
            self.i = 0
        return self.i
        
def heartbeat():
    music.play(["C1:1"], wait=False)

np = neopixel.NeoPixel(pin2, 24)
i = Index()
mode = 0
colors = Colors()
color = colors.get_next_color() 
LEDS = range(24)

while True:
    if button_a.get_presses():
        mode += 1
        if mode >= 4:
            mode = 1
    if button_b.get_presses():
        color = colors.get_next_color()
    c = list(color())
    if i in (7, 15, 23):
        display.show(Image.HEART_SMALL)
        heartbeat()
    else:
        display.show(Image.HEART)
        if i in (0, 8, 16):
            heartbeat()
    if mode == 0:
        for o in [i() - x for x in range(5)]:
            np[o] = (max(z - 15 * abs(o), 0) for z in c)
        np.show()
        sleep(100)
        np.clear()
    elif mode == 1:
        np[i()] = c
        np.show()
    elif mode == 2:
        pass
