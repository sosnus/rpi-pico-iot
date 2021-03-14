# 1. Test Rpi - blink

```python
# import
from machine import Pin
# create object
led = Pin(25, Pin.OUT)

# set value
led.value(1)

led.value(0)
```
