# pip install pytube
from pytube import YouTube
from sys import argv

#argv takes your input into the commnad line when you run the program
link = argv[1]
# Creating YouTube object from the link
yt = YouTube(link)

print("Title:",yt.title)
print("Views:",yt.views)

yd = yt.streams.get_highest_resolution()
# Download video in the given directory
yd.download("/Users/ritikagupta/Desktop/Downloaded_uTube_Video")