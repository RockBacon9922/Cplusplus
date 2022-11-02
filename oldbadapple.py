import cv2
import time

cv = cv2  # alias

# Read the video
cap = cv.VideoCapture('media/Touhou - Bad Apple.mp4')

# get how many frames are in the video
total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

# get the width and height of the video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# export each frame of the video as a png
for i in range(total_frames):
    ret, frame = cap.read()
    cv.imwrite('media/oldbadapple/frame{}.png'.format(i), frame)
    time.sleep(0.001)


# release the video
cap.release()
