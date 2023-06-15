import network
import socket
import urequests as requests
import machine
import time
from machine import Pin, PWM
adc = machine.ADC(0)

# GLOBAL_VARIABLES
ssid = "YOUR-WIFI-SSID"
password = "YOUR-WIFI-PASSWORD"

wlan = None

def init():
    wlan = network.WLAN(network.STA_IF)
    connect_to_wifi(wlan,ssid, password)
    
def loop():
    while True:
        rawAdc = adc.read_u16()
        # convert ADC value to temperature
        # temp = (adcValue/maxAdcValue[65535])*
        #     *(voltage in mV [3.3V = 3300mV]/Sensor Chip Sensitivity: 10mV/℃ [10.24])
        temp=(rawAdc/65535.0)* 3300/10.24
        print("temp=",temp,"C")
        
        
        url = "http://srv18.mikr.us:40083/data"

        payload = [
            {
                "variable": "temperatureEmulator",
                "value": temp
            }
        ]
        headers = {
            "Content-Type": "application/json",
            "device-token": "74484bcb-923a-4a38-afaa-42cacd89f9fd"
        }

        r = requests.request("POST", url, json=payload, headers=headers)

        print("Response: ")
        print(r.text)
        r.close() # important!!!
        print("WAIT...")
        time.sleep_ms(3000)
      
def connect_to_wifi(wlan = None, ssid = "", password = ""):
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep_ms(1000)
    print("WiFi "+ ssid + " connected!")
    
init()
loop()

