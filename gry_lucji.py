import random
from microbit import Image, display, pin1, pin2, pin8, pin12, pin13, pin14, pin15, button_a, button_b, accelerometer, sleep
import music


class DiceStandard():
    def __init__(self):
        self.roll()

    def roll(self):
        self.num = random.choice(list(self.sides.keys()))
        return self.sides[self.num]
     
    def melody(self):
        return self.melodies[self.num]

    sides = {
        '1': Image(
            "00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000"
        ),
        '2': Image(
            "90000:"
            "00000:"
            "00000:"
            "00000:"
            "00009"
        ),
        '3': Image(
            "90000:"
            "00000:"
            "00900:"
            "00000:"
            "00009"
        ),
        '4': Image(
            "90009:"
            "00000:"
            "00000:"
            "00000:"
            "90009"
        ),
        '5': Image(
            "90009:"
            "00000:"
            "00900:"
            "00000:"
            "90009"
        ),
        '6': Image(
            "90009:"
            "00000:"
            "90009:"
            "00000:"
            "90009"
        )
    }
    
    melodies = {
        '1': ["C4:2"],
        '2': ["C4:2", "D4:2"],
        '3': ["C4:2", "D4:2", "E4:2"],
        '4': ["C4:2", "D4:2", "E4:2", "F4:2"],
        '5': ["C4:2", "D4:2", "E4:2", "F4:2", "G4:2"],
        '6': ["C4:2", "D4:2", "E4:2", "F4:2", "G4:2", "A4:2"]
    }


class game_a():
    def play(self):
        p1 = pin1.read_analog()
        p2 = pin2.read_analog()
        if p1 <= 300:
            if p2 < 300:
                display.show(Image.ARROW_SW)
            elif p2 >= 900:
                display.show(Image.ARROW_NW)
            else:
                display.show(Image.ARROW_W)
        elif p1 >= 900:
            if p2 < 300:
                display.show(Image.ARROW_SE)
            elif p2 >= 900:
                display.show(Image.ARROW_NE)
            else:
                display.show(Image.ARROW_E)
        elif 300 < p1 < 900:
            if p2 < 300:
                display.show(Image.ARROW_S)
            elif p2 >= 900:
                display.show(Image.ARROW_N)
            else:
                if not pin15.read_digital():
                    display.show(Image.HAPPY)
                    music.play(music.JUMP_UP)
                elif not pin14.read_digital():
                    display.show(Image.SURPRISED)
                    music.play(music.POWER_UP)
                elif not pin13.read_digital():
                    display.show(Image.SAD)
                    music.play(music.JUMP_DOWN)
                elif not pin12.read_digital():
                    display.show(Image.ASLEEP)
                    music.play(music.POWER_DOWN)
                elif not pin8.read_digital():
                    display.show(Image.HEART)
                    music.play(["C1:1", "C#1:1"])

        display.clear()
        
        
class game_b():
    valid_choices = [0, 1, 3, 4]
    def __init__(self):
        self.pix = None

    def set_random_pix(self):
        self.pix = [random.choice(self.valid_choices), random.choice(self.valid_choices), 9]

    def play(self):
        if self.pix:
            self.logic()
        else:
            self.set_random_pix()           

    def logic(self):
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

        display.set_pixel(*self.pix)
        display.set_pixel(x,y,9)
        
        if [x, y, 9] == self.pix:
            self.pix = None
            display.show(Image.HAPPY)
            music.play(music.JUMP_UP)
            sleep(500)
        if self.btn_pressed():
            sleep(150)
            self.set_random_pix()

    def btn_pressed(self):
        return not pin15.read_digital() or not pin14.read_digital() or not pin13.read_digital() or not pin12.read_digital() or not pin8.read_digital()
            
def game_shake():
    if accelerometer.was_gesture("shake"):
        for w in shake_waits:
            display.clear()
            sleep(50)
            rolled = dice.roll()
            display.show(rolled)
            music.play(["C4:1"], wait=False)
            sleep(w)
        music.play(dice.melody(), wait=False)
        for i in range(4):
            display.clear()
            sleep(500)
            display.show(rolled)
            sleep(500)

### MAIN LOOP ###
shake_waits = [
    10, 10, 10, 10, 10,
    10, 20, 40, 60, 80,
    100, 120, 140, 160, 180,
    200, 250, 300, 400, 500
]
current_game = game_a()
dice = DiceStandard()

while True:
    game_shake()
    if button_a.get_presses():
        current_game = game_a()
        display.show("A")
        sleep(500)
    if button_b.get_presses():
        current_game = game_b()
        display.show("B")
        sleep(500)
    current_game.play()
