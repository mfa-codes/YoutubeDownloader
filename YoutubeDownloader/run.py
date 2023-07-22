from tkinter import *
import yt as y
from pytube import YouTube
import os
import time

# root-Setup
root = Tk()
root.geometry("1000x900")
root.title("Youtube Downloader")
# tk config
root.configure(background='#103783', borderwidth=5)

# Elemente-Variabeln
v = IntVar() # save the value of Radiobutton an check up in ShowChoice()


def getbegin():
    download()
    
def getLink():
        return str(link.get("1.0","end-1c"))

def getTitle():
        return str(Vname.get("1.0","end-1c"))

def ShowChoice():
    if v.get() == 1:
        return "mp3"
    else:
        return "mp4"

def download():
    yt = y.yytd(getLink(), ShowChoice(), getTitle())
    yt.YoutubeURL()
    exit()


# GUI-Elemente        
# Headline
l = Label(root, text="--> Youtube downloader <--", fg = "white", bg = "#103783",  width = 40, height = 3, font=("fett", 32))
l.pack(fill=X, side=TOP)

# Textfield-Label
urlText = Label(root, text="Youtube-URL:", fg = "white", bg="#103783", font=("fett", 18))
urlText.pack(fill=X,pady=5)

# Textfiel-URL
link = Text(root, fg = "#103783", bg = "#fbe9d7", height=4, width=50, font=("fett" ,13))
link.pack(pady=5 )

# line
ln1 = Label(root, text="", fg = "white", bg = "#fbe9d7", font=("kusiv", 2))
ln1.pack(fill=X, pady=5)

# Title-Label
title = Label(root, text="File name:", fg = "white", bg="#103783", font=("fett", 18))
title.pack(fill=X,pady=5)

# Title-Input
Vname = Text(root, fg = "#103783", bg = "#fbe9d7", height=4, width=50, font=("fett" ,13))
Vname.pack(pady=10)

# line
ln1 = Label(root, text="", fg = "white", bg = "#fbe9d7", font=("kusiv", 2))
ln1.pack(fill=X, pady=5)

# Radiobuttons-Label
ft = Label(root, text="Format:", fg = "white", bg="#103783", font=("fett", 18))
ft.pack(fill=X, pady=5)

# Radiobuttons
rmp3 = Radiobutton(root, text="MP3 (Audio)",variable=v, value=1, fg = "#103783", bg="#fbe9d7", font=("fett", 13))
rmp3.pack(pady=5 )

rmp4  = Radiobutton(root, text="MP4 (Video)", variable=v, value=2, fg = "#103783", bg="#fbe9d7",font=("fett", 13))
rmp4.pack(pady=5 )

# line
ln2 = Label(root, text="", fg = "white", bg = "#fbe9d7", font=("kusiv",2))
ln2.pack(fill=X, pady=10)

# Download-Button
b = Button(root, text="Download", width = 20, height = 2 , fg = "#103783", bg = "#fbe9d7", font=("fett", 14), command=getbegin)
b.pack(pady=10)

# line
ln3 = Label(root, text="", fg = "white", bg = "#fbe9d7", font=("kusiv",2))
ln3.pack(fill=X, pady=10)


# Version-Label
version = Label(root, text="Version 1.0", fg = "white",  bg="#103783" ,font=(9))
version.pack(side=BOTTOM)

root.mainloop()

