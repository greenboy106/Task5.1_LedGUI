from tkinter import *
import tkinter.font
from gpiozero import LED
from functools import partial

# Safe and clean GPIO choices
led_red = LED(14)
led_green = LED(15)
led_blue = LED(18)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

def toggle_led(led, button):
    if led.is_lit:
        led.off()
        button["text"] = f"Turn {button['bg']} LED On"
    else:
        led.on()
        button["text"] = f"Turn {button['bg']} LED Off"

# Buttons
red_button = Button(win, text="Turn Red LED On", font=myFont, bg="Red")
green_button = Button(win, text="Turn Green LED On", font=myFont, bg="Green")
blue_button = Button(win, text="Turn Blue LED On", font=myFont, bg="Blue")

red_button.grid(row=0, column=1, padx=20, pady=10)
green_button.grid(row=1, column=1, padx=20, pady=10)
blue_button.grid(row=2, column=1, padx=20, pady=10)

# Bind toggle function
red_button.config(command=partial(toggle_led, led_red, red_button))
green_button.config(command=partial(toggle_led, led_green, green_button))
blue_button.config(command=partial(toggle_led, led_blue, blue_button))

exit_button = Button(win, text="Exit", font=myFont, command=win.destroy)
exit_button.grid(row=3, column=1, pady=20)

win.mainloop()
