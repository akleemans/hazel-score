"""Communicate with the Adafruit display

Show a message on the 2-line display. If run as a script,
it will show a test message.
"""
import time

import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, 16, 2)
lcd.backlight = True


def display(msg):
    lcd.clear()
    lcd.message = msg


if __name__ == '__main__':
    # Show test message on display
    display("Display test!\nIndex = 23")
    time.sleep(5)
    display("Display update!\nIndex = 2045")
