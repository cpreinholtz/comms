import keyboard
import time

ctrl = "0123456789"
while True:
  for c in ctrl:
#    print("testing: "+c)
    if keyboard.is_pressed(c):
      print ("sending:  "+c)
  time.sleep(0.1)
