from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from yearUpApp.forms import SignUpForm
from yearUpApp.tokens import account_activation_token
from django.http import HttpResponse
from django.core.mail import EmailMessage


@login_required
def home(request):
    return render(request, 'yearUpApp/home.html')

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.user_choice = form.cleaned_data.get('user_choice')
        current_site = get_current_site(request)
        subject = 'Activate Your MySite Account'
        message = render_to_string('yearUpApp/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)

        return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'yearUpApp/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'yearUpApp/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'yearUpApp/account_activation_invalid.html')


