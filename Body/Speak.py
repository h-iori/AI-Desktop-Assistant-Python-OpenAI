import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[2].id)
    engine.setProperty('rate',160)
    print("")
    print(f"Marsh : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

