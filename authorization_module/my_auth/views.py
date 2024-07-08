from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from .models import CustomUser as User
from .forms import SignUpForm, LoginForm


# Create your views here.

def signup(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            mail_subject = f'{username}, Activate your account.'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            verification_link = request.build_absolute_uri(
                f'/activate/{uid}/{token}')
            message = f'''Hello {username},
            
            Please click the link below to verify your email and complete your registration:
            {verification_link}
            
            Regards,
            Atharva Kulkarni
            '''
            to_email = form.cleaned_data['email']
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            messages.success(
                request, 'Signup successful! Please check your email to verify your account.')
            return render(request, 'confirm_email.html')
        else:
            messages.error(request, form.errors)
            form = SignUpForm()
            context['form'] = form
    else:
        form = SignUpForm()
        context['form'] = form

    return render(request, 'signup.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (ValueError, TypeError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.email_verified = True
        user.save()
        django_login(request, user)
        return redirect('about')
    else:
        return render(request, 'activation_invalid.html')


def login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('about')
            else:
                messages.error(request, 'Username or Password is incorrect.')
                return redirect('login')
        else:
            messages.error(request, form.errors)
            form = LoginForm()
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, 'login.html', context)


@login_required
def about(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = User.objects.get(username=request.user.username)
        if not user.email_verified:
            logout(request)
            messages.error(request, 'Please verify your email before login.')
            return redirect('login')
    return render(request, 'about.html')
