from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from gtts import gTTS
import os

def text_to_speech(request):
    audio_url = None
    if request.method == "POST":
        text = request.POST.get("text","")
        # Create the media directory if it doesn't exist
        
        media_dir = os.path.join("media")
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        
        #Text to speech program
        texttospeech = gTTS(text=text,lang="en")
        audio_path = os.path.join(media_dir,"audio.mp3")
        texttospeech.save(audio_path)
        
        # Set the audio URL to be used in the template
        audio_url = os.path.join("media","audio.mp3")
        audio_url_wav = os.path.join("media","audio.wav")
        audio_url_ogg = os.path.join("media","audio.ogg")
        
    
        
        # #Using the audio file
        # with open(audio_path,"rb") as audio_file:
        #     response = HttpResponse(audio_file.read(),content_type="audio/mpeg")
        #     response["Content_Disposition"] = "inline;filename=audio.mp3"
        #     return response
        
    
    return render(request, "text_to_speech.html",{"audio_url":audio_url})