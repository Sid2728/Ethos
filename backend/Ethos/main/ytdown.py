from pytube import YouTube
from . models import Audio
import random
def download(link,request):
    youtube_1=YouTube(link)
    videos=youtube_1.streams.filter(only_audio=True)
    idcnt=10000
    path='main/audio/'
    filename=youtube_1.title+'.mp3'
    videos[0].download(path,filename)
    tempath=path+filename
    saveaudio=Audio()
    saveaudio.audioFile=tempath
    saveaudio.uploaded_by_id = request.user.id
    saveaudio.save()
    return saveaudio.id    
# print("done")
# print(youtube_1.title)