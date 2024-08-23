import gradio as gr
import whisper

# Load the Whisper model
model = whisper.load_model("base")

def transcribe(audio):
    # Transcribe the audio
    result = model.transcribe(audio)
    return result['text']

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
