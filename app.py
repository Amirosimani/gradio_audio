# import gradio as gr
# import whisper

# # Load the Whisper model
# model = whisper.load_model("base")

# def transcribe(audio):
#     # Transcribe the audio
#     result = model.transcribe(audio)
#     return result['text']

# # Create the Gradio interface
# interface = gr.Interface(
#     fn=transcribe,
#     inputs=gr.Audio(type="filepath"),
#     outputs="text",
#     title="Audio Transcription App",
#     description="Record audio using your microphone and get a text transcription."
# )

# # Launch the app
# interface.launch()


import gradio as gr
from google.cloud import speech
from google.api_core.exceptions import GoogleAPICallError, InvalidArgument
import wave

def get_sample_rate(audio_file_path):
    with wave.open(audio_file_path, 'rb') as wf:
        return wf.getframerate()

def transcribe(audio):
    # Instantiates a client
    client = speech.SpeechClient()
    
    # Determine the sample rate from the audio file
    sample_rate_hertz = get_sample_rate(audio)

    try:
        # Loads the audio into memory
        with open(audio, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate_hertz,  # Use the sample rate from the audio file
            language_code="en-US",  # Adjust to your desired language
        )

        # Detects speech in the audio file
        response = client.recognize(config=config, audio=audio)

        # The first result's alternative is the most likely transcription
        if response.results:
            return response.results[0].alternatives[0].transcript
        else:
            return "No transcription found."
    
    except (GoogleAPICallError, InvalidArgument) as e:
        return f"Error occurred: {str(e)}"

# Create the Gradio interface
interface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Audio Transcription App",
    description="Record audio using your microphone and get a text transcription."
)

# Launch the app
interface.launch()
