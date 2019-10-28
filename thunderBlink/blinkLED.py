from machine import Pin
import time

# 主控绿色指示灯闪烁
def ledBlink(interval=0.5):
    LED = Pin(2, Pin.OUT)
    while True:
        LED.on()
        time.sleep(interval)
        LED.off()
        time.sleep(interval)

if __name__ == "__main__":
    print("LED is blinking（绿灯正在闪烁）...")
    ledBlink()
else:
    print(__name__ + " module is included!!!")
