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

        


"""
    yt.download()
    #print("Downloaded")
    time.sleep(10)

    if rename == "":
        rename = title
        if form == "mp3":
            os.rename(titl + ".mp4", rename + ".mp3")
            
            
        elif form == "mp4":
            os.rename(titl + ".mp4", rename + ".mov")
            
    
    else:
        if form == "mp3":
            os.rename(titl + ".mp4", rename + ".mp3")
            
        elif form == "mp4":
            os.rename(titl + ".mp4", rename + ".mov")

    print(YoutubeTitle(titl))


def YoutubeTitle(title):
    return title
"""
    
#YoutubeURL("https://www.youtube.com/watch?v=OUeaAOIAbXs", "mp4", "Textmp4")
"""
url = str(input("YouTube-URL eingeben:\n>>> "))
my_video = YouTube(url)

print("\nWelche Dateiformat soll runtergeladen werden?")
print("mp4 = Bild & Audio \nmp3 = nur Audio")
data = input(">>> ")


if data == "mp4":
    yt = my_video.streams.filter(progressive=True, file_extension='mp4').desc().first()
elif data == "mp3":
    yt = my_video.streams.filter(only_audio = True).first()
    
else:
    print("Falsch Eingabe !!! ")

    

print("\n*********************Video Title************************")
#get Video Title
print(my_video.title)

print("\n********************Tumbnail Image***********************")
#get Thumbnail Image
print(my_video.thumbnail_url)
    
print("\n********************Download läuft***********************")
yt.download()
print("\n********************Erfolgreich beendet***********************")
time.sleep(10)
print("\n********************Dateiname Ändern***********************")
rename = input("Soll der dateiname geändert werden ?\n>>> ")
if rename == "ja":
    x = input("\nWie soll die Datei heißen?\n>>> ")
    if data == "mp3":
        os.rename(yt.title + ".mp4", x + ".mp3")
    elif data == "mp4":
        os.rename(yt.title + ".mp4", x + ".mp4")
    print("********************Erfolgreich Umbenannt***********************")
    
elif rename == "nein":
    if data == "mp3":
        os.rename(yt.title + ".mp4", yt.title + ".mp3")
    elif data == "mp4":
        os.rename(yt.title + ".mp4", yt.title + ".mp4")
    print("********************Dateiname behalten***********************")
"""
