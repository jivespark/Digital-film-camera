import time
import signal
import sys
from gpiozero import Button
from camera import Camera
from buzzer import startup_sound, shutter_sound, error_sound, low_storage_sound
from storage import setup_storage, next_filename, low_storage

shutter_pin=17

is_capturing=False

print("Starting camera...")
setup_storage()
cam=Camera()
shutter=Button(shutter_pin, bounce_time=0.05)

def take_photo():
    global is_capturing

    if is_capturing:
        return
    
    if low_storage():
        low_storage_sound()
        print("Warning: low storage")
        return
    
    is_capturing=True

    try:
        filepath=next_filename
        print(f"Capturing {filepath}...")
        shutter_sound()
        cam.capture(filepath)
    except Exception as e:
        print(f"Capture error: {e}")
        error_sound()
    finally:
        is_capturing=False

def shutdown(sig, frame):
    print("Shutting down...")
    cam.stop()
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

startup_sound()
print("Camera ready")

shutter.when_pressed=take_photo
signal.pause()