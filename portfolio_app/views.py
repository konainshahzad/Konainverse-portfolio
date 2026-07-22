from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request, 'portfolio_app/home.html')
def projects(request):
    return render(request, 'portfolio_app/projects.html')
def contact (request):
    success = False
    error = False
    if request.method == "POST":
        name = request.POST.get("name") 
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        if name and email and subject and message:

            Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
            )
            success = True
        else:
            error = True
    return render(request, 'portfolio_app/contact.html', {
        'success': success,
        'error': error
})