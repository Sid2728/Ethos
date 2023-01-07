import moviepy.editor
from tkinter.filedialog import *
from . models import Audio

# video=askopenfilename()
# print(video)
def Convert(vid,request):
  video=moviepy.editor.VideoFileClip(vid)
  audio=video.audio
  print(audio)
  filepath="main/audio/"+vid[vid.rfind('/')+1:vid.rfind('.')]+".mp3"
  audio.write_audiofile(filepath)
  saveaudio=Audio()
  saveaudio.audioFile=filepath
  saveaudio.uploaded_by_id=request.user.id
  saveaudio.save()

  print("--End--")
  return saveaudio.id