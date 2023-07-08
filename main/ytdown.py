from pytube import YouTube
from . models import Audio
from yt_dlp import YoutubeDL
import random
import yt_dlp
import datetime
import ytdl
import subprocess
import string
import random

def generate_random_string(length):
    """Generate a random string of fixed length"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_unique_name(length=8):
    """Generate a unique name for the audio file"""
    while True:
        name = generate_random_string(length)
        # Check if the name already exists in the database
        if not Audio.objects.filter(url='main/audio/'+name+'.webm').exists():
            return name

def download(link,request):
    # ytdl audio link
    audio_file = generate_unique_name()
    output_directory = "main/static/main/audio/"
    output_format = output_directory+audio_file+'.%(ext)s'
    user =request.user
    audio_object_check = Audio.objects.filter(uploaded_by = user,url = link).exists()
    if audio_object_check:
        return Audio.objects.filter(uploaded_by = user,url = link).first().id

    with YoutubeDL() as ydl: 
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title', None)
        command = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', output_format, link]
        videos = subprocess.run(command, capture_output=True)
    if videos.returncode in [0,1]:
            vars=subprocess.run(['mv','ethos/'+audio_file+'.mp3','~/main/static/main/audio'])
            print(vars.returncode)
            # path='main/static/main/audio/'
            filename=audio_file+'.mp3'
            path='main/audio/'
            tempath=path +filename
            saveaudio=Audio()
            saveaudio.audioname = str(video_title)
            saveaudio.url = link
            saveaudio.audioFile=tempath
            saveaudio.uploaded_by_id = request.user.id
            saveaudio.url = link
            saveaudio.save()
            return saveaudio.id
    else:
        return -1    

# URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

# ydl_opts = {
#     'format': 'm4a/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'm4a',
#     }]
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(URLS)







    # youtube_1=YouTube(link)
    # videos=youtube_1.streams.filter(only_audio=True)
    # if videos==videos1:
    #     print("yep")
    # videos[0].download(path,filename)