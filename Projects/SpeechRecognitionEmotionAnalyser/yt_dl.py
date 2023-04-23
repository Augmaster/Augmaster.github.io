import pytube
import time
def download(url):
    yt = pytube.YouTube(url)
    downloader = None
    while downloader is None:
        try:
            downloader = yt.streams.filter(only_audio=True).get_audio_only()
        except:
            print("Download Fail, retrying in 5 seconds")
            time.sleep(5)
            pass
    path = downloader.download()
    print(path)
    return path
