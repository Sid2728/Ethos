import moviepy.editor
# from tkinter.filedialog import *
from . models import Audio

# video=askopenfilename()
# print(video)
def Convert(vid,request,id):
  video=moviepy.editor.VideoFileClip(vid)
  audio=video.audio
  if audio==None:
    return -1
  # print(audio)
  print(audio)
  filepath="main/static/main/audio/"+str(id)+".mp3"
  audio.write_audiofile(filepath)
  saveaudio=Audio()
  filepath="main/audio/"+str(id)+".mp3"
  saveaudio.audioFile=filepath
  saveaudio.audioname = vid[vid.rfind('/')+1:vid.rfind('.')-1]
  saveaudio.uploaded_by_id=request.user.id
  saveaudio.save()

  print("--End--")
  return saveaudio.id