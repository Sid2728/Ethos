import moviepy.editor
from tkinter.filedialog import *


# video=askopenfilename()
# print(video)
def Convert(vid):
  video=moviepy.editor.VideoFileClip(vid)
  audio=video.audio
  print(audio)
  audio.write_audiofile("main/media/"+vid[vid.rfind('/')+1:vid.rfind('.')]+".mp3")
  print("--End--")