import requests
import json
import time
from .api_secrets import API_KEY_ASSEMBLYAI
from .models import Audio


upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}

headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB


def upload(filename):
    def read_file(filename):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
    return upload_response.json()['upload_url']


def transcribe(audio_url, sentiment_analysis):
    transcript_request = {
        'audio_url': audio_url,
        'sentiment_analysis': sentiment_analysis
    }
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']

        
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url, sentiment_analysis): 
    transcribe_id = transcribe(url, sentiment_analysis)  
    while True:
        data = poll(transcribe_id)
        print(data)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return None, data.get('error', 'Unknown error occurred')

        print("Waiting for 30 seconds")
        time.sleep(30)

      
def save_transcript(request, url, title, sentiment_analysis=False):
    data, error = get_transcription_result_url(url, sentiment_analysis)
    audio = Audio.objects.order_by('-id').first()
    if data:
        filename = title + '.txt'
        print(filename)
        for element in data['sentiment_analysis_results']:
            sentiment = element['sentiment']
            if sentiment == 'NEUTRAL':
                audio.neutral += 1
            elif sentiment == 'NEGATIVE':
                audio.negative += 1
            elif sentiment == 'POSITIVE':
                audio.positive += 1
        audio.save()
        print(sentiment)
        print('Transcript saved')
        return True
    elif error:
        print("Error!!!")
        return False