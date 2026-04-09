from picamera2 import Picamera2
import time

class Camera:
    def __init__(self):
        self.cam=Picamera2()
        self.ev=0.0
        self.ready=False
        self._setup()
    
    def _setup(self):
        config=self.cam.create_still_configuration(
            main={"size": (4608, 2592)},
            raw={"size": (4608, 2592)}
        )
        self.cam.configure(config)
        self.cam.set_controls({
            "AeEnable":True,
            "ExposureValue":self.ev,
            "AwbEnable": True,
        })
        self.cam.start()
        time.sleep(2)
        self.ready=True
    
    def capture(self, filepath):
        if(self.ready):
            self.ready=False
            self.cam.capture_file(filepath, name="raw")
            self.ready=True
    
    def stop(self):
        self.cam.stop()