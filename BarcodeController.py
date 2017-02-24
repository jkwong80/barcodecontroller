# import pyttsx
from pygame import mixer
import string

key_sound_map = {}
key_sound_map['littledrummerboysong'] = 'Bing Crosby - The Little Drummer Boy (1962).mp3'
key_sound_map['puffmagicdragon'] = 'Peter Paul & Mary - Puff The Magic Dragon.mp3'
key_sound_map['lionsong'] = 'The Tokens - The Lion Sleeps Tonight.mp3'
key_sound_map['mommy'] = 'mommy.mp3'
key_sound_map['daddy'] = 'daddy.mp3'

for letter in string.ascii_lowercase:
    key_sound_map[letter] = '%s.mp3' %letter


string_list = ['mommy', 'daddy']
string_list += ['helicopter', 'garbage truck', 'dump truck', 'taxi', 'bicycle', 'airplane', 'hot air balloon']
# colors
string_list += ['green', 'yellow', 'blue', 'red', 'orange' 'white', 'black', 'purple']
# animals
string_list += ['dog', 'cat', 'kitten', 'giraffe', 'gorilla', 'puppy']

for temp in string_list:
    key_sound_map[temp] = "%s.mp3" %temp

mixer.init()
try:
    while True:
        code = raw_input("Scan: ")
        # do something with the scanned code
        if code in key_sound_map:
            mixer.music.load(key_sound_map[code])
            mixer.music.play()
            print('Playing %s' %key_sound_map[code])
        if code == 'stop':
            mixer.music.stop()
        if code == 'pause':
            mixer.music.pause()
except KeyboardInterrupt:
    print "\nExit"

mixer.quit()