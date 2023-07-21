from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def main(request):
    return render(request, "index.html")

def resume(request):
    return render(request, "resume.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Perform any validation if needed

        # Send email
        subject = 'New Contact Form Submission'
        body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        from_email = f'{email}' 
        to_email = 'silvansowino1@gmail.com'  
        send_mail(subject, body, from_email, [to_email])

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)

    