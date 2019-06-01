# MicroBit
My Micro:Bit code and projects.

---

## gry_lucji.py (lucy's games)
A little project of simple games for my little daughter Lucy. It requires a WaveShare joystick module.

It consists of three games:

* On shaking, it starts to randomize a standard six-sided dice. After few seconds it stops randomizing, plays a tune and flashes final result.
* On clicking A button, switches to A game. It really just displays what just was pressed, with directional arrows on analog press and smiley faces on other buttons. Plays a tune on each button.
* On clicking B button, switches to B game.

## tony_stark_heart.py
This project is inspired by Iron Man and it's arc reactor. It requires a DFRobot circular RGB expansion board v2.0.

The 24 LEDs on the board light up in three modes:

* Mode 1: a strip of five leds, each 20% dimmer then the next, is circling around the shield. Pressing B button changes the color.
* Mode 2: is a slow pulsing of all shield LEDs, from 0 to max and then back. B button also changes colors.
* Mode 3: similar to mode 1, but the colors change automatically to show all colors of the rainbow in order.

Each mode is changed by pressing A button.

Modes 1 and 3 utilize the micro:bit's 5v5 led matrix to show a beating heart with animation and sound.

It's great for cosplaying Iron Man, or just geeking out in a t-shirt ;-)
