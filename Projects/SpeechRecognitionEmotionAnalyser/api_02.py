# files after part 2
import requests
import time
from api_secret import API_KEY_ASSEMBLYAI
import pandas as pd
from nltk import tokenize
import numpy as np

from deep_translator import GoogleTranslator


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


def transcribe(audio_url):
    transcript_request = {
        'audio_url': audio_url
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']

        
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url):
    transcribe_id = transcribe(url)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
            
        print("waiting for 30 seconds")
        time.sleep(30)
        
        
def save_transcript(url, title, languages):
    data, error = get_transcription_result_url(url)
    
    if data:
        for lang in languages:
            translated_text = translation(data['text'], lang)
            np.savetxt(f"{title}_{lang}.txt", translated_text, delimiter="\n ", fmt='% s')
            print(f'Transcript saved in {lang} as txt')
    elif error:
        print("Error!!!", error)
        
def translation(text, language):
    translate_text = GoogleTranslator(source='auto', target=language).translate(text)
    tokenized_text = tokenize.sent_tokenize(translate_text)
    return tokenized_text