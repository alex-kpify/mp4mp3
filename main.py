import os
from moviepy.editor import *
# video = VideoFileClip(os.path.join("TRF3-Gravação de Reunião.mp4"))
# video.audio.write_audiofile(os.path.join("TRF3-Gravação de Reunião.mp3"))
video = VideoFileClip(os.path.join("TRF4.mp4"))
video.audio.write_audiofile(os.path.join("TRF4-Gravação de Reunião.mp3"))