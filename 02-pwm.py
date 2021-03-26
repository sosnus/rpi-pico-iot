import time
from machine import Pin, PWM
#Construct PWM object, with LED on Pin(25).
pwm = PWM(Pin(25))
# Set the PWM frequency.
pwm.freq(1000)
while True:
    for i in range(256):
        pwm.duty_u16(i * i)
        time.sleep_ms(10)
