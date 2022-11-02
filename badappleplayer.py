import cv2
import time

cv = cv2  # alias

black = (0, 0, 0)
white = (255, 255, 255)

# create a new window
cv.namedWindow('Bad Apple', cv.WINDOW_NORMAL)

# Read the video
cap = cv.VideoCapture('media/Touhou - Bad Apple.mp4')

# get how many frames are in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# get the width and height of the video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# set the window size
cv.resizeWindow('Bad Apple', width, height)

# wait for key press
cv.waitKey(0)

for i in range(total_frames):
    # open image from file
    img = cv.imread('media/badapple/frame{}.png'.format(i))
    # convert image to text
    text = ''
    for y in range(height):
        for x in range(width):
            if img[y, x].all() == black:
                text += ' '
            else:
                text += '█'
        text += ""

    # display text
    cv.putText(img, text, (0, 0), cv.FONT_HERSHEY_SIMPLEX, 1, white)
    time.sleep(60 / 1000)
