import time
import picamera


for c in "teste":
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0.1)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(0.2)
    
