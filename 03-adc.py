### V1 simple
"""
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
"""

### V2 voltage
# """
import machine
import time
from machine import Pin, PWM
adc = machine.ADC(1) # ADC0 = GPIO 27
vref = 3.3
div = 2.0
while True:
    # read ADC
    rawAdc = adc.read_u16()
    voltage = div * vref * (rawAdc/65535.0)
    # print(voltage)
    print("U= " +str(voltage)+" V")
    time.sleep_ms(10)
# """