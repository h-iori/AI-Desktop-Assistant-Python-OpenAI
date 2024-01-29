import keyboard
import pyautogui
import webbrowser
import requests
from Body.Speak import Speak
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
    
    elif "search" in Query:
        Nameofweb = Query.replace("search ","")
        Link = f"{Nameofweb}"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
    
    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
    
    elif "temperature" in Query:
        def trim_left(Query, word):
            index = Query.find(word)
            if index != -1:
                return Query[index:]
            else:
                return Query
        a= trim_left(Query, 'temperature')
        tempofcity= a
        url = f"https://www.google.com/search?q={tempofcity}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', attrs={'class': 'BNeawe'}).text
        ans= f"The current temperature is {data}"
        Speak(ans)
        return True
    
    elif "weather" in Query:
        def trim_left(Query, word):
            index = Query.find(word)
            if index != -1:
                return Query[index:]
            else:
                return Query
        a= trim_left(Query, 'weather')
        weathofcity= a
        url = f"https://www.google.com/search?q={weathofcity}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('div', attrs={'class': 'BNeawe'}).text
        weath_res= f"The current temperature is {data}"
        Speak(weath_res)
        return True
    
    elif " date " in Query and " time " in Query:
        now = datetime.now()  # returns date in 'YYYY-MM-DD' format
        date= now.strftime("%d-%B-%y") 
        now1 = datetime.now()
        time= now1.strftime("%I:%M %p")
        Speak(f"the current date is {str(date)} " , f"and the current time is {str(time)}" )
        return True
    
    elif "present date" in Query or "current date" in Query or "what is the date" in Query or "whats the date" in Query or "what's the date" in Query or "what date it is" in Query or "what date is it" in Query:    
        now = datetime.now() # returns date in 'YYYY-MM-DD' format
        date= now.strftime("%d-%B-%y") 
        Speak(f"the current date is {str(date)}")
        return True
    
    elif "present time" in Query or "current time" in Query or "what is the time" in Query or "whats the time" in Query or "what's the time" in Query or "what time it is" in Query or "what time is it" in Query:
        now1 = datetime.now()
        time= now1.strftime("%I:%M %p")  # returns date in 'YYYY-MM-DD' format
        Speak(f"the current time is {str(time)}") 
        return True
    
    
    

  