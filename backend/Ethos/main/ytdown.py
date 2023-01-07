from pytube import YouTube
def download(link):
    youtube_1=YouTube(link)
    videos=youtube_1.streams.filter(only_audio=True)
#all->format
    # vid=list(enumerate(videos))
    # for i in vid:
    #     print((i[1].abr[0:i[1].abr.index('k')]))
# strm=min(opns)
# print(strm)
# Ethos\backend\Ethos\Ethos\backend\Ethos\main\media\S jaishankar reply to Austria's state broadcaster ORF Full Video.mp3
# Ethos\backend\Ethos\main\media\vid.mp3
    path='main/media/'
    filename=youtube_1.title+'.mp3'
    videos[0].download(path,filename)
# print("done")
# print(youtube_1.title)