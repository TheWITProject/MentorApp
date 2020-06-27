from django.shortcuts import render

def manual_match(request):
    return render(request, 'admin/matches/manualmatch.html', {})
