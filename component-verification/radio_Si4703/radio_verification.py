from radio_module import Radio
from machine import I2C, Pin
import time


def main():
    def channel_info():
        channel = radio.GetChannel()
        channel_str = f'Channel: {channel*0.1} MHz'
        print(channel_str)

    radio = Radio(Pin(4, Pin.OUT), Pin(5, Pin.OUT), Pin(2, Pin.OUT))
    radio.Init()

    print('Information about radio module:')
    print(radio.printInfo())
    print('')

    channel_info()
    print('Changing radio channel...')
    radio.SetChannel(931)
    channel_info()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped. Exiting...")
        radio.ShutDown()


if __name__ == '__main__':
    main()