from machine import I2C, Pin, UART
from ht16k33Matrix import HT16K33Matrix

uart = UART(2,115200)
uart.init(115200, bits=8, parity=None, stop=1)

i2c = I2C(scl=Pin(22), sda=Pin(21))
display = HT16K33Matrix(i2c)
display.set_brightness(10)
display.set_angle(0)

display.clear().draw()
display.set_character(ord('-'), True).draw()

ch=b''
while True:
    if uart.any() > 0:        
        ch = uart.readline()        
        display.clear().draw()
        display.set_character(ord(ch), True).draw()
            