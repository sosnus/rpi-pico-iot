import machine
import time
from machine import Pin, PWM
pwm = PWM(Pin(25))
# ADC0 = GPIO 26
adc = machine.ADC(0)
pwm.freq(1000)
while True:
    # read ADC
    a = adc.read_u16()
    # write value from ADC to PWM
    pwm.duty_u16(a)
    time.sleep_ms(10)
