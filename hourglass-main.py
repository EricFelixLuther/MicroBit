# Imports go at the top
from microbit import *
import neopixel
import music

time = 15  # default hourglass time in minutes

# select time
while not accelerometer.was_gesture('shake'):
    if button_a.was_pressed():
        time = max(1, time - 1)
    if button_b.was_pressed():
        time = min(50, time + 1)
    # extrapolate time number onto screen
    image_string = '9' * int(time / 2) + ('2' if time % 2 == 1 else '0')
    while len(image_string) < 25:
        image_string += '0'
    substrings = []
    for i in range(0, len(image_string), 5):
        # Extract a substring of length 5 starting from the current index
        substring = image_string[i:i+5]
        # Add the substring to the list
        substrings.append(substring)
    display.show(Image(":".join(substrings)))
# select color
display.scroll('Wybierz kolor', delay=100)
TOTAL_LEDS = 24
np = neopixel.NeoPixel(pin2, TOTAL_LEDS)
leds = list(range(TOTAL_LEDS))
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
color_i = 0
for led in leds:
    for i in range(256):
        np[led] = [i, i, i]
        np.show()
        sleep(0.05)

while not accelerometer.was_gesture('shake'):
    for led in leds:
        np[led] = colors[color_i]
    if button_a.was_pressed():
        color_i -= 1
        if color_i < 0:
            color_i = len(colors) - 1
    if button_b.was_pressed():
        color_i += 1
        if color_i > len(colors):
            color_i = 0
    np.show()
# hourglass go
display.scroll("Czas start", wait=False)
selected_color = colors[color_i]
leds.reverse()
sleep_time = round((time * 60 * 1000) / (256 * TOTAL_LEDS), 4)
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