from machine import Pin
from radio_module import Radio
from machine import I2C, Pin


def main():
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)
    # radio = Radio(i2c, Pin(2))
    # radio.Init()
    print(i2c.scan())


if __name__ == '__main__':
    main()