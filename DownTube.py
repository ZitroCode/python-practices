#/bin/pydoc3.9

from pytube import YouTube

link = input("Enter URL of video\n>> ")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
