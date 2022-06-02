from django.core.mail import send_mail

def send_verification_email(user):
    send_mail(
        'Verify your account',
        fail_silently=True,
        
    )