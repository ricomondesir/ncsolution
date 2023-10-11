from django.shortcuts import render
from django.core.mail import send_mail

from django import forms
from captcha.fields import CaptchaField

# Create your views here.
def index(request):
    return render(request, "ncs/index.html")

def portfolio(request, id_portfolio):
 
    portfolio = id_portfolio

    return render(request, "ncs/portfolio.html", {
        "portfolio" : portfolio
    })

class CaptchaTestForm(forms.Form):
    captcha_field = CaptchaField()

def contact(request):
    form = CaptchaTestForm()
    if request.method == 'POST':
        name = request.POST['full-name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        form=CaptchaTestForm(request.POST)

        print('Is from valid :', form.is_valid())

        if form.is_valid():
        
            data = {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'message' : message
            }

            try:

                message = '''
                From: {}
                Name: {}
                Subject: {}
        
                New message: 
                {}

                '''.format(data['email'], data['name'], data['subject'], data['message'])
                send_mail(data['subject'], message, '', ['ncsayiti@gmail.com'])

                return render(request, "ncs/contact.html", {
                    "alert" : "success",
                    "message" : "Message sent!",
                    "form" : form,        
                })                 
            except: 
                return render(request, "ncs/contact.html", {
                    "alert" : "warning",
                    "message" : "Can not send e-mail at this time!",
                    "form" : form,
                })
        else:
            return render(request, "ncs/contact.html", {
                "alert" : "warning",
                "message" : "captcha input is empty or not valid",
                "form" : form,
            })            
    return render(request, "ncs/contact.html", {
        "form" : form,
    })

def team(request):
    return render(request, "ncs/team.html")

def asanka(request):
    return render(request, "ncs/asanka.html")