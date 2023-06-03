# script that takes a YouTube playlist link and takes a snapshot of each video in the playlist every 10 seconds:
# pip install pytube opencv-python

# change directory,playlist link


import os
import pytube
import cv2

playlist_link = "https://www.youtube.com/playlist?list=PLojRVMfz8TPPwgDWTVcWkFHziCL3KZHfc"

# Create a folder to save the snapshots
if not os.path.exists("snapshots"):
    os.mkdir("snapshots")

# Get the playlist
yt = pytube.YouTube(playlist_link)
playlist = yt.playlist

# Iterate over each video in the playlist
for video in playlist:
    # Download the video
    video.download()

    # Open the video with OpenCV
    cap = cv2.VideoCapture(video.title)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Take a snapshot every 10 seconds
    for i in range(0, total_frames, int(cap.get(cv2.CAP_PROP_FPS)) * 10):
        cap.set(1, i)
        ret, frame = cap.read()

        # Save the snapshot as a JPEG image in the "snapshots" folder
        cv2.imwrite(f"snapshots/snapshot_{i}.jpg", frame)
