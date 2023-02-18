import speech_recognition as sr
import webbrowser

# Initialize the speech recognizer
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Use Google Speech Recognition to transcribe the audio
try:
    query = r.recognize_google(audio)
    print(f"You said: {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError as e:
    print(f"Sorry, something went wrong: {e}")

