"""
Script para extrair o áudio de um vídeo
"""
import os
from moviepy.editor import VideoFileClip  # pylint: disable=E0401

video = VideoFileClip(os.path.join("GT.mp4"))
video.audio.write_audiofile(os.path.join("GT.mp3"))
