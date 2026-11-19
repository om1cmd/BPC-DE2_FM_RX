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

    # set according to your country bandplan
    minimum_frequency = 87.5   # minumum tunable frequency in MHz (lowest supported value is 76)
    maximum_frequency = 108  # maximum tunable frequency in MHz (highest supported value is 108)

    encoder = RotaryIRQ(pin_num_clk=12,
                        pin_num_dt=3,
                        min_val=int(minimum_frequency*10),
                        max_val=int(maximum_frequency*10),
                        reverse=False,
                        half_step=True,
                        range_mode=RotaryIRQ.RANGE_WRAP)

    encoder.add_listener(encoder_handler)

    try:
        while True:
            global encoder_changed_value
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