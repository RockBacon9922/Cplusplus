import cv2
import time
import numpy as np

cv = cv2  # alias

# Read the video
cap = cv.VideoCapture('media/Touhou - Bad Apple.mp4')

# get how many frames are in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# get the width and height of the video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))  # 480
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))  # 360

# define black and white
black = [0, 0, 0]
white = [255, 255, 255]

# delete everything in the console then convert the video to text the print the text
print(chr(27) + "[2J")
for i in range(total_frames):
    ret, frame = cap.read()
    # convert image to text
    text = ''
    for y in range(height):
        for x in range(width):
            if frame[y, x].sum() >= 254 * 3:
                text += '🍏'
            else:
                text += '🍎'
        text += "\n"
    # display text
    print(text)
    time.sleep(60 / 1000)
