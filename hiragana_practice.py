import random
from gtts import gTTS
from io import BytesIO
import os
import time
from playsound import playsound


def hiragana_test():
    hiragana_list = []
    files = os.listdir()

    file_names = (input('please enter the names of the hiragana columns you would like to practice, separated by commas, or all if you would like to be tested on all hiragana: ')).split(',')
    pause_time = float(input('please enter the number of seconds you would like to pause between reading out the sounds: '))

    if(file_names[0] == 'all'):

        for i in range(len(files)):

            files[i] = files[i].split('.')

            if files[i][1] == 'txt':
                current_file = open(files[i][0] + '.txt', 'r')

                for j in current_file:
                    if not ('\n' in j):
                        j += '\n'
                    hiragana_list.append(j)

                current_file.close()

    else: 
        for i in file_names:
            current_file = open(i + '.txt', 'r')

            for j in current_file:
                if not ('\n' in j):
                    j += '\n'
                hiragana_list.append(j)

            current_file.close()

    '''
    while(len(hiragana_list) > 0):
        index = random.randint(0, len(hiragana_list) - 1)
        mp3_F = BytesIO()
        tts = gTTS(hiragana_list[index], lang='ja')
        tts.write_to_fp(mp3_F)
        hiragana_list.remove(hiragana_list[index])
        time.sleep(pause_time)
    '''


    while(len(hiragana_list) > 0):
        index = random.randint(0, len(hiragana_list) - 1)
        tts = gTTS(hiragana_list[index], lang='ja')
        tts.save('audio.mp3')
        playsound('audio.mp3')
        time.sleep(pause_time)
        print(hiragana_list[index])
        hiragana_list.remove(hiragana_list[index])

    os.remove('audio.mp3')

hiragana_test()