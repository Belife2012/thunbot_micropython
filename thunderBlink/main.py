import _thread
import blinkLED

_thread.start_new_thread(blinkLED.ledBlink, ())
