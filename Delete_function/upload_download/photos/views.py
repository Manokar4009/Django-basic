from unicodedata import category
from django.shortcuts import render, redirect
from . models import Category, Photo, Csv
import os
import pandas as pd
import json
# Create your views here.
from django.http import HttpResponse



def gallery(request):
    #user = request.user
    #category = request.GET.get('category')
    #if category == None:
    #    photos = Photo.objects.filter(category__user=user)
    #else:
    #    photos = Photo.objects.filter(
    #        category__name=category, category__user=user)

    #categories = Category.objects.filter(user=user)
    categories = Category.objects.all()
    photos = Photo.objects.all()


    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewphoto(request, pk):
    photo = Photo.objects.get(id=pk)
    csv = Csv.objects.get(id=pk)
    print(csv.csvfile)
    df = pd.read_csv(csv.csvfile)
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    print(data)
	#context = {'d': data}
	#return render(request, 'table.html', context)
    text = {'photo': photo, 'd': data}
    return render(request, 'photos/photo.html', text)#{'photo': photo})

def addphoto(request):
    #user = request.user

    #categories = user.category_set.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
             #category, created = Category.objects.get_or_create(user=user, name=data['category_new'])
        else:
            category = None

        #for image in images:
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
        print(url)
        datas = {"key": url}
        member = Csv(csvfile=url)
        member.save()
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

def deleteItem(request, id):
    item = Photo.objects.get(id=id)
    item.delete()
    file = Csv.objects.get(id=id)
    file.delete()
    return redirect('gallery')

