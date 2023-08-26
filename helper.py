from index import Response
from index import speech
speech = speech()
while True:
    me = str(input("enter the first chat:"))
    if "hi" in me or "hello" in me:
        res = Response(me)
        alex = res.wishing_me()
    else:
        res = Response(me)
        alex = res.get_response()
    print(alex)
  
    speech.speak(alex) 

