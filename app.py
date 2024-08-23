import gradio as gr
import speech_recognition as sr

def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Sorry, I could not understand the audio."
        except sr.RequestError:
            text = "Could not request results; check your network connection."
    return text

gr.Interface(
    fn=transcribe_audio, 
    inputs=gr.Audio(type="filepath"),  # Remove the source argument
    outputs="text",
    title="Speech to Text Transcription",
    description="Speak into the microphone and get the transcribed text below."
).launch()
