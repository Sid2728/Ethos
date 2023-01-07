from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name = 'login'),
    path('homepage/',views.Home,name='Home'),
    path('signup/',views.sign_up,name='signUp'),
    path('convert/',views.askconvert,name='convert'),
    path('download_view/',views.download_view,name='download_view'),
    path('logout/',views.Logout,name='logout'),
    path('allaudio/',views.Allaud,name='allaud')
]