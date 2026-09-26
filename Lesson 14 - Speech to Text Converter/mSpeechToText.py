"""
First Step : pip install SpeechRecognition -  on command Prompt or Terminal
# pip list  - type this on terminal and you can see all installed modules of python.
"""

from tkinter import *
import speech_recognition as sr # import the library
from tkinter import messagebox
from tkinter.filedialog import *



Window= Tk ()
#add title
Window. title ("Speech to Text")
#add dimensions
Window. geometry("800x400")

#heading
heading1 = Label (Window, text = "Voice Notepad", font = "bold, 30 ")
heading1.grid(row=0, column=1, padx=20, pady=20)
#label and entry box for enter the text
#label1= Label (Window, text = "Click Button to record your speech:")
#label1.grid (row=1, column=0, padx=10)
#Text label
Output_text = Text (Window, height= 4, width = 40)
Output_text. grid (row=1, column=1, pady = 20, padx=20)

#function
def Translate () :
    r = sr. Recognizer ()
    with sr. Microphone () as source:
        print ("Speak Anything ")
        audio = r.listen (source)
        try:

            text = r.recognize_google (audio)
        except :
            text="Sorry could not recognize your voice"
            Output_text.delete (1.0, END)
            Output_text. insert (END, text)

# initialize recognize
# mention source it will be either Microphone or audio files.

# listen to the source

# use recognizer to convert our audio into text part.

def save():
#get file using dialog
#default extension is optional, here will add .txt if missing
    fout=asksaveasfile (defaultextension=".txt") #if filename selected
    if fout:
        print (Output_text. get (1.0, END) , file=fout)
    else:
        messagebox. showinfo ("Warning", "Text not saved")


# our Translate function using command = Translate
trans_btn = Button (Window, text = 'Click on me !.. \nTo start recording',font = ("Arial",15,"bold"), command = Translate, width=20)
trans_btn.grid (row=1, column=0, pady = 20, padx=20)
save_button = Button (Window, text='Save the Text', width=20, height=4, command=save)
save_button. grid (row = 1, column = 2, pady = 10, columnspan=3)
# start the gui
Window.mainloop ()