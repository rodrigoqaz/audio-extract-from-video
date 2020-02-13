import sys
from moviepy.editor import *
import os

videos = 'videos/'

for r, d, f in os.walk(videos):
    for file in f:
        if not file[0] == '.':
            video_path = os.path.join(r, file)
            audio_path = os.path.join('audios', file.replace('.mp4', '.mp3'))
            video = VideoFileClip(video_path)
            audio = video.audio
            audio.write_audiofile(audio_path)
