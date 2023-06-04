# script to download all the youtube videos given as links in a text file. the decreasing preference order of video quality should be 720p,480p,360p,250p. that is , if 720p not found, then 480p, if 480p not found then 360p likewise

# give the link file,install pytube

import os
import pytube

# Specify the video quality preference order
quality_order = ["720p", "480p", "360p", "240p"]

# Create a new folder to store the downloaded videos
if not os.path.exists("linkvideos"):
    os.mkdir("linkvideos")

# Read the text file containing the video links
with open("video_links.txt", "r") as f:
    links = f.readlines()

# Iterate through the links and download the videos
for link in links:
    link = link.strip()  # remove leading/trailing white space
    video = pytube.YouTube(link)
    print(f"Download started for {video.title}.")
    for quality in quality_order:
        try:
            video_stream = video.streams.filter(resolution=quality).first()
            video_stream.download(output_path='linkvideos')
            print(f"Successfully downloaded {video.title} in {quality} quality.")
            break
        except:
            pass

