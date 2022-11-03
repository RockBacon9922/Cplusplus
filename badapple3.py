import cv2
import time
import numpy as np
import threading
import fpstimer
import moviepy.editor as mp
import pygame

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
# create timer
timer = fpstimer.FPSTimer(fps)

# define black and white
black = [0, 0, 0]
white = [255, 255, 255]

# create a function


def textvideo():
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
        timer.sleep()

# create a function which makes the video play in a window


def video():
    cap = cv2.VideoCapture('media/Touhou - Bad Apple.mp4')
    success, video_image = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)

    window = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    textThread.start()
    audio.start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        success, video_image = cap.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    exit()


# create an audio track from the video
mp.VideoFileClip(
    'media/Touhou - Bad Apple.mp4').audio.write_audiofile('media/audio.mp3')

# create a audio playback function


def audioplayback(path):
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()


# create a thread for audio playback
audio = threading.Thread(target=audioplayback, args=('media/audio.mp3',))

# create a thread but make thread daemon
textThread = threading.Thread(target=textvideo)
videoThread = threading.Thread(target=video)
# start the thread
# textvideo()
# textThread.start()
# audio.start()
video()
