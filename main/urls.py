from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.Login, name = 'login'),
    path('homepage/',views.Home,name='Home'),
    path('signup/',views.sign_up,name='signUp'),
    path('convert/',views.askconvert,name='convert'),
    path('logout/',views.Logout,name='logout'),
    path('audio_detail/<pk>',views.audio_detail,name='aud_detail'),
    path('audioDelete/<pk>',views.delete_audio,name='del_audio'),
    path('deletecomment/<pk>',views.deletecomment,name='deleteComment'),
    path('download_view/',views.download_view,name='download_view'),
    path('analysis/<pk>',views.Analytics,name='analysis'),
    path('audio_analysis/<pk>',views.Analysis,name='analytic'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "main/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "main/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "main/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "main/password_done.html"),name="password_reset_complete"),
]

urlpatterns+=staticfiles_urlpatterns()