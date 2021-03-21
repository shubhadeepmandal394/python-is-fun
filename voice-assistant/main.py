import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_instructions():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(command)
    except:
        pass
    return command


def run_assistant():
    command = take_instructions()
    print(command)
    if 'date' in command:
        date = datetime.datetime.now().strftime('%d %M %Y')
        day = datetime.datetime.now().strftime('%A')
        talk(date + 'and today is' + day)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('you are most welcome')
    else:
        talk('Pardon Me, Can you please say that again ?')


while True:
    run_assistant()