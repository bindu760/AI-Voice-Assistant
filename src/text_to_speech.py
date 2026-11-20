import pyttsx3
import markdown
from bs4 import BeautifulSoup

engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


def clean_text_for_speech(text):

    # Convert Markdown into HTML
    html = markdown.markdown(text)

    # Extract plain text from HTML
    soup = BeautifulSoup(html, "html.parser")

    # Get only readable text
    clean_text = soup.get_text(separator=" ")

    return clean_text


def speak_text(text):

    clean_text = clean_text_for_speech(text)

    print("\nSpeaking...")

    engine.say(clean_text)
    engine.runAndWait()


if __name__ == "__main__":
    speak_text("Hello! I am your AI voice assistant.")