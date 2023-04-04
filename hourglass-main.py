# Imports go at the top
from microbit import *
import neopixel
import music

time = 1  # default hourglass time in minutes
TOTAL_LEDS = 24
np = neopixel.NeoPixel(pin2, TOTAL_LEDS)
colors = [
    [255, 255, 255],  # white
    [0, 255, 0],  # green
    [255, 0, 0],  # red
    [0, 0, 255],  # blue
    [255, 0, 255],  # purple
    [255, 80, 0],  # orange
    [255, 255, 0],  # yellow
    [0, 255, 255], # cyan
]
# select color
display.scroll('Wybierz kolor', delay=100, wait=False)

for i in range(256):
    np[0] = [i, i, i]
    np.show()
    sleep(0.1)

color_i = 0

while not accelerometer.was_gesture('shake'):
    np[0] = colors[color_i]
    if button_a.was_pressed():
        color_i -= 1
        if color_i < 0:
            color_i = len(colors) - 1
    if button_b.was_pressed():
        color_i += 1
        if color_i >= len(colors):
            color_i = 0
    np.show()
selected_color = colors[color_i]

# select time
display.scroll('Ile minut', delay=100, wait=False)
while not accelerometer.was_gesture('shake'):
    if button_a.was_pressed():
        time = max(1, time - 1)
        np[time] = [0, 0, 0]
    if button_b.was_pressed():
        time = min(24, time + 1)
        np[time - 1] = selected_color
    np.show()

# hourglass go
display.scroll("Czas start", wait=False)
leds = list(range(time))
leds.reverse()
sleep_time = round((60 * 1000) / 256, 4)
for led in leds:
    current_led_color = selected_color.copy()
    while any(current_led_color):
        current_led_color = [max(c - 1, 0) for c in current_led_color]
        np[led] = current_led_color
        np.show()
        sleep(sleep_time)
        
while not button_a.was_pressed() and not button_b.was_pressed():
    display.scroll('Koniec!', wait=False)
    music.play(music.DADADADUM, loop=True)
