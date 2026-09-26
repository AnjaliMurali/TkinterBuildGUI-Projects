"""
Follow the setup guide depending on the OS. 
# pip list  - type this on terminal and you can see all installed modules of python.
"""


from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile


Window = Tk()
Window.title("Speech to Text")
#Window.geometry("900x500")


# ---------------- HEADING ----------------

heading1 = Label(
    Window,
    text="Voice Notepad",
    font=("Arial", 30, "bold")
)
heading1.grid(row=0, column=1, padx=20, pady=20)


# ---------------- OUTPUT TEXT ----------------

Output_text = Text(
    Window,
    height=8,
    width=50,
    font=("Arial", 14)
)
Output_text.grid(row=1, column=1, pady=20, padx=20)


# ---------------- STATUS LABEL ----------------

status_label = Label(
    Window,
    text="Ready to record",
    font=("Arial", 12, "italic"),
    
)
status_label.grid(row=2, column=1, pady=10)


# ---------------- TRANSLATE FUNCTION ----------------


def Translate():

    import pyaudio
    import wave
    import threading
    import time

    # Recording settings
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 30

    def record_audio():

        audio = pyaudio.PyAudio()

        # Open microphone
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )

        frames = []

        # Countdown
        for remaining in range(RECORD_SECONDS, 0, -1):

            status_label.config(
                text=f"🔴 Recording...\n\n"
                     f"{remaining} seconds remaining"
            )

            # Record approximately one second
            start_time = time.time()

            while time.time() - start_time < 1:
                data = stream.read(
                    CHUNK,
                    exception_on_overflow=False
                )
                frames.append(data)

        # Stop microphone
        stream.stop_stream()
        stream.close()
        audio.terminate()

        status_label.config(
            text="⏹️ 30 seconds finished!\n\n🔎 Recognizing speech..."
        )

        # Save recording as WAV
        filename = "recording.wav"

        wave_file = wave.open(filename, "wb")
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b"".join(frames))
        wave_file.close()

        # Recognize speech
        r = sr.Recognizer()

        try:

            with sr.AudioFile(filename) as source:
                recorded_audio = r.record(source)

            text = r.recognize_google(recorded_audio)

            Output_text.delete("1.0", END)
            Output_text.insert(END, text)

            status_label.config(
                text="✅ Done!\nYour 30-second recording has been converted to text."
            )

        except sr.UnknownValueError:

            status_label.config(
                text="❌ I could not understand the recording."
            )

        except sr.RequestError as e:

            status_label.config(
                text=f"🌐 Google Speech Recognition error:\n{e}"
            )

        except Exception as e:

            status_label.config(
                text=f"⚠️ Error:\n{e}"
            )


    # Run recording in a separate thread
    threading.Thread(
        target=record_audio,
        daemon=True
    ).start()



    r = sr.Recognizer()

    try:

        # Step 1
        status_label.config(text="🎤 Opening microphone...")
        Window.update()

        with sr.Microphone() as source:

            # Step 2
            status_label.config(
                text="🔊 Adjusting for background noise...\nPlease remain quiet."
            )
            Window.update()

            r.adjust_for_ambient_noise(source, duration=1)

            # Step 3
            status_label.config(
                text="🗣️ Speak now!\nYou have up to 30 seconds."
            )
            Window.update()

            audio = r.listen(
                source,
                timeout=10,
                phrase_time_limit=30
            )

        # Step 4
        status_label.config(text="⏹️ Recording finished.")
        Window.update()

        # Step 5
        status_label.config(text="🔎 Recognizing your speech...")
        Window.update()

        text = r.recognize_google(audio)

        # Step 6
        Output_text.delete("1.0", END)
        Output_text.insert(END, text)

        status_label.config(
            text="✅ Done! Your speech has been converted to text."
        )

    except sr.WaitTimeoutError:

        status_label.config(
            text="⏰ No speech detected.\nPlease click the button and speak."
        )

    except sr.UnknownValueError:

        status_label.config(
            text="❌ I could not understand your voice.\nPlease try again."
        )

    except sr.RequestError as e:

        status_label.config(
            text="🌐 Could not connect to Google Speech Recognition."
        )

    except Exception as e:

        status_label.config(
            text=f"⚠️ Error: {e}"
        )


# ---------------- SAVE FUNCTION ----------------

def save():

    fout = asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if fout:

        print(Output_text.get("1.0", END), file=fout)
        fout.close()

        status_label.config(
            text="💾 Text saved successfully!"
        )

        messagebox.showinfo(
            "Success",
            "Text saved successfully!"
        )

    else:

        status_label.config(
            text="⚠️ Text was not saved."
        )


# ---------------- RECORD BUTTON ----------------

trans_btn = Button(
    Window,
    text="Click on me!\nTo start recording",
    font=("Arial", 15, "bold"),
    command=Translate,
    width=20,
    height=3
)

trans_btn.grid(
    row=1,
    column=0,
    pady=20,
    padx=20
)


# ---------------- SAVE BUTTON ----------------

save_button = Button(
    Window,
    text="Save the Text",
    width=20,
    height=4,
    command=save
)

save_button.grid(
    row=1,
    column=2,
    pady=10,
    padx=20
)


# ---------------- START GUI ----------------

Window.mainloop()

