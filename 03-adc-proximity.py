import machine
import time
from machine import Pin, PWM
adc = machine.ADC(0) # ADC0 = GPIO 27
vref = 3.3
div = 1.0
while True:
    # read ADC
    rawAdc = adc.read_u16()
    proximity = (rawAdc/65535.0) * 100.0
    # voltage = div * vref * (rawAdc/65535.0)
    # print(voltage)
    print("U= " +str(proximity)+" %")
    time.sleep_ms(10)