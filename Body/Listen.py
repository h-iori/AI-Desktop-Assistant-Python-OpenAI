import speech_recognition as sr
import sys 
from deep_translator import GoogleTranslator
# Listen
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ="hi")
    except:
        return ""
    query = str(query).lower()
    return query
    
# Translation
def TranslationHintoEng(Text):
    line= str(Text)
    result = GoogleTranslator(source='auto', target='english').translate(line)
    data= result.lower()
    print(f"You :  {data}.")
    if "exit" in data or "goodbye" in data or "go to sleep" in data or "bye" in data or "get exited" in data or "see you later" in data or "farewell" in data:
        sys.exit()
    return data
#connecting the ears and translator

def MicExecution():

    query = Listen()
    data= TranslationHintoEng(query)
    return data
 
