from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json
import requests
import random

start = 0

def home(request):
    return render(request, 'home.html')

def fun_math(request):
    return render(request, 'funMath.html')

def word_issue(request):
    return render(request, 'wordIssue.html')

def time_based(request):
    global start

    if request.method == 'POST':
        response = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S') - start
        
        if response >= datetime.timedelta(seconds=5):
            return render(request, 'success.html')
        else:
            message = 'Response time is less then 5 seconds. Bot detected'
            return render(request, 'time.html', { 'message': message })
    
    else:
        start = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
        return render(request, 'time.html')

def recaptcha(request):

    if request.method == 'POST':

        recaptcha_response = request.POST.get('g-recaptcha-response')
        values = {
            'secret': '6Le9ENIZAAAAALhQvsqSxA5zxljbFuvxCMUtZ_6-',
            'response': recaptcha_response
        }
        
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', params = values)
        print(r.url)
        response = r.json()

        print(response)

        if response['success']:
            return render(request, 'success.html')

        else:
            message = 'Invalid reCAPTCHA. Please try again.'
            return render(request, 'recaptcha.html', { 'message': message })

    else:
        return render(request, 'recaptcha.html')

def invisible(request):
    return render(request, 'invisible.html')

def confident(request):

    #link0 = 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/012015/bootstrap.png?itok=GTbtFeUj'
    #link1 = 'https://miro.medium.com/max/1200/1*1OBwwxzJksMv0YDD-XmyBw.png'
    #link1 = 'https://source.unsplash.com/1600x900/?building'
    #link2 = 'https://banner2.cleanpng.com/20180604/pol/kisspng-react-javascript-angularjs-ionic-atom-5b154be6709500.6532453515281223424611.jpg'
    #link3 = 'https://banner2.cleanpng.com/20180920/hq/kisspng-laravel-software-framework-web-framework-php-zend-laravel-software-framework-php-web-framework-model-5ba3437deb19e7.104986071537426301963.jpg'
    #link4 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/600px-Python-logo-notext.svg.png'
    #link5 = 'https://www.oracle.com/a/ocom/img/hp11-intl-java-logo.jpg'
    #link6 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTKWkic1-VG_92r8ZiioV4mRwveI8HHpQiHDg&usqp=CAU'
    #link7 = 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/012015/bootstrap.png?itok=GTbtFeUj'
    #link8 = 'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/012015/bootstrap.png?itok=GTbtFeUj'

    workset1 = ['lake','forest','Houses','motorcycles','trains','smartphones','fruits','highway','sportscar']
    img_gen = ['https://loremflickr.com/200/200/','https://source.unsplash.com/200x200/?']
    keywordset = []
    links = []

    for i in range(9):
        keyword = random.choice(workset1)
        link = random.choice(img_gen)+keyword
        keywordset.append(keyword)
        links.append(link)


    #links = [link0, link1, link2, link3, link4, link5, link6, link7, link8]
    category = random.choice(keywordset)
    params = {'object': 'default', 'links': links, 'category':category}
    return render(request, 'confident.html', params)

def slider(request):
    if request.method == 'POST':
        return render(request, 'success.html')
    else:
        return render(request, 'slider.html')

def success(request):
    return render(request, 'success,html')



    