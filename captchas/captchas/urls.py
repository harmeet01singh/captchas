from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home),
    path('funmath',views.fun_math),
    path('word', views.word_issue),
    path('time', views.time_based),
    path('nocaptcha', views.no_captcha),
    path('invisible', views.invisible),
    path('confident', views.confident),
    path('slider',views.slider)
]

urlpatterns += staticfiles_urlpatterns()