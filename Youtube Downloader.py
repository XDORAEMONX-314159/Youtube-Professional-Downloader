import tkinter as tk
from tkinter import Canvas, ttk
import tkinter.messagebox
from pytube import YouTube
from tkinter import filedialog
from tkinter.constants import * 
from tkinter import *
import os
from PIL import ImageTk, Image

choose_answer = None
        
def download():
    choose_answer = choose.get()
    if choose_answer == 'MP4':
        
        my_video = YouTube(str(url_entry.get()))
        my_video = my_video.streams.get_highest_resolution()
        my_video.download(filedialog.askdirectory())
        
        tkinter.messagebox.showinfo(title='Youtube Downloader', message='Download complete')

    elif choose_answer == 'WAV':
        video = YouTube(str(url_entry.get()))
        current_path = os.path.dirname(os.path.realpath(__file__))
        best_abr = int(video.streams.filter(only_audio=True)[0].abr.replace('kbps',''))
        best_abr_itag = video.streams.filter(only_audio=True)[0].itag
        
        for i in range(0, len(video.streams.filter(only_audio=True))):
            current_abr = int(video.streams.filter(only_audio=True)[i].abr.replace('kbps',''))
            
            if current_abr > best_abr:
                best_abr = current_abr
                best_abr_itag = video.streams.filter(only_audio=True)[i].itag
                
        output = video.streams.get_by_itag(best_abr_itag).download(filedialog.askdirectory())
        os.rename(output, output.replace('.webm', '.wav'))
        tkinter.messagebox.showinfo(title='Youtube Downloader', message='Download complete')
        
    else:
        tkinter.messagebox.showinfo(title='Youtube Downloader', message='Please choose the available file extention.')
    
window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("400x200+800+350")   
window.resizable(False, False)
window.iconbitmap('Youtube Profetional.ico')

cnv = Canvas(window, width = 236, height = 80)
cnv.pack()

photo = ImageTk.PhotoImage(Image.open("Youtube Downloader logo.png"))
cnv.create_image(0, 0, anchor=NW, image=photo)



label_entry = tk.Label(window, text='Please enter the URL down')
label_entry.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

label_choose = tk.Label(window, text='Please choose the file extention which you want')
label_choose.pack()

choose = ttk.Combobox(window,width=10, values=['MP4','WAV'], state='readonly')
choose.pack()

button_download = tk.Button(window, text='Download Now', width=20, command=download)
button_download.pack()

window.mainloop()
