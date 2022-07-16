from gtts import gTTS
import os

#method 2
#You can give text file location to read the text
abc=open("sample1.txt")
text=abc.read()

#method 1
#text="Hey guys! my name is shreyas! "


language='en' #english lang

obj= gTTS(text=text,lang=language,slow=False)
#We have used slow = false because our converted video will be having high speed
obj.save("sample.mp3")

os.system('sample.mp3')

#to open music player directy we have to import os