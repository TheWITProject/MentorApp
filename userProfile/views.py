from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from userProfile.forms import *
from userProfile.tokens import account_activation_token

@login_required
def home(request):
    return render(request, 'pages/home.html')

def logout_view(request):
	logout(request)
	return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()


            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


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
        return redirect('profile')
    else:
        return render(request, 'registration/account_activation_invalid.html')



@login_required
def edit_profile(request):
    if request.method == 'POST':
        #user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            #user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return render(request,'pages/profile.html',{'profile_form': profile_form})
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        #user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'pages/edit_profile.html', {
        #'user_form': user_form,
        'profile_form': profile_form
    })



@login_required
def profile(request):
    form = ProfileForm(request.POST)
    args = {'form':form}
    if form.is_valid():
        user = ProfileForm(instance = request.user)
    return render(request, 'pages/profile.html', args)