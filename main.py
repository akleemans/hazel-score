"""Main script

Take a picture every few seconds and run the score function on it, then
show the results on the display.
"""
import io
import time

from PIL import Image
from picamera import PiCamera

import display
import score

camera = PiCamera()
camera.start_preview()
time.sleep(2)

while True:
    print('Taking picture...')
    start_time = time.time()

    # Variant with saving the image to file
    # camera.capture('/home/pi/hazel-score/img/test.jpg')
    # Read from file
    # result, msg = score.score(Image.open('img/test.jpg'))

    # Create the in-memory stream
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    # rewind the stream to the beginning so we can read its content
    stream.seek(0)
    image = Image.open(stream)

    print('Done taking picture in', time.time() - start_time, 's')
    time.sleep(1)

    start_time = time.time()
    result, msg = score.score(image)

    print('Done calculating score in', time.time() - start_time, 's')

    display.display(msg)
    time.sleep(3)
