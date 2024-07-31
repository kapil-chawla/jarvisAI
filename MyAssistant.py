import speech_recognition as sr
import pyttsx3
import openai
import time
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set OpenAI API key
openai.api_key = ''

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def set_alarm(time_str):
    alarm_time = datetime.datetime.strptime(time_str, "%H:%M").time()
    speak(f"Setting an alarm for {time_str}.")
    while True:
        current_time = datetime.datetime.now().time()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            speak("It's time!")
            break
        time.sleep(30)

def add_to_do_item(item):
    with open("todo_list.txt", "a") as file:
        file.write(f"{item}\n")
    speak(f"Added {item} to your to-do list.")

def main():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()
        if 'search for' in command:
            query = command.replace('search for', '')
            speak(f"Searching for {query}.")
            response = get_chatgpt_response(query)
            speak(response)
        elif 'set an alarm' in command:
            time_str = command.replace('set an alarm for', '').strip()
            set_alarm(time_str)
        elif 'add to my to-do list' in command:
            item = command.replace('add to my to-do list', '').strip()
            add_to_do_item(item)
        elif 'exit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
