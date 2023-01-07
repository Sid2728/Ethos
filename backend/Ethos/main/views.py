from django.shortcuts import render,redirect
from .converter import Convert
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .converter import Convert
from django.core.files.base import ContentFile
from .models import upload
from django.shortcuts import render
import urllib.request
import secrets
import random
import string
from .ytdown import download

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/homepage/')
        else:
            # Display an error message
            pass
    return render(request, 'main/login.html')

def Logout(request):
    logout(request)
    return redirect('/')

def sign_up(request):
  
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        print('hello')
        if form.is_valid():
            print('hello')
        try: 
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
        except Exception as e:
            print(e)   

        return redirect('login')
    else:
        form = UserRegisterForm()
        

    return render(request, 'main/signup.html',{'form':form})
def Home(request):
    return render(request,'main/homepage.html')

def askconvert(request):

    if request.method=='POST':
        videom = request.FILES.get("vid")
      
        temp = upload()
        temp.video.save(videom.name,videom)
        temp.save()
        Convert("Ethos/backend/Ethos/main/media/"+videom.name)
    return render(request,'main/homepage.html')

def download_view(request):

    if request.method=='POST':
        url = request.POST.get("url")
        download(url)

    
        return render(request,'main/askConvert.html')


    return render(request, 'download.html', {'url': url})

