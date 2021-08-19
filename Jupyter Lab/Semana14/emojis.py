# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 23:24:00 2020

@author: ASUS
"""
from tkinter import *
import tkinter.font as tkFont

# Dict with all the emojis
# it is made in this format -->    EMOJI_NAME: EMOJI_SURROGATE_PAIR
emoji_dict = {
    "GRINNING_FACE": '\ud83d\ude00',
    "GRINNING_FACE_WITH_BIG_EYES": '\ud83d\ude03',
    "GRINNING_FACE_WITH_SMILING_EYES": '\ud83d\ude04',
    "BEAMING_FACE_WITH_SMILING_EYES": '\ud83d\ude01',
    "GRINNING_SQUINTING_FACE": '\ud83d\ude06',
    "GRINNING_FACE_WITH_SWEAT": '\ud83d\ude05',
    "LAUGHING_ON_THE_FLOOR": '\ud83e\udd23',
    "TEARS_OF_JOY": '\ud83d\ude02',
    "SMILING_FACE_SLIGHTLY": '\ud83d\ude42',
    "UPSIDE-DOWN_FACE": '\ud83d\ude43',
    "WINKING_FACE": '\ud83d\ude09',
}

emoji_num_name = dict()
emoji_name_num = dict()
counter = 0

for key in emoji_dict:
    emoji_num_name[counter] = key
    emoji_name_num[key] = counter
    counter += 1
    
def sumbit(text):
    text = text.split(":-")
    for index in range(len(text)):
        word = text[index]
        word = word.split("-:")
        for index_ in range(len(word)):
            little_word = word[index_]
            if little_word.isdigit():
                emoji_name = emoji_num_name[int(little_word)]
                emoji = emoji_dict[emoji_name]
                word[index_] = emoji
        text[index] = "".join(word)
    text = "".join(text)
    text = text.encode('utf-16', 'surrogatepass').decode('utf-16')
    print(text)
def creates_emojis():
    x = 10
    y = 0
    for emoji_name in emoji_dict:
        emoji_code = emoji_dict[emoji_name]
        code_ = emoji_name_num[emoji_name]
        emoji_button = Button(emoji_frame, text=emoji_code, borderwidth=0, font=customFont)
        emoji_button.place(x=x, y=y)
        #emoji_button.bind("<Button-1>", lambda event, code=code_, var=sumbit_var: insert_emoji(var, ":-" + str(code) + "-:"))
        
        if x <= 150:
            x += 30
        else:
            x = 10
            y += 30
    emoji_frame.configure(widt=200, height=y+60)





root = Tk()
root.tk.call('encoding', 'system', 'utf-8')
root.configure(width=500, height=500)
font = "Courier"
customFont = tkFont.Font(family=font, size=14)

emoji_frame = LabelFrame(text="emojis")
emoji_frame.place(x=10, y=60)
sumbit_var = StringVar()
print(sumbit_var.get())

creates_emojis()



root.mainloop()