import speech_recognition as sr

print("Starting microphone test...")

try:
    r = sr.Recognizer()

    print("Creating microphone...")
    mic = sr.Microphone()

    print("Microphone found!")
    print("Available microphones:")

    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(index, name)

except Exception as e:
    print("ERROR:")
    print(e)