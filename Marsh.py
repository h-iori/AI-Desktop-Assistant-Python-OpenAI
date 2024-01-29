import speech_recognition as sr
from Brain.MarshBrain import ReplyBrain
from Body.Speak import Speak
print(">>> Starting Marsh.... Please wait for few seconds. ")
from Body.Listen import MicExecution
print(">>> MarshAI is Getting Ready....")
from Main import MainTaskExecution
def MainExecution():
    Speak("Hello Sir")
    Speak(" What can i do for you?")


    while True:
         

         Data = MicExecution()

         Data= str(Data)
         ValueReturn = MainTaskExecution(Data)
         if ValueReturn== True:
             pass


         elif len(Data)<3:
             pass

         else:
            Reply= ReplyBrain(Data)

            Speak(Reply)


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language ="en")
    except:
        return ""
    query = str(query).lower()
    print(query)
    return query

def Wakeupdetected():
    queery= Listen().lower()
    if "wake up" in queery  :
        print(">>> Wake up detected >>>")
        MainExecution() 
    else:
        pass

while True:
     Wakeupdetected() 

