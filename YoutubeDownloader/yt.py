from pytube import YouTube
import os
import time

class yytd:
    def __init__(self, url, form, Vtitl):
        self.url=url
        self.form = form
        self.Vtitl = Vtitl


    def YoutubeURL(self):
        yturl = YouTube(url=self.url)
        titl = yturl.title
        print(titl)
        print(self.form)

        if self.form == "mp3":
            yt = yturl.streams.filter(only_audio = True).first()
            yt.download(output_path="mp3-player", filename=".mp3", filename_prefix= self.Vtitl)
    
        if self.form == "mp4":
            yt = yturl.streams.filter(progressive=True, file_extension='mp4').desc().first()
            yt.download(output_path="mov-Video", filename=".mov", filename_prefix = self.Vtitl)
