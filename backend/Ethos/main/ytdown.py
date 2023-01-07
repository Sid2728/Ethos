from pytube import YouTube
from . models import Audio
import random
import datetime

def download(link,request):
    youtube_1=YouTube(link)
    videos=youtube_1.streams.filter(only_audio=True)
    path='main/static/main/audio/'
    filename=youtube_1.title+ str(random.random()) +'.mp3'
    videos[0].download(path,filename)
    path='main/audio/'
    tempath=path +filename
    saveaudio=Audio()
    saveaudio.audioname = youtube_1.title
    saveaudio.audioFile=tempath
    saveaudio.uploaded_by_id = request.user.id
    saveaudio.save()
    return saveaudio.id    
# print("done")
# print(youtube_1.title)