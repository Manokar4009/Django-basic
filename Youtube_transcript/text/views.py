from django.shortcuts import render, redirect
from pytube import YouTube
from django.http import HttpResponse

import whisper

# Create your views here.
def index(request):
    link='https://www.youtube.com/watch?v=QTR4l60l910'
    try:
        yt = YouTube(link)
    except:
        print("Connection Error")
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(139)
    stream.download('',"./media/video/test.mp4")
    model = whisper.load_model("base")
    result = model.transcribe("./media/video/test.mp4")
    print(result['text'])
    return HttpResponse('hello world!')
    