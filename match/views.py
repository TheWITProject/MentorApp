from django.shortcuts import render, redirect
# from dal import autocomplete
from django.contrib.auth.models import User
from django.http import JsonResponse
#from dal_select2 import Select2QuerySetView
from userProfile.models import Profile
from .models import Matches
from .serializers import *



def manual_match(request):
    return render(request, 'admin/matches/manualmatch.html', {})


def match_autocomplete(request):
	print("uh oh")
	if not request.user.is_authenticated:
		return Profile.objects.none()


	if request.method == 'GET' and 'term' in request.GET:
		print("reached here after if")
		qs = Profile.objects.filter(first_name__istartswith=request.GET.get('term')) | Profile.objects.filter(last_name__istartswith=request.GET.get('term'))
		titles = list()

		for var in qs:
            # titles.append(var.first_name + var.last_name)
			titles.append(var.user.username + " | " + var.first_name + " "+var.last_name)

		return JsonResponse(titles, safe=False)
	else:
		print(request.GET)

	return render(request, 'admin/matches/manualmatch.html')

def handle_manual(request):
    print(request)
    print(request.POST["mentor-search"].find("|"))
    print(request.POST["mentor-search"].split()[0])
    print(request.POST["student-search"])
    print(request.POST["student-search"].find("|"))
    if((request.POST["mentor-search"].find("|") ==-1) | (request.POST["student-search"].find("|") == -1)):
        print("oopsie daisey")
    else:
        mentor_name = request.POST["mentor-search"].split()[0]
        student_name = request.POST["student-search"].split()[0]
        id_mentor = User.objects.get(username = mentor_name).pk
        id_student = User.objects.get(username = student_name).pk
        print(id_mentor)
        print(id_student)
        dict = [{'user_id': id_mentor, 'match_id': id_student}, {'user_id': id_student, 'match_id': id_mentor}]
        # b = {}
        # b['user_id'] = id_mentor
        # b['match_id'] = id_student
        # other = []
        # other.append(b)
        # print(other)
        print(dict)
        serializer = MatchesSerializer_manual(data=dict, many=True)
        print("SERIALIECE")
        if serializer.is_valid():
            print("HELOOOOOOO")
            matches_save = serializer.save()
            print("MATCHES MADE")
            # self.message_user(request, "Matches have been made")
        else:
            # self.message_user(request, "Matches have NOT been made")
            print("MATCHES NOT MADE")
            print(serializer.errors)
    return redirect('../admin/match/matches')



#class MatchAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
#        if not self.request.user.is_authenticated:
#            return Profile.objects.none()

#        qs = Profile.objects.all()

#        if self.q:
#            qs = qs.filter(first_name__istartswith=self.q)

#        return qs
