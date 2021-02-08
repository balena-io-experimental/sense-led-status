import RPi.GPIO as GPIO
import requests
import json
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

GPIO.output(37, GPIO.LOW) #red
GPIO.output(35, GPIO.LOW) #yellow
GPIO.output(33, GPIO.LOW) #green

r = requests.get('http://sensor')
y = json.loads(r.text)
t = y["temperature"]

while True:
  if t < -1:
    print("LED status green.")
    GPIO.output(37, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(33, GPIO.HIGH)
  elif t > -1 and t < 1:
    print("LED status yellow.")
    GPIO.output(37, GPIO.LOW)
    GPIO.output(35, GPIO.HIGH)
    GPIO.output(33, GPIO.LOW)
  else:
    print("LED status red.")
    GPIO.output(37, GPIO.HIGH)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)

  time.sleep(30)
