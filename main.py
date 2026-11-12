from radio_module import Radio
from machine import I2C, Pin
import time


def main():
    radio = Radio(Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(2, Pin.OUT))
    radio.Init()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        radio.ShutDown()


if __name__ == '__main__':
    main()