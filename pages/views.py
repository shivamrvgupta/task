from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def blogs(request):
    return render(request, 'pages/blog.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        message = request.POST['message']
        print('Enquiry Checking ---')

        # If user had made enquiry already

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                user_id=user_id)
            print("New Enquiry Sent ")
            if has_contacted:
                messages.error(
                    request, 'You have Already made an inquiry for this listing')
                print("Error has been sended")
                return redirect('/')

        contact = Contact(first_name=first_name,last_name=last_name,
                          email=email, phone=phone, message=message, user_id=user_id)
        print("Request been checked")
        contact.save()
        print("Request Saved")

        send_mail(
            'Service Enquiry',
            'There has been an enquiry .Sign into the admin pannel for more info',
            'shivamrvgupta@gmail.com',
            ['rvshivamsahu.1222@gmail.com'],
            fail_silently=False,
        )

        messages.success(
            request, 'Your request have been submitted, We will get back to you soon ')
        print("Message has been Sent")
        return redirect('/')
    return render(request, 'pages/contact.html')
