from django.shortcuts import render, redirect
from pytube import YouTube
from django.http import HttpResponse
from .forms import transcriptForm
from .models import transcript
import os
import ffmpeg
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
    #model = whisper.load_model("base")
    #result = model.transcribe("./media/video/test.mp4")
    #print(result['text'])
    return HttpResponse('hello world!')

def sitemap(request):
    sitemapdocuments = transcript.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in sitemapdocuments:
        baseurls = obj.url
        info = obj.info
        #print(rank)
    print(baseurls)
    print(info)
    try:
        yt = YouTube(baseurls)
    except:
        print("Connection Error")
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.get_by_itag(139)
    stream.download('',"./media/video/test.mp4")
       #return HttpResponse("Hello, world!")
    return render(request, 'file.html', { 'sitemapdocuments': sitemapdocuments })

def sitemap_upload(request):
    if request.method == 'POST':
        form = transcriptForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            return redirect('sitemap')
    else:
        form = transcriptForm()
    return render(request, 'test.html', {
        'form': form
    })