

"""
ESP32-S2 mini micropython 
with 320x240 ILI9341 SPI Display
"""
# Get error: cannot import ILI9341
# Using a try statement 'fixes' it...
import gc
gc.collect()
import ili934xnew
try:
  print('im trying')
  from ili934xnew import ILI9341, color565
except:
  print("Minor issue with ili934xnew")
#import ili934xnew
from machine import Pin, SPI
from micropython import const
import os
import time
import glcdfont
import fs8
import fs16



def df():
  s = os.statvfs('//')
  return ('{0} MB'.format((s[0]*s[3])/1048576))

def free(full=False):
  F = gc.mem_free()
  A = gc.mem_alloc()
  T = F+A
  P = '{0:.2f}%'.format(F/T*100)
  if not full: return P
  else : return ('Total:{0} Free:{1} ({2})'.format(T,F,P))

SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(3)
CENTER_Y = int(SCR_WIDTH/2)
CENTER_X = int(SCR_HEIGHT/2)

print(os.uname())
TFT_CLK_PIN = const(12)
TFT_MOSI_PIN = const(11)

TFT_MISO_PIN = const(4)

TFT_CS_PIN = const(7)
TFT_RST_PIN = const(5)
TFT_DC_PIN = const(9)


spi = SPI(
    1,
    baudrate=40000000,
    miso=Pin(TFT_MISO_PIN),
    mosi=Pin(TFT_MOSI_PIN),
    sck=Pin(TFT_CLK_PIN))
print(spi)

display = ILI9341(
    spi,
    cs=Pin(TFT_CS_PIN),
    dc=Pin(TFT_DC_PIN),
    rst=Pin(TFT_RST_PIN),
    w=SCR_WIDTH,
    h=SCR_HEIGHT,
    r=SCR_ROT)

display.erase()
display.set_pos(0,0)

p=[2,2,color565(255,255,0)]

#for x in range(200):
#  for y in range(200):

#    display.pixel(x,y,x+y)
print('Displaying Hello World')
display.set_font(fs16)
display.set_color(color565(255, 255, 255), color565(12, 12, 12))
display.print("Getting ili9341 to work!")
display.print('Memory free: '+ df() +' : ' + free())
gc.collect()
display.print('Memory free: '+ df() +' : ' + free())

#display.pixel(p[0],p[1],p[2])
    
time.sleep(1)
print('did stuff')



