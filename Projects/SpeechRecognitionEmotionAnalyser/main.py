from api_02 import *
from yt_dl import download
import sys

filename = download("https://www.youtube.com/watch?v=zhWDdy_5v2w")
audio_url = upload(filename)

# See options here: https://github.com/lushan88a/google_trans_new/blob/main/constant.py

languages = ['fr', 'en', 'es']
save_transcript(audio_url, 'transcript_file', languages)