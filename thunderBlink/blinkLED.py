from machine import Pin
import time

def ledBlink(interval=0.5):
    LED = Pin(2, Pin.OUT)
    while True:
        LED.on()
        time.sleep(interval)
        LED.off()
        time.sleep(interval)

if __name__ == "__main__":
    print("LED is blinking...")
    ledBlink()
else:
    print(__name__ + " module is included!!!")
