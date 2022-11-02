#include <opencv2/opencv.hpp>
#include <iostream>
#include <time.h>
#include <string>

using namespace std;
using namespace cv;

// Read the video
VideoCapture cap("media/Touhou - Bad Apple.mp4");

// get how many frames are in the video
int total_frames = cap.get(CV_CAP_PROP_FRAME_COUNT);

// get the width and height of the video
int width = cap.get(CV_CAP_PROP_FRAME_WIDTH);
int height = cap.get(CV_CAP_PROP_FRAME_HEIGHT);

// export each frame of the video as a png
for (int i = 0; i < total_frames; ++i)
{
    bool ret = cap.read(frame);
    imwrite("media/badapple/frame{}.png", i, frame);
    sleep(0.001);
}

// release the video
cap.release();