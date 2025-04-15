
ydl_opts = {
    'ffmpeg_location' : "ffmpeg",
    "cookies": "www.youtube.com_cookies.txt",
    'no_post_overwrites': True,
    'ignoreerrors': True,
    'format': 'bestvideo+bestaudio',  # Select best audio quality
    'outtmpl': directory + '%(uploader)s - %(title)s.%(ext)s',  # Save file with the title of the video
    'postprocessors': [{  # Add post-processor to convert to mp3
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
}

def download_url():
    pass