from pytube import YouTube
from moviepy.editor import *
import os, sys

class Audio:
    def __init__(self, filetype):
        self.filetype = filetype
        
    def Mp4ToFile(self, mp4Path):
        AudioFullPath = mp4Path
        
        #Extract FileName
        AudioFileName = AudioFullPath.split("\\")[-1]
        
        #Change to chosen file type and new directory
        NewAudioFileName = str("".join(AudioFileName.split(" "))[:-3])+self.filetype
        NewAudioFullPath = os.getcwd()+"\\output\\"+str(NewAudioFileName)
        
        #Transform to your chosen file
        preTransform = AudioFileClip(AudioFullPath)
        preTransform.write_audiofile(NewAudioFullPath)
        
        print(NewAudioFullPath)

class Downloader:

    def __init__(self, url):
        self.url = url
    
    def getaudio(self):
        video = YouTube(self.url)
        
        audio_stream = video.streams.filter(file_extension='mp4').filter(only_audio=True)
        audio_stream = audio_stream[-1]
        return audio_stream.download()
    
if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: yt_downloader.py {URL}")
    else:
        #test: https://www.youtube.com/watch?v=9bZkp7q19f0
        TestObj = Downloader(sys.argv[-1])
        downloaded_filename = TestObj.getaudio()
        Audio("ogg").Mp4ToFile(downloaded_filename)
    