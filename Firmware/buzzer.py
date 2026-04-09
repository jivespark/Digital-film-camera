import lgpio
import time

buzzer_pin=22
h=lgpio.gpiochip_open(0)

def beep(frequency=2000, duration=0.05):
    lgpio.tx_pwm(h, buzzer_pin, frequency, 50)
    time.sleep(duration)
    lgpio.tx_pwm(h, buzzer_pin, 0, 0)

def startup_sound():
    beep(1000, 0.1)
    time.sleep(0.05)
    beep(1500, 0.1)
    time.sleep(0.05)
    beep(2000, 0.15)

def shutter_sound():
    beep(2500, 0.02)

def error_sound():
    beep(500, 0.3)
    time.sleep(0.1)
    beep(500, 0.3)

def low_storage_sound():
    beep(800, 0.1)
    time.sleep(0.05)
    beep(800, 0.1)