from pytube import YouTube
import os
import re

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process to run in terminal
class Yt_Downloader:

    def __init__(self, link):
        self.link = link
        self.path = "Downloads"
        self.status = 0


    def download(self):
        try:
            youtubeObject = YouTube(self.link) 
        except:
            return self.status      
        if(os.path.exists(self.path + "/" + youtubeObject.title +".mp4")):
            print("\nVIDEO ALREADY EXISTS, TRY A DIFFERENT ONE!\n")
            self.status = 2
        else:
            youtubeObject = youtubeObject.streams.get_highest_resolution()     
            try:                      
                youtubeObject.download(self.path)
            except:
                print("ERROR WHILE DOWNLOADING THIS VIDEO!\n")
                return self.status 
            print("DOWNLOAD FINISHED!\n")
            self.status = 1
        return self.status


# MAIN
if __name__ == "__main__":
    yt_Downloader = Yt_Downloader()