from machine import Pin
from radio_module import Radio
from machine import I2C, Pin


def main():
    # i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)
    radio = Radio(Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(2, Pin.OUT))
    radio.Init()
    radio.printInfo()
    radio.ShutDown()


if __name__ == '__main__':
    main()