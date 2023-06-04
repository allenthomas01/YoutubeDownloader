import os
import pytube

# enter the YouTube playlist URL
PLAYLIST_URL = input("Enter the YouTube playlist URL: ")

# enter the start and end video numbers
START_VIDEO = int(input("Enter the start video number: "))
END_VIDEO = int(input("Enter the end video number: "))

# enter the output directory
output_dir = input("Enter the output directory: ")

# Create a PyTube playlist object
playlist = pytube.Playlist(PLAYLIST_URL)

# Get a list of all the video URLs in the playlist
video_urls = playlist.video_urls

# Iterate over the list of video URLs 
for url in video_urls[START_VIDEO - 1:END_VIDEO]:
    # Create a PyTube video object
    video = pytube.YouTube(url)

    try:
        # Get the video's title
        video_title = video.title
    except pytube.exceptions.PytubeError:
        # If error occurs, fallback title
        video_title = "Unknown_Title"

    # Print the video's title
    print(f"Downloading '{video_title}' ...")

    # Check if the output directory exists, and create it if it doesn't
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Try to get a 720p video stream
    video_stream = video.streams.get_highest_resolution()

    # If no 720p stream is available, try to get the highest resolution stream
    if video_stream is None:
        video_stream = video.streams.get_highest_resolution()

    # Download the video to the output directory
    video_stream.download(output_dir)

print("Finished downloading videos!")
