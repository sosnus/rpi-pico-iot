"""
MicroPython/Pyboard exercise
display on 0.96" 128x64 SSD1315 I2C OLED.

"""
import sys
import os
import time
import ssd1306
import framebuf

print("====================================")
print(sys.implementation[0], os.uname()[3],
      "\nrun on", os.uname()[4])
print("====================================")

oled_i2c = machine.I2C(2)
print("Default I2C(2):", oled_i2c)

DISP_WIDTH=128
DISP_HEIGHT=64

# Raspberry Pi logo as 32x32 bytearray
fb_width=32
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

def demo():

    oled.fill(0)
    oled.rect(0, 0, DISP_WIDTH, DISP_HEIGHT, 1)
    oled.text('Hello coXXect', 5, 5, 1)
    oled.text('SSD1315 OLED', 5, 15, 1)
    oled.text('comp.to SSD1306', 5, 25, 1)
    oled.show()
    time.sleep(2)

    oled.blit(fb, DISP_WIDTH-fb_width, 32)
    oled.show()
    time.sleep(1)
    
    for i in range(DISP_WIDTH-fb_width, 0-1, -1):
        oled.blit(fb, i, 32)
        oled.show()
        time.sleep(0.05)

oled = ssd1306.SSD1306_I2C(DISP_WIDTH, DISP_HEIGHT, oled_i2c)
print("Default SSD1306 I2C address:",
      oled.addr, "/", hex(oled.addr))
    
#oled.rotate(False)
oled.invert(0)
oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
time.sleep(1)
    
demo()
#oled.rotate(True)
oled.invert(1)
demo()
time.sleep(1)
    
oled.invert(0)
time.sleep(1)
    
#oled.rotate(False)
oled.invert(0)
oled.fill(0)
    
step_width = fb_width+2
for i in range(0, DISP_WIDTH, step_width):
    oled.blit(fb, i, 32)
    oled.show()
    time.sleep(0.5)

print("~ bye ~")
