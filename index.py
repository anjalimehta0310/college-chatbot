import wikipedia
import pyttsx3
import datetime
import webbrowser


class speech:

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.voice = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voice[1].id)
        self.engine.setProperty('rate',130)

    def speak(self,audioText):
        self.engine.say(audioText)
        self.engine.runAndWait()

class Response:

    def __init__(self,requestText):
        self.requestText = requestText

    def wishing_me(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            return 'good morning mam ,how can i help you'
        elif hour >= 12 and hour <= 18:
            return 'good afternoon mam,how can i help you'
        else:
            return 'good evening mam,how can i help you'

    def get_response(self):
        rt = self.requestText.lower()
        chat = ''
        if "name" in rt:
            chat = 'My name is INFOBOT and i am here to help you'
             
        elif rt == "inventor":
            chat = 'Anjali is my inventor.'
            
        elif rt == "how are you":
            chat = 'hey, i am fine bro.'
            
        elif "fee" in rt or "first year fee" in rt:
            chat = 'the fee for first year in sum of one lakh forty thousand'
            
        elif "registrar office" in rt or "register" in rt:
            chat = 'registrar office is in D block'
            
        elif "branches" in rt or "trades" in rt:
            chat = 'There is CSE,Mechanical,Electronic,CSE-DS,Civil,Electrical branches in our college'
            
        elif "Admin block" in rt or "account" in rt:
            chat = 'the admin block is in A block'
           
        elif "college website" in rt:
            webbrowser.open("https://www.rkgit.edu.in/")
            chat = 'opening RKGIT website'
            
        elif "hostel" in rt or "accomodation" in rt:
            webbrowser.open("https://rkgit.edu.in/upload/vacation%20of%20Hostel%20Accomodation")
            chat = 'wait a minute'
        
        else:
            try:
                result = wikipedia.summary(rt, sentence=4)
                chat = 'According to wikipedia {result}'
            except:
                chat = "sorry! default message."
        return chat