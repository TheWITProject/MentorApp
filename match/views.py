from django.shortcuts import render
from dal import autocomplete
from django.http import JsonResponse
#from dal_select2 import Select2QuerySetView
from userProfile.models import Profile
from .models import Matches


def manual_match(request):
    return render(request, 'admin/matches/manualmatch.html', {})


def match_autocomplete(request):
	print("uh oh")
	if not request.user.is_authenticated:
		return Profile.objects.none()


	if request.method == 'GET' and 'term' in request.GET:
		print("reached here after if")
		qs = Profile.objects.filter(first_name__istartswith=request.GET.get('term'))
		titles = list()

		for var in qs:
			titles.append(var.user.username)

		return JsonResponse(titles, safe=False)
	else:
		print(request.GET)

	return render(request, 'admin/matches/manualmatch.html')



#class MatchAutocomplete(autocomplete.Select2QuerySetView):
#    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
#        if not self.request.user.is_authenticated:
#            return Profile.objects.none()

#        qs = Profile.objects.all()

#        if self.q:
#            qs = qs.filter(first_name__istartswith=self.q)

#        return qs
