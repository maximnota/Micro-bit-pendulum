from microbit import *
from math import *
import time

def forward_backward_graph():
    time.sleep(1)
    display.clear()
    while True:
        a = accelerometer.get_values()
        phi = atan2(a[0], a[2])
        degrees_phi = degrees(phi)
        print(degrees_phi)
        sleep(100)
        if button_a.is_pressed() or button_b.is_pressed():
            break

def side_to_side_graph():
    time.sleep(1)
    display.clear()
    while True:
        a = accelerometer.get_values()
        theta = atan2(a[1], a[2])
        degrees_theta = degrees(theta)
        print(degrees_theta)
        sleep(100)
        if button_a.is_pressed() or button_b.is_pressed():
            break


display.scroll("A for X, B for Y")

while True:
    if button_a.is_pressed():
        display.show("X")
        forward_backward_graph()
    elif button_b.is_pressed():
        display.show("Y")
        side_to_side_graph()
    else:
        display.clear()

    