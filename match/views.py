from django.shortcuts import render
from dal import autocomplete
# from dal_select2 import Select2QuerySetView
from userProfile.models import Profile
from .models import Matches


def manual_match(request):
    return render(request, 'admin/matches/manualmatch.html', {})


class MatchAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated:
            # return Matches.objects.none()

        qs = Profile.objects.all()

        if self.q:
            qs = qs.filter(first_name__istartswith=self.q)

        return qs
