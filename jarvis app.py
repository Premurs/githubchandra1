import pyttsx3
import speech_reconition
import datetime
import wikipedia
import webbrowser
import os
import comtype.client



engine = pyttsx3.init('sapi5')
voices = engine.get property('voice')
engine.setproperty('voice,voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning!')
    elif hour>=12 and <18:
        speak('good afternoon!')
    else:
        speak('good evening')
    speak('i am jarvis,please tell me how may i help you')    
def takecommand():
    r= sr.Recognzer()
    with sr.microphone() as source:
        print('listening...')
        r,pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.reconize_google(audio,language = 'en-in')
        print(f'user said:(query)/n')
    except Exception as e:
        print('say that again please...')
        return 'none'
if_name_=='_main_':
    wishme()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query:
            speak('searching wikipidea...')
            query=query.replace('wikipedia')
            result=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print('result')
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow'in query:
            webbrowser.open('stackoverflow.com')
        elif'play music' in query:
            music_dr='o//songs//favorits'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])
        elif 'the time'in query:
            strTime = datetime.datetime.now().strtime('XH:XM"XS')
            speak(f'sir,the time is {strTime}')
