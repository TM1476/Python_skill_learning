import pyttsx3
import datetime
import pyjokes
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def get_text_command():
    print("\n" + "="*30)
    query = input("Enter Command (time/joke/open google/exit): ")
    return query.lower()

def run_assistant():
    speak("Hello, I am your Q-Skill assistant. Since the microphone is offline, please type your commands.")
    
    while True:
        command = get_text_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye! Have a productive day.")
            break
        
        elif command == "":
            continue
            
        else:
            speak("I'm not sure how to do that yet.")

if __name__ == "__main__":
    run_assistant()
