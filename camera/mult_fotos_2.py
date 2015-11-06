import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(10)
