import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

def Blink():
  for i in range(0,3):
    print "blink #" +str(i+1)
    GPIO.output(23,True)
    time.sleep(1)
    GPIO.output(23,False)
    time.sleep(1)
  print "done!!"
  GPIO.cleanup()
Blink()
