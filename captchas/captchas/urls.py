from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home),
    path('funmath',views.fun_math),
    path('word', views.word_issue),
    path('time', views.time_based),
    path('recaptcha', views.recaptcha),
    path('audio', views.audio),
    path('confident', views.confident),
    path('slider',views.slider),
    path('success',views.success)
]

urlpatterns += staticfiles_urlpatterns()