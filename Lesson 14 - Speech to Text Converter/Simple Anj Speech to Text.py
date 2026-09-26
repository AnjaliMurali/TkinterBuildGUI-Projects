from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
import speech_recognition as sr
# ---------------- WINDOW ----------------
Window = Tk()
Window.title("Voice Notepad")
# ---------------- SPEECH RECOGNIZER ----------------
recognizer = sr.Recognizer()
# This will store the microphone
microphone = sr.Microphone()
# This will store the stop function
stop_listening = None
# ---------------- START RECORDING ----------------
def start_recording():
    global stop_listening
    status_label.config(text="Listening... Speak now!")
    # Function that runs when speech is detected
    def got_audio(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio)
            Output_text.insert(END, text + "\n")
        except sr.UnknownValueError:
            status_label.config(text="Could not understand the speech.")
        except sr.RequestError:
            status_label.config(text="Could not connect to Google.")

    # Start listening in the background
    # the below line means - Keep listening to the microphone in the background. 
    # Whenever you hear speech, call got_audio().
    stop_listening = recognizer.listen_in_background(
        microphone,
        got_audio
    )
    print(stop_listening)
# ---------------- STOP RECORDING ----------------
def stop_recording():
    global stop_listening
    if stop_listening is not None:
        stop_listening(wait_for_stop=False)
        stop_listening = None
        status_label.config(text="Recording stopped.")
    else:
        status_label.config(text="Recording is not running.")
# ---------------- SAVE ----------------
def save():
    fout = asksaveasfile(defaultextension=".txt",filetypes=[("Text files", "*.txt")])
    if fout is not None:
        print(Output_text.get("1.0", END).strip(),file=fout)
        fout.close()
        status_label.config(text="Text saved successfully!")
        messagebox.showinfo("Success","Text saved successfully!")

# ---------------- CLEAR ----------------
def clear():
    Output_text.delete("1.0",END)
#---------------- HEADING ----------------
heading1 = Label(Window,text="Voice Notepad",font=("Arial", 30, "bold"))
heading1.grid(row=0, column=1, padx=20, pady=20)
# ---------------- OUTPUT TEXT ----------------
Output_text = Text(Window,height=8,width=50,font=("Arial", 14))
Output_text.grid(row=1, column=1, pady=20, padx=20)
# ---------------- STATUS ----------------
status_label = Label(Window,text="Ready to record",font=("Arial", 12, "italic"))
status_label.grid(row=2, column=1, pady=10)
# ---------------- START BUTTON ----------------
start_button = Button(Window,text="Start",font=("Arial", 15, "bold"),width=15,height=3,command=start_recording)
start_button.grid(row=1,column=0,padx=20,pady=20)
# ---------------- STOP BUTTON ----------------
stop_button = Button(Window,text="Stop",font=("Arial", 15, "bold"),width=15,height=3,command=stop_recording)
stop_button.grid(row=1,column=2,padx=20,pady=20)
# ---------------- SAVE BUTTON ----------------
save_button = Button(Window,text="Save Text",font=("Arial", 12, "bold"),width=15,height=2,command=save)
save_button.grid(row=3,column=1,pady=20)
# ---------------- START GUI ----------------
#additional clear button
clearText_button = Button(Window,text="Clear Text",font=("Arial", 12, "bold"),width=15,height=2,command=clear)
clearText_button.grid(row=3,column=2,pady=20)
Window.mainloop()