import RPi.GPIO as GPIO
import time

# Global Variables
led_on = False
count = 0

#Initiallizing the the pins that will control the light and button
def setup_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# flashLED function makes sure that everything is ready to go.
def flash_LED(count):
    for i in range(count):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.2)

#Turns the light on and off
def switch(ev=None):
    global led_on, count
    led_on = not led_on
    count += 1

    if led_on == True:
        print("Turning On\tcount: " + str(count))
        GPIO.output(18, GPIO.HIGH)
    else:
        print("Turning Off\tcount: " + str(count))
        GPIO.output(18, GPIO.LOW)

#Listens for button presses, buy checking the voltage on pin 23
def detect_button_press():
    GPIO.add_event_detect(23, GPIO.FALLING, callback=switch, bouncetime=300)

#Keeps the program running even if no one is hitting buttons
def wait_for_events():
    while True:
        time.sleep(1)


#Running the Functions
setup_GPIO()
flash_LED(5)
detect_button_press()

wait_for_events()
