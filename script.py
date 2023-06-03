
import os
import pytube
#from http.client import IncompleteRead

# Replace PLAYLIST_URL with the URL of the YouTube playlist
# Replace START_VIDEO with the number of the first video you want to download
# (e.g. if you want to start downloading from the third video, set START_VIDEO = 3)
PLAYLIST_URL = "ENTER THE URL OF YOUTUBE PLAYLIST HERE"
 
START_VIDEO = 1 
END_VIDEO=50

# Create a PyTube playlist object
playlist = pytube.Playlist(PLAYLIST_URL)

# Get a list of all the video URLs in the playlist
video_urls = playlist.video_urls

# Iterate over the list of video URLs starting from the specified video number
for url in video_urls[START_VIDEO - 1:END_VIDEO]:
    # Create a PyTube video object
    video = pytube.YouTube(url)

    # Get the video's title and file size
    video_title = video.title
    try:
        file_size = video.streams.first().filesize
    except KeyError:
        file_size = "unknown"
    #file_size = video.streams.first().filesize
    
    # Print the video's title and file size
    print(f"Downloading '{video_title}' ...")

    # Set the output directory for the downloaded videos
    # Replace "videos" with the desired output directory
    output_dir = "cpp"

    # Check if the output directory exists, and create it if it doesn't
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Try to get a 720p video stream
    video_stream = video.streams.filter(resolution='720p').first()

    # If no 720p stream is available, try to get a 480p stream
    if video_stream is None:
        video_stream = video.streams.filter(resolution='480p').first()

    # If no 480p stream is available, try to get a 360p stream
    if video_stream is None:
        video_stream = video.streams.filter(resolution='360p').first()

    # Download the video to the output directory
    video_stream.download(output_dir)

print("Finished downloading videos!")
