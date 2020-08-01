"""Take a test image

Using the camera module, initialize the camera and take a test image with the
current date as file name.
"""
import time

from picamera import PiCamera

camera = PiCamera()
date = time.strftime('%Y-%m-%d_%H-%M-%S')
camera.capture('./img/' + date + '.jpg')
