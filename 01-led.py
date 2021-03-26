from machine import Pin 
led = Pin(25, Pin.OUT) 
import time 
while True: 
  led.value(1) 
  time.sleep_ms(500) 
  led.value(0) 
  time.sleep_ms(500)
