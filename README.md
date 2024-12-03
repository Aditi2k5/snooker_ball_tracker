 # Snooker Ball Tracker

This project tracks snooker balls in a video using OpenCV. It is a basic model which focuses on detecting and tracking blue snooker balls. 
## Setup Instructions

### 1. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```
### 2. Install required packages
Install packages open-cv and numpy as mentioned in requirements.txt using command pip install -r requirements.txt

### 3. Snooker Video
The video data used in the code is snooker.mp4 which is a video having top view of a snooker table present in data directory of the repository.

### 4. Running the file
To run the python file tracker.py which has the code, use the command python scripts/tracker.py

This script processes the video frame by frame, converts each frame to the HSV color space, creates a mask for the blue color, finds contours in the mask, and draws bounding boxes around the detected balls. The main function to be considered here is process_video() which performs the necessary actions required for the code to run as intended to track the snooker ball.
