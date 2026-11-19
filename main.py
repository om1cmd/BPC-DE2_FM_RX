from radio_module import Radio
from machine import I2C, Pin
from rotary_irq_rp2 import RotaryIRQ
import time


def main():
    radio = Radio(Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(22, Pin.OUT))
    radio.Init()

    encoder = RotaryIRQ(pin_num_clk=12, pin_num_dt=3, min_val=870, max_val=1080, reverse=False, half_step=True, range_mode=RotaryIRQ.RANGE_WRAP)

    try:
        while True:
            print(encoder.value())
            time.sleep_ms(20)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        radio.ShutDown()


if __name__ == '__main__':
    main()