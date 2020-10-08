from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json
import requests
import random
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import string
from captcha.audio import AudioCaptcha

start = 0
rtext = ''
atext = ''

def home(request):
    captchas = [
        {
            'name': 'Fundamental Math',
            'description': 'A captcha structure appears with math issue, anticipating that you should understand and enter suitable reaction. The requests which are exceptionally clear, for instance, “1+2”, “8-3” can be difficult for robot to understand.',
            'image': './static/fundaMath.png'
        },
        {
            'name': 'Word Issue',
            'description': 'Test may ask you to retype confounding progression of letters, enter last word among various ones, or answer concealing that words appeared in.',
            'image': './static/issue.png'
        },
        {
            'name': 'Time Based',
            'description': 'Recording proportion of time that customers spend to complete structure is another effective kind of captcha.',
            'image': './static/time.jpeg'
        },
        {
            'name': 'Google Recaptcha',
            'description': 'This technique tracks turn of events and figures. Bots that are systematic will undoubtedly check compartment straightforwardly in inside while individuals will all in all snap in some various regions of case. Customers can complete this endeavor with no effort yet it exhibits hard for bots.',
            'image': './static/recaptchav2.png'
        },
        {
            'name': 'Audio Captcha',
            'description': 'Audio CAPTCHA is a reverse Turing test to discriminate the user as human or bot using audio as a medium. As W3C guidelines mandate the need of accessibility of web for people with disabilities like visual or motor impairment, audio CAPTCHA is an essential form of CAPTCHA for web security.',
            'image': './static/audio.png'
        },
        {
            'name': 'Confident Captcha',
            'description': 'Confident captcha is picture based procedure. It outfits selection of pictures with bearings. For example, customers are guided “click on each picture that has vehicle”. Not in any way like various kinds of captcha, web owner can adjust and use this captcha ',
            'image': './static/confi.png'
        },
        {
            'name': 'Slider Captcha',
            'description': 'Confident captcha is picture based procedure. It outfits selection of pictures with bearings. For example, customers are guided “click on each picture that has vehicle”. Not in any way like various kinds of captcha, web owner can adjust and use this captcha ',
            'image': './static/slider.png'
        }

    ]

    return render(request, 'home.html', { 'captchas': captchas })

def fun_math(request):
    # size = random.randint(10,16)
    # length = random.randint(4,8)
    # img = np.zeros(((size*2)+5, length*size, 3), np.uint8)
    # img_pil = Image.fromarray(img+255)

    # font = ImageFont.truetype(font='arial', size =size)
    # draw = ImageDraw.Draw(img_pil)
    # text = ''.join(
    #    random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) 
    #            for _ in range(length))
    # draw.text((5, 10), text, font=font, 
    #        fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    
    # cv2.imwrite(f"./static/funMath.png", img) #if you want to save the image
    # params = {'text': text}
    return render(request, 'funMath.html')

def word_issue(request):
    global rtext

    if request.method == 'POST':
        response = request.POST.get("captcha-text")

        if response == rtext:
            return render(request, 'success.html')
        else:
            return render(request, 'wordIssue.html', { 'message': 'Try Again' })

    size = random.randint(10,16)
    length = random.randint(4,8)
    img = np.zeros(((size*2)+5, length*size, 3), np.uint8)
    img_pil = Image.fromarray(img+255)

    # Drawing text and lines
    font = ImageFont.truetype('./static/arial.ttf', size =size)
    draw = ImageDraw.Draw(img_pil)
    text = ''.join(
        random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) 
                for _ in range(length))
    draw.text((5, 10), text, font=font, 
            fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw.line([(random.choice(range(length*size)), random.choice(range((size*2)+5)))
            ,(random.choice(range(length*size)), random.choice(range((size*2)+5)))]
            , width=1, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    # Adding noise and blur
    img = np.array(img_pil)
    thresh = random.randint(1,5)/100
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < thresh:
                img[i][j] = random.randint(0,123)
            elif rdn > 1-thresh:
                img[i][j] = random.randint(123,255)
    # img = cv2.blur(img,(int(size/random.randint(4,8)),int(size/random.randint(4,8))))
    rtext = text
    #Displaying image
    #cv2.imshow(f"{text}", img)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    cv2.imwrite(f"./static/wordissue.png", img)
    return render(request, 'wordIssue.html')

def time_based(request):
    global start

    if request.method == 'POST':
        response = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S') - start
        
        if response >= datetime.timedelta(seconds=10):
            return render(request, 'success.html')
        else:
            message = 'Response time is less then 10 seconds. Bot detected'
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

def audio(request):
    global atext
    if request.method == 'POST':
        response = request.POST.get("captcha-text")

        if response == atext:
            return render(request, 'success.html')
        else:
            return render(request, 'audio.html',{ 'message': 'Try Again' } )

    captcha_text = str(random.randint(1000,9999))
    audio_captcha = AudioCaptcha()
    audio_data = audio_captcha.generate(captcha_text)
    audio_captcha.write(captcha_text,'./static/cap.wav')
    atext = captcha_text
    return render(request, 'audio.html')

def confident(request):

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



    