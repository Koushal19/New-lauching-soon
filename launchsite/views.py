from django.shortcuts import render,redirect
from .models import Student_Detail
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
# Create your views here.
def frontpage(request):
    if request.method=="POST":
        name=request.POST.get('name')
        college_name=request.POST.get('college_name')
        email=request.POST.get('email')

        student= Student_Detail.objects.create(name=name,college_name=college_name,email=email)
        student.save()


        send_thank_you_email(name, email)
        messages.success(request, 'Thank you for successfully registering!')
        return redirect('frontpage')        

    return render(request, 'launchsite/frontpage.html')


def send_thank_you_email(name, email):
    subject = "Thank You for Registering!"
    message = f"Hi {name},\n\nThank you for registering.ThinkUni is a Student Marketplace where we host products and sevices as a one stop solution to all your student needs , to help students have a hassle free Unidays.Stay tuned for more updates!\n\nBest regards,\nThinkUni Team"
    from_email = settings.EMAIL_HOST_USER  
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)



