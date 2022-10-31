from machine import Pin, I2C
from time import sleep
import BME280

## I2C INIT
sda = machine.Pin(0)  # GP_0
scl = machine.Pin(1)  # GP_1
i2c = machine.I2C(0, sda=sda, scl=scl, freq=100000)

while True:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  # uncomment for temperature in Fahrenheit
  #temp = (bme.read_temperature()/100) * (9/5) + 32
  #temp = str(round(temp, 2)) + 'F'
  print('Temperature: ', temp)
  print('Humidity: ', hum)
  print('Pressure: ', pres)

  sleep(5)