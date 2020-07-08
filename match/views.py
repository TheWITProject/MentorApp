from django.shortcuts import render, redirect
# from dal import autocomplete
from django.http import HttpResponse

from urllib import request
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
#from dal_select2 import Select2QuerySetView
# from django.core.exceptions import ValidationError
from userProfile.models import Profile
from .models import Matches
from .serializers import *
from django.utils.translation import ugettext_lazy as _


def manual_match(request):
    return render(request, 'admin/matches/manualmatch.html', {})

def match_autocomplete_mentor(request):
	if not request.user.is_authenticated:
		return Profile.objects.none()

	if request.method == 'GET' and 'term' in request.GET:
		qs = (Profile.objects.filter(first_name__istartswith=request.GET.get('term')) | Profile.objects.filter(last_name__istartswith=request.GET.get('term'))).filter(user_type="IS_MENTOR")
		titles = list()

		for var in qs:
			titles.append(var.user.username + " | " + var.first_name + " "+var.last_name)

		return JsonResponse(titles, safe=False)
	else:
		print(request.GET)

	return render(request, 'admin/matches/manualmatch.html')

def match_autocomplete_student(request):
	if not request.user.is_authenticated:
		return Profile.objects.none()

	if request.method == 'GET' and 'term' in request.GET:
		qs = (Profile.objects.filter(first_name__istartswith=request.GET.get('term')) | Profile.objects.filter(last_name__istartswith=request.GET.get('term'))).filter(user_type="IS_MENTEE")
		titles = list()

		for var in qs:
			titles.append(var.user.username + " | " + var.first_name + " "+var.last_name)

		return JsonResponse(titles, safe=False)
	else:
		print(request.GET)

	return render(request, 'admin/matches/manualmatch.html')

def handle_manual(request):
    if((request.POST["mentor-search"].find("|") ==-1) | (request.POST["student-search"].find("|") == -1)):
        messages.error(request, _('INVALID USER(S) INPUTED'))
    else:
        mentor_name = request.POST["mentor-search"].split()[0]
        student_name = request.POST["student-search"].split()[0]
        id_mentor = User.objects.get(username = mentor_name).pk
        id_student = User.objects.get(username = student_name).pk
        dict = [{'user_id': id_mentor, 'match_id': id_student}, {'user_id': id_student, 'match_id': id_mentor}]
        serializer = MatchesSerializer_manual(data=dict, many=True)
        if serializer.is_valid():
            matches_save = serializer.save()
            print("MATCHES MADE")
        else:
            print("MATCHES NOT MADE")
            print(serializer.errors)
    return redirect('../admin/match/matches')