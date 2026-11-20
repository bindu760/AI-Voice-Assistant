
import pyttsx3


engine = pyttsx3.init()

# Set speaking speed
engine.setProperty("rate", 175)

# Set volume (0.0 to 1.0)
engine.setProperty("volume", 1.0)


def speak_text(text):

    print("\nSpeaking...")

    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    speak_text("Hello! I am your AI voice assistant.")
