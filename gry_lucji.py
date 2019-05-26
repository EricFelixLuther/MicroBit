import random
from microbit import *
import music


class DiceStandard():
    def __init__(self):
        self.roll()

    def roll(self):
        self.num = random.choice(list(self.sides.keys()))
        return self.sides[self.num]
        
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


dice_standard = DiceStandard()

class Main():
    def __init__(self):
        self.games = (
            self.game_1,
            self.game_2,
            self.game_3
        )
        self.current_game_index = 0
        self.current_game = self.games[self.current_game_index]

    def next_game(self):
        self.current_game_index += 1
        if self.current_game_index >= len(self.games):
            self.current_game_index = 0
        self.current_game = self.games[self.current_game_index]
    
    def game_1(self):
        # TODO Press selected button
        side = random.choice(('up', 'down', 'left', 'right'))
        if side == 'up':
            img = Image.ARROW_N
        elif side == 'down':
            img = Image.ARROW_S
        elif side == 'left':
            img = Image.ARROW_W
        else:
            img = Image.ARROW_E
        display.show(img)
        button_pressed = False
        while not button_pressed:
            if(side == 'up' and (pin2.read_analog() > 900 or not pin13.read_digital())) or \
                    (side == 'down' and (pin2.read_analog() < 300 or not pin15.read_digital())) or \
                    (side == 'left' and (pin1.read_analog() < 300 or not pin12.read_digital())) or \
                    (side == 'right' and (pin1.read_analog() > 900 or not pin14.read_digital())):
                display.show(Image.YES)
                music.play(music.JUMP_UP)
                button_pressed = True
            elif(side == 'up' and not (pin2.read_analog() > 900 or not pin13.read_digital())) or \
                    (side == 'down' and not (pin2.read_analog() < 300 or not pin15.read_digital())) or \
                    (side == 'left' and not (pin1.read_analog() < 300 or not pin12.read_digital())) or \
                    (side == 'right' and not (pin1.read_analog() > 900 or not pin14.read_digital())):
                display.show(Image.NO)
                music.play(music.JUMP_DOWN)
            else:
                display.show(img)

    def game_2(self):
        # Roll die
        if accelerometer.was_gesture("shake"):
            for i in range(10, 500, 10):
                display.clear()
                sleep(50)
                rolled = dice_standard.roll()
                display.show(rolled)
                music.play(["C4:1"], wait=False)
                sleep(i)
            music.play(music.PUNCHLINE, wait=False)
            for i in range(4):
                display.clear()
                sleep(500)
                display.show(rolled)
                sleep(500)
            

    def game_3(self):
        # Display images on buttons
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

### MAIN LOOP ###
games = Main()

while True:
    if button_a.get_presses():
        games.next_game()
    games.current_game()
