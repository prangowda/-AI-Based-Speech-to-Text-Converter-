import deepspeech
import numpy as np
import pyaudio
import wave
import speech_recognition as sr

# Load DeepSpeech model
model_file_path = "deepspeech-0.9.3-models.pbmm"
scorer_file_path = "deepspeech-0.9.3-models.scorer"
model = deepspeech.Model(model_file_path)
model.enableExternalScorer(scorer_file_path)

# Function to record and recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("📝 Converting speech to text...")
        text = recognizer.recognize_google(audio)
        print("📝 Recognized Text: ", text)
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand the audio!")
    except sr.RequestError:
        print("❌ Could not request results, check your internet!")

if __name__ == "__main__":
    recognize_speech()
