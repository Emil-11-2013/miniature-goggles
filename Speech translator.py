import speech_recognition as sr
import pyttsx3
from googletrans import Translator


def speak(text, lang="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')

    if lang == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = recognizer.listen(source)

    try:
        print("recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"{text}")
        return text
    except sr.RequestError as e:
        print("Could not request results from Google API. {0}".format(e))
        return "Error"


def translate(text: str, target_language: str = "es"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(translation.text)
    return translation.text


def display_lang_options():
    print("Select an option:")
    print("1. English")
    print("2. French")
    print("3. Spanish")
    print("4. Swedish")
    print("5. Hindi")
    print("6. Arabic")
    print("7. Bengali")
    print("8. Kannada")

    choice: int = int(input("Enter your option: "))
    lang_dict: dict[int, str] = {
        1: "English",
        2: "French",
        3: "Spanish",
        4: "Swedish",
        5: "Hindi",
        6: "Arabic",
        7: "Bengali",
        8: "Kannada"
    }
    return lang_dict.get(choice, "es")


def main(target_language="es"):
    target_language = display_lang_options()
    original_text: str = speech_to_text()

    if original_text:
        translated_text = translate(original_text, target_language)
        speak(translated_text, lang="en")
        print(f"Translated text: ", translated_text)


if __name__ == "__main__":
    main()
