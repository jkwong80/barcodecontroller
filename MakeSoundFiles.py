
import os, sys
from gtts import gTTS
import string
soundfile_directory = 'soundfiles'

string_list = ['mommy', 'daddy']
string_list += ['helicopter', 'garbage truck', 'dump truck', 'taxi', 'bicycle', 'airplane', 'hot air balloon']
# colors
string_list += ['green', 'yellow', 'blue', 'red', 'orange' 'white', 'black', 'purple']
# animals
string_list += ['dog', 'cat', 'kitten', 'giraffe', 'gorilla', 'puppy']

string_list += [letter for letter in string.ascii_lowercase]


# random objects

# proper nouns

for temp in string_list:
    tts = gTTS(text=temp, lang='en')
    tts.save(os.path.join(soundfile_directory, "%s.mp3" %temp))



# os.system("mpg321 good.mp3")


