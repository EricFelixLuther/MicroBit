from microbit import *
import neopixel
import random


class Colors():
	def __init__(self):
		self.i = -1
		self.colors = (
			(255, 255, 255),
            (255, 0, 0),
            (255, 255, 0),
            (0, 255, 0),
            (0, 255, 255),
            (0, 0, 255),
            (255, 0, 255)
		)
		self.next_color()

	def check_change_color(self):
		if button_a.get_presses() or button_b.get_presses():
			return self.next_color()

    def next_color(self):
		self.i += 1
		if self.i >= len(self.colors):
			self.i = 0
		return self.colors[self.i]

		
class Wheel():
    def __init__(self):
        self.speed = 0
		self.i = 1
		self.np = neopixel.NeoPixel(pin2, 24)
		self.led = -1
		self.color = Colors()

	def next_led(self):
		self.led += 1
		self.np[led] = self.color
		self.np.show()
		
    def shake(self):
		if accelerometer.is_gesture('shake'):
			val = sum([abs(v) / 100 for v in accelerometer.get_values()])
			self.speed += val
    
	def slow(self):
		self.speed -= 10

	def get_speed(self):
		if self.speed <= 5:
			self.speed = 5
		return self.speed

	def refresh_matrix(self):
		display.show(getattr(Image, "CLOCK" + str(self.i)))
		self.i += 1
		if self.i > 12:
			self.i = 1


c = color.next_color()

wheel = Wheel()

led = 0
frame = 0

while True:
    wheel.shake()
    wheel.color.check_change_color()
    wheel.next_led()
    if wheel.speed > 0:
        led += 1
        if i > 23:
            i = 0
        sleep(max(1000 - magnitude.m, 5))
        wheel.slow()