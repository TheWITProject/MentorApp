from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.http import HttpResponseRedirect
from match.models import *
from .serializers import MatchesSerializer
from django.http import HttpResponse

import requests
import pandas as pd
import json
import os
import csv

class MatchesAdmin(admin.ModelAdmin):
    change_list_template = "admin/matches/buttons.html"
    list_display = ("user_id", "puser")
    actions = ['export_matches']
    

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('makematches/', self.make_matches),
            # path('download/', self.export_matches),
        ]
        return my_urls + urls

    def make_matches(self, request):
        r = requests.get('http://127.0.0.1:8000/survey/json/5')
        r.json()
        print(os.getcwd())
        # x = requests.post('http://127.0.0.1:8000/api/v1/mlalgorithmstatuses', json = r.json())
       
        mock_json = pd.read_json('/Users/student/MentorApp/match/mock.json', orient = 'records')
        print(mock_json)
        dict_json = mock_json.to_dict('records')
        # mock_json = x.to_json
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
        writer.writerow(["user_id", "match_id"])

        for s in queryset:
            writer.writerow([s.user_id, s.match_id])
        
        f.close()
        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = matches.csv'
        self.message_user(request, "Matches have been downloaded")

        return response
        # return HttpResponseRedirect("../")
    



admin.site.register(Matches, MatchesAdmin)

