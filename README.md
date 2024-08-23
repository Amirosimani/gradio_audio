# Enable the Speech-to-Text API.

1. Create a service account key and download the JSON key file.
2. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of your JSON key file. For example:
`export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-file.json"`



pyhon app.py


-----------
# dev locally on linux
If the mic is not recognized, follow this steps

1. installto manage your audio devices. 
`sudo apt-get install pavucontrol`
2. then run `pavucontrol` and make sure your mic is listed and is not muted.
3. verify mic works in python
   3.1 If you are getting error installing `PyAudio`, you might need to do this first `sudo apt-get install portaudio19-dev` and install 
   
```
    import speech_recognition as sr

    recognizer = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()

    print("Available microphones:")
    for index, name in enumerate(mic_list):
        print(f"{index}: {name}")
```
