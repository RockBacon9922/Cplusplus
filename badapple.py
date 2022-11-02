import cv2
import time
import numpy as np

cv = cv2  # alias

# Read the video
cap = cv.VideoCapture('media/Touhou - Bad Apple.mp4')

# get how many frames are in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# get the width and height of the video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# define black and white
black = [0, 0, 0]
white = [255, 255, 255]

# create a blank frame to the size of the video
blankImg = np.zeros((height, width, 3), dtype=np.uint8)

# export blank image
cv.imwrite('media/badapple/blankimage.png', blankImg)

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# org
org = 1

spacing = 1
# fontScale
fontScale = 0.001

# Blue color in BGR
color = (255, 255, 255)

# Line thickness of 2 px
thickness = 1

frame = 0

# export each frame of the video as a png
for i in range(1235, total_frames):
    ret, frame = cap.read()
    blankImgCp = blankImg
    # convert frame into a text image
    for y in range(height):
        text = ''
        for x in range(width):
            if frame[y, x].sum() >= 254 * 3:
                text += '.'
            else:
                text += '@'
        image = cv2.putText(blankImgCp, text, (0, org + (spacing*y)), font,
                            fontScale, color, thickness)
    # write text to blank image
    # export image
    cv.imwrite('media/badapple/frame{}.png'.format(i), blankImg)
    frame += 1


# release the video
cap.release()
