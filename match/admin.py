from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.http import HttpResponseRedirect
from match.models import *
from userProfile.models import Profile
from .serializers import MatchesSerializer
from django.http import HttpResponse


import requests
import pandas as pd
import json
import os
import csv

class MatchesAdmin(admin.ModelAdmin):
    change_list_template = "admin/matches/buttons.html"
    list_display = ("user_id", "name", "last_name","match_first_name", "match_last_name")
    #readonly_fields = ("user_id", "match_id", "name", "last_name","match_first_name", "match_last_name")
    actions = ['export_matches']
    

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('makematches/', self.make_matches),
        ]
        return my_urls + urls

    def make_matches(self, request):
        r = requests.get('http://127.0.0.1:8000/survey/json/4')
        r.json()
        x = requests.post('http://127.0.0.1:8000/api/v1/mentor_match_classifier/predict', json = r.json())
        
        print(x.json())
        match_json = x.json()

        mid_json = match_json['matches']
        mock_json = pd.read_json(mid_json, orient = 'records')
        print(type(mock_json))
        dict_json = mock_json.to_dict('records')

        serializer = MatchesSerializer(data=dict_json, many=True)
        if serializer.is_valid():
            matches_save = serializer.save() 
            self.message_user(request, "Matches have been made")
        else:
            self.message_user(request, "Matches have NOT been made")
            print(serializer.errors)
        return HttpResponseRedirect("../")

    def export_matches(self, request, queryset):

        f = open('some.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(["User ID", "Username", "User's First Name", "User's Last Name","Match ID", "Match's First Name", "Match's Last Name"])

        for s in queryset:
            writer.writerow([s.user_id, Profile.objects.get(user_id=s.user_id), Profile.objects.get(user_id=s.user_id).first_name, Profile.objects.get(user_id=s.user_id).last_name, s.match_id, Profile.objects.get(user_id=s.match_id).first_name, Profile.objects.get(user_id=s.match_id).last_name])
        
        f.close()
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = matches.csv'
        self.message_user(request, "Matches have been downloaded")

        return response
        

    def name(self, obj):
        return Profile.objects.get(user_id=obj.user_id).first_name

    def last_name(self, obj):
        return Profile.objects.get(user_id=obj.user_id).last_name

    def match_first_name(self, obj):
        return Profile.objects.get(user_id=obj.match_id).first_name

    def match_last_name(self, obj):
        return Profile.objects.get(user_id=obj.match_id).last_name
    



admin.site.register(Matches, MatchesAdmin)

