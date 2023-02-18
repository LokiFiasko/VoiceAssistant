import speech_recognition as sr
import webbrowser


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    query = r.recognize_google(audio)
    print(f"You said: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Sorry, something went wrong: {e}")

