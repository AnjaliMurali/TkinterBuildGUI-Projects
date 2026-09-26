from tkinter import *
import speech_recognition as sr
import webbrowser
from urllib.parse import quote

# ---------------- WINDOW ----------------
Window = Tk()
Window.title("Voice Search")
# ---------------- SPEECH RECOGNIZER ----------------
recognizer = sr.Recognizer()
microphone = sr.Microphone()
# ---------------- SEARCH FUNCTION ----------------
def search_google():
    status_label.config(text="Listening... Speak now!")
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source)
        # Convert speech to text
        text = recognizer.recognize_google(audio)
        status_label.config(text="Searching for: " + text)
        # Create Google search URL
        search_url = "https://www.google.com/search?q=" + quote(text)
        # Open Google in the web browser
        webbrowser.open(search_url)
    except sr.UnknownValueError:
        status_label.config(text="Could not understand the speech.")
    except sr.RequestError:
        status_label.config(text="Could not connect to Google.")
# ---------------- HEADING ----------------
heading = Label(Window,text="What do you want to search?",font=("Arial", 24, "bold"))
heading.pack(pady=30)
# ---------------- SEARCH BUTTON ----------------
search_button = Button(Window,text="Search Google",font=("Arial", 15, "bold"),width=20,height=3,command=search_google)
search_button.pack(pady=20)

# ---------------- STATUS ----------------
status_label = Label(Window,text="Click the button and speak",font=("Arial", 12, "italic"))
status_label.pack(pady=20)
# ---------------- START GUI ----------------
Window.mainloop()

