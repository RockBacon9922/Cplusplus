import cv2
import time
import numpy as np

cv = cv2  # alias

# Read the video
cap = cv.VideoCapture('media/Touhou - Bad Apple.mp4')

# get how many frames are in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# get the width and height of the video

usr = input("Enter the scale percent of the video: ")
try:
    scale_percent = int(usr)  # percent of original size
    if scale_percent > 100 or scale_percent < 0:
        scale_percent = 12
except:
    scale_percent = 12
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) * scale_percent / 100)  # 480
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) * scale_percent / 100)  # 360
# get frame rate
fps = cap.get(cv.CAP_PROP_FPS)

# define black and white
black = [0, 0, 0]
white = [255, 255, 255]

# delete everything in the console then convert the video to text the print the text
for i in range(total_frames):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    # convert image to text
    text = ''
    for y in range(height):
        for x in range(width):
            if frame[y, x].sum() >= 200 * 3:
                text += '🍏'
            else:
                text += '🍎'
        text += "\n"
    # display text
    print(text)
    time.sleep(fps / 1000)
