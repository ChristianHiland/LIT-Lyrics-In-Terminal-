from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

def lyrics(folderName, url, trackNames):
  id = url.replace("https://www.youtube.com/watch?v=", '')
  
  # Must be a single transcript.
  transcript = YouTubeTranscriptApi.get_transcript(id)
  formatterJSON = JSONFormatter()
  
  # .format_transcript(transcript) turns the transcript into a JSON string.
  json_formatted = formatterJSON.format_transcript(transcript)
  lyricFile = str(folderName + "/" + trackNames + ".json")
  
  # Now we can write it out to a file.
  with open(lyricFile, 'a', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

def varGet():
  artistName = input("What's the name of that artist? ")
  albumName = input("What's the album name? ")
  trackName = input("What's the track number? ")
  trackNames = str("Track_" + trackName)
  folderName = str("Lyrics/" + artistName + "/" + albumName + "/" + trackNames)
  url = input("What's the URLs' name: ")
  lyrics(folderName, url, trackNames)
varGet()
