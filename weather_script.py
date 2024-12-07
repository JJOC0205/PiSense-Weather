#!/usr/bin/python
from sense_hat import SenseHat
import time
import sys

sense = SenseHat()

def main():
    while True:
        command = input("Temperature, Humidity, or Exit:")
        if command == "Temperature":
            print("Temperature: %s C" % sense.get_temperature())
            sense.show_message("Temperature: %s C" % sense.get_temperature())
        elif command == "Humidity":
            print("Humidity: %s %%rH" % sense.get_humidity())
            sense.show_message("Humidity: %s %%rH" % sense.get_humidity())
        elif command == "Exit":
            sys.exit()
        else:
            print("Invalid command")


if __name == "main":
    main()