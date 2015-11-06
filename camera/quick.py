import time
import picamera
camera = picamera.PiCamera()

x = 0
while(x<=10):
    x += 1

    try:
            camera.start_preview()
            time.sleep(10)
            camera.capture('image.jpg')
            camera.stop_preview()
            
