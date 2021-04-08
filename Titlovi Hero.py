import sys
import codecs
import os

filename = "a.srt"

file2 = open(filename, "r")
file3 = open("titl.srt", "w", encoding='utf8')
contents = file2.read()
contents.encode("UTF-8")
newcontents = contents.replace("æ", "ć").replace("è","č").replace("È","Č").replace("Æ","Ć")

file3.write(newcontents)
file3.close()
file2.close()

if os.path.exists(filename):
    os.remove(filename)
else:
    print("The file does not exist")
