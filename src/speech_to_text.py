import sounddevice as sd
from scipy.io.wavfile import write
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SAMPLE_RATE = 16000
DURATION = 5


def record_audio():
    print("Speak now...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("recording.wav", SAMPLE_RATE, audio)

    print("Recording saved.")



def transcribe_audio():
    with open("recording.wav", "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="text"
        )

    print("\nRecognized Text:")
    print(transcription)

    return transcription



if __name__ == "__main__":
    record_audio()
    transcribe_audio()