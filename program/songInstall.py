import os
from pytube import YouTube
import lyricGet

def download(folderName, url, trackNames):
  url = YouTube(url)
  # accessing audio streams of YouTube obj.(first one, more available)
  stream = url.streams.filter(only_audio=True).first()
  print(stream)
  # download into working directory
  stream.download(folderName)
  print("You'll need to renamed the song to the name to Track_#.mp4")
  lyrics = input("Do you want the lyrics? [Y/N] ")
  if lyrics.lower() == str("n"):
    lyricGet.lyrics(folderName, url, trackNames)
  else:
    print("Ok")

def down():
  play = input("Is this song in a new album? [Y/N] ")
  if play.lower() == str("y"):
    albumName = input("What is the name of the album? ")
    folder = str("Song_List/" + albumName)
    os.mkdir(folder)
  else:
    print("Artist In folder:\n")
    os.listdir("Song_List/")
    print(" ")
    artistName = input("What's the name of that artist? ")
    albumName = input("What's the album name? ")
    trackName = input("What's the track number? ")
    trackNames = str("Track_" + trackName)
    folderName = str("Song_List/" + artistName + "/" + albumName + "/" + trackNames)
    url = input("What's the URLs' name: ")
    download(folderName, url, trackNames)
down()
