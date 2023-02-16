import program.song_install as songIN
import program.song_select as songSel
import program.lyricGet as lyricG

print("1. Song Install\n 2. Lyrics Get\n 3. Song Select\n")

user = input("What option? ")

if user == str("1"):
  songIN.down()
elif user == str("2"):
  lyricG.varGet()
elif user == str("3"):
  songSel.start()
else:
  print("Wrong option.")
