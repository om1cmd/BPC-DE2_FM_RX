from machine import I2C, Pin
from sh1106 import SH1106_I2C
import time


def main():
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)
    oled = SH1106_I2C(i2c)

    oled.fill(0)
    oled.text("Frequency", 0, 0)
    oled.text("... MHz", 0, 12)
    oled.text("RDS will be here", 0, 34)
    oled.show()

    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        oled.fill(0)
        oled.show()
        oled.poweroff()

if __name__ == "__main__":
    main()