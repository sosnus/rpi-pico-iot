import machine, onewire, ds18x20, time
from time import sleep
from machine import Pin
from machine import PWM
pwm = PWM(Pin(0))
pwm.freq(50)


ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
temperature = 30
print('Found DS devices: ', roms)



def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)


while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
        temperature = ds_sensor.read_temp(rom)
    temperatureInt = int(temperature)
    if(temperatureInt < 20):
        setServoCycle(1000)
    elif(temperatureInt > 60):
        setServoCycle(9000)
    else:
        pos = (temperatureInt-20)*200+1000
        setServoCycle(pos)
    time.sleep(3)

