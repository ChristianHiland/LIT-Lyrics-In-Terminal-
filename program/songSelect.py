import json
import time

def wait(timem):
  time.sleep(timem)

def start():
  print("Song Select:\n")
  
  with open('Lyrics/Abuse/Dog/Track_1/Track_1.json', 'r') as f:
      for jsonObj in f:
          lyricsDict = json.loads(jsonObj)
  for lyric in lyricsDict:
    wait(lyric["duration"])
    print("")
    print(lyric["text"])
start()
