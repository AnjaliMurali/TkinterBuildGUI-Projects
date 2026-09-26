"""
First Step : pip install gTTS on command Prompt or Terminal
# pip list  - type this on terminal and you can see all installed modules of python.
"""
from tkinter import *
from gtts import gTTS  #gTTS stands for Google Text-to-Speech.
import os #for playing the audio from the system

root = Tk()
root.title("text_to_speech_convertor")
root.geometry("650x550")

def play():
    # Language in which you want to convert
    language = "en"
    """
    "fr"   # French
    "de"   # German
    "es"   # Spanish
    "hi"   # Hindi
    """

    # Passing the text  and language,
    # here we have  slow=False. Which tells
    # the module that the converted audio should
    # have a high speed

    myobj = gTTS(text=entry.get(),lang=language)
  

    # give the name as you want to
    # save the audio
    """
     #For macOS use: 
        myobj.save("convert.mp3")
        os.system("open convert.mp3")

        # or another method that to specify path

        myobj.save("Lesson 13/convert.mp3")
        os.system("open 'Lesson 13/convert.mp3'")

    """
    #For windows use: 
    #myobj.save("convert.mp3") 
    #os.startfile("Lesson 13 - Text to Speech Converter/convert.mp3")
   
    myobj.save("convert.mp3")
    os.startfile(os.path.abspath("convert.mp3"))
    """
    If the path is not clear and media player is not opening by default, then try this 
        myobj.save("Lesson 13 - Text to Speech Converter/convert.mp3")
        path = os.path.abspath("Lesson 13 - Text to Speech Converter/convert.mp3")
        print(path)
        os.startfile(path)
    """
    
    

label = Label(root, text="Text to Speech",font="bold, 30",bg="lightpink")
label.pack(pady = 50)
entry = Entry(root, width=30, font=14)
entry.pack()
#entry.insert(0, "")
btn = Button(root, text="SUBMIT",width="15", pady=10,font="bold, 15",bg='yellow',command=play)
btn.pack(pady = 50)
root.mainloop()