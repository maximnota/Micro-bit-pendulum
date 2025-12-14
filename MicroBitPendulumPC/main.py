import serial
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/tty.usbmodem2102', 115200)
data = []

while True:
    line = ser.readline().decode().strip()
    value = float(line)
    data.append(value)
    plt.clf()
    plt.plot(data)
    plt.pause(0.01)

