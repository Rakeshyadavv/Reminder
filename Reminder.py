import pyttsx3
from datetime import datetime
import time


class Reminder:
    def speak(self):
        engine = pyttsx3.init()
        current_time = datetime.now().strftime('%I:%M %p')
        print(current_time)
        reminder_message = f"Take some rest, you are working since last 30 minute"

        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-50)

        volume = engine.getProperty('volume')
        engine.setProperty('volume',volume+0.50)

        engine.say(reminder_message)
        engine.runAndWait()

ob1 = Reminder()
while True:
    count =0
    while count<10:
        ob1.speak()
        time.sleep(3)
        count = count+1
    time.sleep(5)
    time.sleep(1800)
    
   