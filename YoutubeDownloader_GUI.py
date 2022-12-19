import PySimpleGUI as sg
import tkinter as tk
import concurrent.futures

from Youtube_Downloader import Yt_Downloader
from threading import Thread

def popup(message = "Downloading your video, please wait..."):
    sg.theme('DarkGrey')
    layout = [[sg.Text(message)]]
    window = sg.Window('Message', layout, no_titlebar=True, keep_on_top=True, finalize=True)
    return window


def download(link):
    ytd = Yt_Downloader(link)
    status = ytd.download()
    return status


window_column = [
    [
        sg.Text("URL: "),
        sg.InputText("", size = (55,1), enable_events = True, key = "-URL-")
    ]

]

layout = [
    [sg.Text("Welcome to YoutbeDownloader")],
    [sg.Column(window_column)],
    [sg.Button("Download")],
    [sg.Button("Exit")]
]

window = sg.Window("Youtube Downloader", layout)
#elegxo gia link = 00
while True:
    event, values = window.read()
    if(event == "Download"):
        if(values["-URL-"] != ""):
            link = values["-URL-"]
            popup_win = popup()
            window.force_focus()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(download, link)
                status = future.result()
            # thread = Thread(target = download, args = ({link}), daemon = True)
            # thread.start()
            # status = thread.join()
            popup_win.close()
            if(status == 0):
                tk.messagebox.showerror(title = "Something went wrong", message = "An error occured while trying to download this video\n Check if the link is correct!")    
            elif(status == 2):
                tk.messagebox.showwarning(title = "Something went wrong", message = "This video already exists in your folder\nTry a new one!")
            else:
                tk.messagebox.Message(title = "Complete", message = "Video downloaded successfully")
                window["-URL-"].Update("")
        else:
            tk.messagebox.showerror(title="Something went wrong", message="Please paste a youtube link first!")
    if(event == "Exit" or event == sg.WIN_CLOSED):
        break
window.close()



