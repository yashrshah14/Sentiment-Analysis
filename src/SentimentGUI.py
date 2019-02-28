# Importing libraries and modules
from tkinter import *
from PIL import ImageTk, Image
import time
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pygif as gif

# Start of GUI
root = Tk()
root.title("Sentiment Analysis")
bg_color = "PINK"

dict = {
"anger" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/anger.gif",
"joy" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/joy.gif",
"sadness" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/sadness.gif",
"fear" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/fear.gif",
"disgust" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/disgust.gif",
"shame" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/shame.gif",
"guilt" : "/Users/abhianshusingla/Documents/Multi-Sentiment Analysis/images/guilt.gif",
}

dic_word = {
"anger" : "angry",
"joy" : "joyful",
"sadness" : "sad",
"fear" : "fearful",
"disgust" : "disgusting",
"shame" : "shameful",
"guilt" : "guilty",
}

gif_array = {
"anger" : gif.AnimatedGIF(root, dict["anger"]),
"joy" : gif.AnimatedGIF(root, dict["joy"]),
"sadness" : gif.AnimatedGIF(root, dict["sadness"]),
"fear" : gif.AnimatedGIF(root, dict["fear"]),
"disgust" : gif.AnimatedGIF(root, dict["disgust"]),
"shame" : gif.AnimatedGIF(root, dict["shame"]),
"guilt" : gif.AnimatedGIF(root, dict["guilt"]),
}




# Frames
main_frame = Frame(root, bg = bg_color)
main_frame.pack()

top_frame = Frame(main_frame, bg = bg_color)
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame, bg = bg_color)
bottom_frame.pack(side=TOP)


# Heading
header_label = Label(top_frame, text="How are you feeling?",font=("Chalkboard", 50), fg = "RED", bg = bg_color)
header_label.pack(anchor = N)

# Text
ask_label = Label(top_frame, text="Tell me",font=("Chalkboard", 20), fg = "BLACK", bg = bg_color)
ask_label.pack(anchor = N)

# Entry
sentene_entry = Entry(top_frame, width = 40, bg = bg_color, fg = "BLACK")
sentene_entry.pack()

# Sentiment Label
emotion_label = Label(bottom_frame,font=("Chalkboard", 50), fg = "RED", bg = bg_color)
emotion_label.pack(anchor = N)

def getSentence():
    return str(sentene_entry.get())



def show_image(val):
    emotion = val
    for key in dict:
        if(gif_array[key].winfo_ismapped()):
            gif_array[key].pack_forget()

    gif_array[val[0]].pack()
    emotion_label["text"] = "You are " + dic_word[val[0]]





# Main Loop
def start():
    root.mainloop()
    time.sleep(0.1)
