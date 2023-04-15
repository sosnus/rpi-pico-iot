import machine
import time
import bme280
# bme280 lib source: https://github.com/SebastianRoll/mpy_bme280_esp8266

i2c = machine.I2C(scl=machine.Pin(1), sda=machine.Pin(0), id=0)

while True:
    bme = bme280.BME280(i2c=i2c)
    print(bme.values)
    time.sleep(3)
