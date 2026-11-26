from radio_module import Radio
from machine import I2C, Pin, Timer
from rotary_irq_rp2 import RotaryIRQ
from sh1106 import SH1106_I2C
import time


screen_refresh_due = False
encoder_changed_value = False

def encoder_handler():
    global encoder_changed_value
    encoder_changed_value = True


def timer_handler(timer):
    global screen_refresh_due
    screen_refresh_due = True


def oled_draw(oled, frequency):
    oled.fill(0)
    oled.text('Frequency', 0, 0)
    oled.text(f'{frequency/10} MHz', 0, 12)
    oled.text('RDS will be here', 0, 34)
    oled.show()


def main():
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100_000)

    radio = Radio(i2c, Pin(22, Pin.OUT))
    radio.Init()

    oled = SH1106_I2C(i2c)

    timer = Timer(-1)
    timer.init(period=100,
               mode=Timer.PERIODIC,
               callback=timer_handler)

    # set according to your country bandplan
    minimum_frequency = 87.5   # minumum tunable frequency in MHz (lowest supported value is 76)
    maximum_frequency = 108    # maximum tunable frequency in MHz (highest supported value is 108)

    encoder = RotaryIRQ(pin_num_clk=12,
                        pin_num_dt=3,
                        min_val=int(minimum_frequency*10),
                        max_val=int(maximum_frequency*10),
                        reverse=False,
                        half_step=True,
                        range_mode=RotaryIRQ.RANGE_WRAP)

    encoder.add_listener(encoder_handler)

    frequency = radio.GetChannel()
    oled_draw(oled, frequency)

    try:
        while True:

            global encoder_changed_value
            global screen_refresh_due

            if encoder_changed_value:
                frequency = encoder.value()
                radio.SetChannel(frequency)
                oled_draw(oled, frequency)

                encoder_changed_value = False

            if screen_refresh_due:
                frequency = encoder.value()
                oled_draw(oled, frequency)

                screen_refresh_due = False

            time.sleep_ms(10)

    except KeyboardInterrupt:
        print('\nProgram stopped. Exiting...')
        oled.fill(0)
        oled.show()
        oled.poweroff()
        timer.deinit()
        radio.ShutDown()


if __name__ == '__main__':
    main()