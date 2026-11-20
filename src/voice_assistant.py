
from src.speech_to_text import record_audio, transcribe_audio
from src.llm_brain import get_ai_response
from src.text_to_speech import speak_text


def run_assistant():

    # Step 1: Record user's voice
    record_audio()

    # Step 2: Convert voice into text
    user_text = transcribe_audio()

    # Step 3: Validate recognized text
    if not user_text or not user_text.strip():
        print("No speech detected. Please try again.")
        return

    # Step 4: Send text to AI
    ai_response = get_ai_response(user_text)

    # Step 5: Display AI response
    print("\nAI Assistant:")
    print(ai_response)

    # Step 6: Speak AI response
    speak_text(ai_response)


if __name__ == "__main__":
    run_assistant()
