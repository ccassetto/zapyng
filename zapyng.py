import moviepy.editor as mp
import sys
import os
import subprocess
from os import listdir

cwd = os.getcwd()

os.system('clear')
query1=input("Set number of videos to download: ")
query2=input("Set duration of cuts in seconds: ")
os.system('clear')

for i in range(int(query1)):
	os.system('youtube-dl https://petittube.com/')

os.system('for i in *.mkv; do ffmpeg -i "$i" "${i%.*}.mp4"; done')
os.system('for i in *.webm; do ffmpeg -i "$i" "${i%.*}.mp4"; done')


folder = os.listdir(cwd)
clips = []

for item in folder:
	if item.endswith(".mp4"):
		clip = mp.VideoFileClip(item)
		clip = clip.resize(width=1920)
		if clip.duration>float(query2):
			clip = clip.subclip(0,float(query2))
		clips.append(clip)

for item in folder:
    if item.endswith(".mkv"):
        os.remove(os.path.join(cwd, item))
    elif item.endswith(".webm"):
        os.remove(os.path.join(cwd, item))

finalclip = mp.concatenate_videoclips(clips,method="compose")
finalclip.write_videofile("output.mp4")