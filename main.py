from radio_module import Radio
from machine import I2C, Pin
from rotary_irq_rp2 import RotaryIRQ
import time


encoder_changed_value = False


def encoder_handler():
    global encoder_changed_value
    encoder_changed_value = True


def main():
    radio = Radio(Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(22, Pin.OUT))
    radio.Init()

    encoder = RotaryIRQ(pin_num_clk=12, pin_num_dt=3, min_val=870, max_val=1080, reverse=False, half_step=True, range_mode=RotaryIRQ.RANGE_WRAP)
    encoder.add_listener(encoder_handler)

    try:
        while True:
            if encoder_changed_value:
                frequency = encoder.value()
                radio.SetChannel(frequency)
                encoder_changed_value = False
                print(frequency)
            time.sleep_ms(100)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        radio.ShutDown()


if __name__ == '__main__':
    main()