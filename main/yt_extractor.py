from youtube_dl.utils import DownloadError
from yt_dlp import YoutubeDL

with YoutubeDL() as ydl:

    def get_video_info(url):
        with ydl:
            try:
                result = ydl.extract_info(
                    url,
                    download=False
                )
            except DownloadError:
                return None

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        return video


    def get_audio_url(video):
        for f in video['formats']:
            if f['ext'] == 'm4a':
                return f['url']
    



