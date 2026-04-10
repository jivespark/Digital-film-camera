**Firmaware instructions:**

This firmware is meant to be used on the raspberry pi. For the pi you should install the Raspberry pi os lite, and I also recommend enableing ssh to be able to run it headless. Also make sure that the camera interface is enabled.

Libraries to install:  
Picamera2, system packages:  
`sudo apt install -y python3-pip python3-picamera2 libcamera-apps`
Python libraries:  
`pip install lgpio gpiozero --break-system-packages`