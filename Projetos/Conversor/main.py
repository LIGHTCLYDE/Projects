from cProfile import label
from cgitb import text
import re
from struct import pack
import tkinter as tk
from turtle import bgcolor
from numpy import var
from pytube import YouTube
from moviepy.editor import *


root = tk.Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Conversor de YT para MP3")
root.configure(bg="#20B2AA")

tk.Label(root,
      text='YouTube Video Downloader',
      font='arial 20 bold',
      bg="#000000",
      fg="White").pack()


link = tk.StringVar()
tk.Label(root,
      text='Cole o link de download aqui ⇩',
      font='gotham 15 bold',
      bg="White").place(x=40, y=60)


link_enter = tk.Entry(root,
                   width=50,
                   textvariable=link).place(x=32, y=90)
                
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams[1]
    video.download()
    tk.Label(root,
          text='BAIXADO',
          font='gotham 15',
          bg="black",
          fg="blue").place(x=185, y=185)
    return video.download()

def converter():
    mp4_file = f"C:/Users/Sup34/Desktop/Conversor/mp3Downloads"
    mp3_file = downloader()
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
    tk.Label(root,
          text='Convertido',
          font='arial 15',
          bg="black",
          fg="blue").place(x=185, y=245)


download_mp4 = tk.Button(root,
                      text='Baixar',
                      font='arial 15 bold',
                      bg='White',
                      padx=2,
                      command=downloader,
                      fg="Black").place(x=180, y=150)



convert_mp4 = tk.Button(root,
                      text='Converter para mp3',
                      font='arial 15 bold',
                      bg='White',
                      padx=2,
                      command=converter,
                      fg="Black").place(x=180, y=210)

root.mainloop()