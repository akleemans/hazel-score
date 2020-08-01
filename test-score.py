"""Classify test images

Reads the test images under test-images and calls score()
to see what class they are.
"""

from PIL import Image

from score import score

for i in range(1, 7):
    img = Image.open('test-images/img' + str(i) + '.jpg')
    result, msg = score(img)
    print(msg + '\n')
