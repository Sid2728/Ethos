from django.shortcuts import render,redirect
from .converter import Convert
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core.files.base import ContentFile
from .models  import upload
from django.http import HttpResponse
from django.contrib import messages
import urllib.request
import secrets
import random
from functools import wraps
from django.core.files.storage import default_storage
import string
from .ytdown import download
from . models import Audio,TimeStamp
from . models import Audio
from .sentiment import printAnalysis
# from django.contrib.auth.decorators import login_required

def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Send a warning message
            messages.warning(request, "Please log in to access this page.")
            # Redirect to login page
            return redirect('login')  # Replace 'login' with your login URL name
        
        # User is authenticated, proceed with the original view function
        return view_func(request, *args, **kwargs)

    return wrapped_view


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage/')
        else:
            messages.warning(request,"Incorrect username and/or password")
            return redirect('login')
    return render(request, 'main/login.html')

@login_required
def Logout(request):
    logout(request)
    return redirect('/')

def sign_up(request):
  
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        # print('hello')
        if form.is_valid():
            # print('hello')
            pass
        try:  
            form.save()
            username=form.cleaned_data.get('username')
            print("account created")
            messages.success(request,f'Account created for {username}')
        except Exception as e:
            print(e)   

        return redirect('login')
    else:
        form = UserRegisterForm()
        

    return render(request, 'main/signup.html',{'form':form})

@login_required
def Home(request):
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    # print(allaudios)
    context = {
            'allaudios':allaudios
        }
    return render(request,'main/homepage.html',context)

@login_required
def askconvert(request):

    if request.method=='POST':
        videom = request.FILES.get("vid")
        temp = upload()
        temp.video.save(videom.name.strip().replace(" ","_"),videom)
        temp.save()
        id = Convert("main/media/"+videom.name.strip().replace(" ","_"),request,temp.id)
        temp.delete()
        allaudios = Audio.objects.filter(uploaded_by=request.user.id)
        context = {
            'allaudios':allaudios
        }
        if id==-1:
            return render(request,'main/noaudio.html')
        return redirect('/audio_detail/'+ str(id))
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    print(allaudios)
    context = {
            'allaudios':allaudios
        }
    return render(request,'main/homepage.html',context)

@login_required
def download_view(request):
    
    if request.method=='POST':
        url = request.POST.get("url")
        id = download(url,request)
        if id != -1:
            return redirect('/audio_detail/'+ str(id))
        else:
            return render(request,'main/noaudio.html') 

    return render(request, 'download.html', {'url': url})

@login_required
def audio_detail(request,pk):
    audio = Audio.objects.get(id=pk)
    print(request.POST.get('time'))
    if request.POST:
        timestamp = TimeStamp()
        timestamp.audio = audio
        timestamp.comment = request.POST.get('comment')
        timestamp.time = '00:' + request.POST.get('time')
        timestamp.save()
    comments = TimeStamp.objects.filter(audio = audio.id).order_by("time").values()
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    context = {
        'comments':comments,
        "audio":audio,
        'allaudios':allaudios,
    }
    return render(request,'main/pagetwo.html',context)

def editname(request,pk):
    audio = Audio.objects.get(id=pk)
    audio.audioname=request.POST.get('editname')
    audio.save()
    context = {
        "audio":audio,
    }
    return render(request,'main/pagetwo.html',context)

@login_required
def audio_display(request,pk):
    audio = Audio.objects.get(id=pk)
    timestamp=TimeStamp.objects.filter(audio=audio).all()
    allaudios = Audio.objects.filter(uploaded_by=request.user.id)
    context={
        'timestamp':timestamp,
        'allaudios':allaudios,
        'pk':pk,
        "audio":audio
    }
    return render(request,'main/detail.html',context)

@login_required
def deletecomment(request,pk):
    if request.method=='POST':
        print(pk)
        tst=TimeStamp.objects.get(pk=pk)
        tst.delete()
        id=request.POST.get('hiddenfield')
        
    return redirect('/audio_detail/' + str(id))

@login_required
def delete_audio(request,pk):
    audio = Audio.objects.get(id=pk,uploaded_by=request.user)
    path='./main/static'+audio.audioFile.url
    print(path,default_storage.exists(path))
    default_storage.delete(path)
    audio.delete()
    return redirect('/homepage/')

@login_required
def Analytics(request,pk):
    # print(getURL(request))
    audio = Audio.objects.get(id=pk)
    print(audio.url)
    if audio.positive==0 and audio.negative==0 and audio.neutral==0:
        printAnalysis(request,Audio.objects.get(id=pk).url)
    return redirect('/audio_analysis/' + str(pk))

@login_required
def Analysis(request, pk):
    audio = Audio.objects.get(id=pk)
    if audio.negative + audio.positive != 0:
        pr = audio.positive / (audio.negative + audio.positive)
    else:
        pr = 0.0

    context = {
        'positive': audio.positive,
        'negative': audio.negative,
        'neutral': audio.neutral,
        'ratio': pr
    }
    return render(request, 'main/analytics.html', {'context': context})