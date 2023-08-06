from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, "ncs/index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['full-name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }

        try:

            message = '''
            New message: {}

            From: {}
            '''.format(data['message'], data['email'])
            send_mail(data['subject'], message, '', ['ncsayiti@gmail.com'])

            return render(request, "ncs/contact.html", {
                "alert" : "success",
                "message" : "Message sent!"        
            })                 
        except: 
            return render(request, "ncs/contact.html", {
                "alert" : "warning",
                "message" : "Can not send e-mail at this time!"
            })
    return render(request, "ncs/contact.html")

def team(request):
    return render(request, "ncs/team.html")

def asanka(request):
    return render(request, "ncs/asanka.html")