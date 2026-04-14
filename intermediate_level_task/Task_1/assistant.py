import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def run_assistant():
    speak("Hello, I am your QSkill assistant. How can I help you today?")
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'github' in command:
            speak("Opening your GitHub profile")
            webbrowser.open("github.com")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye! Have a productive day.")
            break

if __name__ == "__main__":
    run_assistant()
