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
from survey.models import Response, Survey
from userProfile.models import FrequentlyAsked, FrequentlyAskedMentor
from django.views.generic.edit import FormView
from match.models import Matches
from userProfile.models import Profile

@login_required
def home(request):
    user_id = User.objects.get(username=request.user).pk
    print(user_id)
    completed = len(Survey.objects.filter(id__in=Response.objects.filter(user_id=user_id).values_list('survey_id')).filter(is_published = True))
    active_survey = [len(Survey.objects.exclude(id__in=Response.objects.filter(user_id=user_id).values_list('survey_id')).filter(is_published = True))]
    not_completed = tuple(Survey.objects.exclude(id__in=Response.objects.filter(user_id=user_id).values_list('survey_id')).filter(is_published = True))
    not_completed = tuple(Survey.objects.exclude(id__in=Response.objects.filter(user_id=user_id).values_list('survey_id')).filter(is_published = True))

    match_model_user = Matches.objects.get(user_id=user_id)
    match_model_match = Profile.objects.get(user_id=match_model_user.match_id)
    print(match_model_match)

    args = {'surveys': not_completed, 'active': active_survey,'match':match_model_match}
    return render(request, 'pages/home.html',args)

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
            message = render_to_string('registration/account_activation_email.html',{
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
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        user.profile.save()
        login(request, user)
        return redirect('edit_profile')
    else:
        return render(request, 'registration/account_activation_invalid.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        print(request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        # add_form = AdditionalQuestionsForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid() :
            profile_form.save()
            # add_form.save()
            return redirect("profile")
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        # add_form = AdditionalQuestionsForm(instance=request.user.profile)
    return render(request, 'pages/edit_profile.html', {
        'profile_form': profile_form,
        # 'add_form': add_form
    })

    
@login_required
def profile(request):
    # form = ProfileForm(request.POST)
    # args = {'form':form}
    # if form.is_valid():
    #     user = ProfileForm(instance = request.user)
    # return render(request, 'pages/profile.html', args)
    form = ProfileForm(instance=request.user.profile)
    all_surveys = tuple(Survey.objects.all().filter(is_published = True))
    return render(request, 'pages/profile.html', {'form':form, 'allsurveys':all_surveys})

def set_notifications(request):
    if request.user.is_authenticated:
        user_id = User.objects.get(username=request.user).pk
        context = {}
        context["notifications"] = tuple(Survey.objects.exclude(id__in=Response.objects.filter(user_id=user_id).values_list('survey_id')).filter(is_published = True))
        context["current_page"] = request.path
        return context
    context = {}
    return context

def faq_page(request):
    faq_objects = FrequentlyAsked.objects.all()
    faq_mentor_objects = FrequentlyAskedMentor.objects.all()
    args = {}
    if faq_objects:
        args["faq_objects"] = faq_objects
    if faq_mentor_objects:
        args["faq_mentor_objects"] = faq_mentor_objects
    return render(request, 'pages/faq.html', args)
