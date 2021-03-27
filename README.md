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

## Maqueen and Waveshare Joystick

This project is split into two .hex files as it was designed using makecode.microbit.org platform instead of standard Python. This was dictated by the fact that there are no (easily accessible) python libraries for both: [Maqueen robot](https://wiki.dfrobot.com/micro_Maqueen_for_micro_bit_SKU_ROB0148-E) and [WaveShare Joystick](https://www.waveshare.com/wiki/Joystick_for_micro:bit).

#### Waveshare_joypad_for_Maqueen.hex

This file contains code for the joypad. In short: Gathers information about analog input, recalculates it into 8 directions and sends them via radio. The rest of the buttons are used to change icons on the 5x5 LED matrix on the Maqueen Micro:Bit, change RGB LED colors or switch front red LEDs on and off.

- Analog input - drives Maqueen robot
- Analog press - turn front LEDs on/off
- Button A - Changes RGB LEDs (previous color) on the Maqueen
- Button B - Changes RBG LEDs (next color) on the Maqueen
- Button C - Shows surprised emote on both Joypad and Maqueen
- Button D - Shows sad emote on both devices
- Button E - Shows Happy emote on both devies
- Button F - Shows heart on both devies

#### Maqueen_for_Waveshare_Pad.hex

This file contains code for the Maqueen robot. Receives information via radio and translates them into proper activities: driving, LED control, dot matrix changes.

Idea for this project was to create a dedicated toy for my daughter Lucy, that no other kid has. Designed with love :-)
