import moviepy.editor
from tkinter.filedialog import *
# from . views import passing
from . models import Audio
# video=askopenfilename()
# print(video)
idcnt=1
def Convert(vid):
  video=moviepy.editor.VideoFileClip(vid)
  audio=video.audio
  
  # print(audio)
  # print("HEREERERREREERER")
  # passing(audio)
  temppath="main/media/"+vid[vid.rfind('/')+1:vid.rfind('.')]+".mp3"
  audio.write_audiofile(temppath)
  saveaudio=Audio()
  saveaudio.audioFile=temppath
  saveaudio.uploaded_by_id = idcnt
  idcnt=idcnt+1
  saveaudio.save()
  print("--End--")