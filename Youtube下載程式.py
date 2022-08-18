from logging import root
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
        
        tkinter.messagebox.showinfo(title='Youtube下載程式', message='下載完成')

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
        tkinter.messagebox.showinfo(title='Youtube下載程式', message='下載完成')
        
    else:
        tkinter.messagebox.showinfo(title='Youtube下載程式', message='請選擇有效的副檔名')
    
window = tk.Tk()
window.title("Youtube下載程式")
window.geometry("400x200+800+350")
window.resizable(False, False)
window.iconbitmap('Youtube下載程式 icon.ico')

photo_canvas = Canvas(window, width=236, height=80)
photo_canvas.pack()

photo = ImageTk.PhotoImage(Image.open('Youtube下載程式 logo.png'))

photo_canvas.create_image(0,0, anchor=NW, image=photo)

label_entry = tk.Label(window, text='請在下方輸入連結')
label_entry.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

label_choose = tk.Label(window, text='請選擇您想要的副檔名')
label_choose.pack()

choose = ttk.Combobox(window,width=10, values=['MP4','WAV'], state='readonly')
choose.pack()

button_download = tk.Button(window, text='下載', width=20, command=download)
button_download.pack()

window.mainloop()
