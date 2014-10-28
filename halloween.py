#!/usr/bin/python

import time
import datetime
from Adafruit_7Segment import SevenSegment

# ===========================================================================
# Countdown
# ===========================================================================
segment = SevenSegment(address=0x70)

print "Press CTRL+Z to exit"

countdown = 60 * 20 # 20 minutes
ticks = 12

current = countdown
current_tick = ticks

# Continually update the time on a 4 char, 7-segment display
while(True):   
  # if there is no blinkin 0 and the time is up
  # return to the start
  if (current == 0 and current_tick == 0):
      current = countdown
      current_tick = ticks
      
  # When the countdown is a 0, blink between zeros and eights
  if (current == 0 and current_tick % 2):
      minute = 88
      second = 88      

  # or simply show the time
  else:       
      minute = current / 60
      second = current % 60
  
  # Set minutes
  segment.writeDigit(0, int(minute / 10))     # Tens
  segment.writeDigit(1, minute % 10)          # Ones
  
  # Set seconds
  segment.writeDigit(3, int(second / 10))   # Tens
  segment.writeDigit(4, second % 10)        # Ones
  
  # Toggle colon
  segment.setColon(second % 2)              # Toggle colon at 1Hz
  
  # while the countdown is still 
  # running, decrement and wait 1 sec
  if (current > 0):
      current -= 1
      time.sleep(1)
      
  # when the countdown is done, decrement ticks
  # but sleep only .2 secs
  else:
      current_tick -= 1
      time.sleep(.2)
