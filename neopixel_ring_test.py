from microbit import *
import neopixel
import random

np = neopixel.NeoPixel(pin2, 24)

i = 0
class Colors():
	def __init__(self):
		self.r = 0
		self.g = 0
		self.b = 0

	def color(self):
		return (self.r, self.g, self.b)
		
	def __iter__(self):
	    while True:
    		while self.r < 255:		# add red
    			self.r += 1
    			yield self.color()
    		while self.b > 0:		# remove blue
    			self.b -= 1
    			yield self.color()
    		while self.g < 255:		# add green
    			self.g += 1
    			yield self.color()
    		while self.r > 0:		# remove red
    			self.r -= 1
    			yield self.color()
    		while self.b < 255:		# add blue
    			self.b += 1
    			yield self.color()
    		while self.g > 0:		# remove green
    			self.g -= 1
    			yield self.color()

colors = Colors()
display.show(Image.HEART)
while True:
    for c in colors:
        np[i] = c
        np.show()
        i += 1
    	if i > 23:
    		i = 0
    	sleep(100)
    	#np.clear()