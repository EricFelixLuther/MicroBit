from microbit import display, Image, pin2, button_a, button_b, sleep
import neopixel
import random
import music

class Rainbow():
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.ri = 0
        self.gi = 0
        self.bi = 0

    def increment(self):
        self.r += self.ri
        self.g += self.gi
        self.b += self.bi

    def __call__(self):
        # if red is at max: remove blue
        # if blue is at zero: add green
        # if green is at max: remove red
        # if red is at zero: add blue
        # if blue as at max: remove green
        # if green is at zero: add red
        if self.r == 0 and self.g == 0 and self.b == 0:
            # Start state. Begin adding red
            self.ri = 1
            self.gi = 0
            self.bi = 0
        if self.r == 255 and self.g == 0 and self.b == 0:
            # Red is at max. Start adding green
            self.ri = 0
            self.gi = 1
            self.bi = 0
        if self.r == 0 and self.g == 255 and self.b == 0:
            # Green is at max. Start adding blue
            self.ri = 0
            self.gi = 0
            self.bi = 1
        if self.r == 0 and self.g == 0 and self.b == 255:
            # Blue is at max, start adding red
            self.ri = 1
            self.gi = 0
            self.bi = 0
        if self.r == 255 and self.g == 255 and self.b == 0:
            # Red and green is yellow. Start removing red
            self.ri = -1
            self.gi = 0
            self.bi = 0
        if self.r == 255 and self.g == 0 and self.b == 255:
            # Red and blue is purple. Start removing blue
            self.ri = 0
            self.gi = 0
            self.bi = -1
        if self.r == 0 and self.g == 255 and self.b == 255:
            # Green and blue is cyan. Start removing green
            self.ri = 0
            self.gi = -1
            self.bi = 0
        if self.r == 255 and self.g == 255 and self.b == 255:
            # This situation should not occur
            raise Exception("White color achieved")

        self.increment()
        return [self.r, self.g, self.b]

def heartbeat(led):
    if led in (0, 2, 8, 10, 16, 18):
        display.show(Image.HEART_SMALL, wait=False)
        music.play(["C1:1"], wait=False)
    else:
        display.show(Image.HEART, wait=False)
    
np = neopixel.NeoPixel(pin2, 24)
l = 0
colors = (
    [255, 255, 255],  # white
    [255, 0, 0],  # red
    [0, 255, 0],  # green
    [0, 0, 255],  # blue
    [255, 0, 255],  # purple
    [255, 80, 0]  # orange
)
color_i = 0
color = colors[color_i]
rainbow = Rainbow()
leds = range(24)

i = 0
ii = 1

while True:
    while True:
        if button_a.get_presses():
            break
        if button_b.get_presses():
            color_i += 1
            if color_i >= len(colors):
                color_i = 0
            color = colors[color_i]
    
        heartbeat(l)

        for other_led in (0, 1, 2, 3, 4, 5):
            np[l - other_led] = [max(c - int(c * 0.2 * other_led) - 1, 0) for c in color]
        np.show()
        sleep(100)
        l += 1
        if l >= 24:
            l = 0

    while True:
        if button_a.get_presses():
            break
        if button_b.get_presses():
            color_i += 1
            if color_i >= len(colors):
                color_i = 0
            color = colors[color_i]
    
        #heartbeat(l)

        for led in leds:
            try:
                np[led] = [int(c * i / 100) for c in color]
            except:
                display.scroll(str(i))
        np.show()
        sleep(20)
        l += 1
        if l >= 24:
            l = 0

        if i <= 0:
            i = 0
            ii = 1
        elif i >= 100:
            i = 100
            ii = -1
        i += ii
    
    np.clear()
    color = Rainbow()
    while True:
        if button_a.get_presses():
            break
        
        heartbeat(l)

        for other_led in (0, 1, 2, 3, 4, 5):
            np[l - other_led] = [max(c - int(c * 0.2 * other_led) - 1, 0) for c in color()]
        np.show()
        sleep(100)
        l += 1
        if l >= 24:
            l = 0
