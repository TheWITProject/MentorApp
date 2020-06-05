from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.http import HttpResponseRedirect
from match.models import *
#
# class MatchesAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Hero)
class MatchesAdmin(admin.ModelAdmin):
    change_list_template = "admin/matches/buttons.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('makematches/', self.make_matches),
            path('download/', self.export_matches),
        ]
        return my_urls + urls

    def make_matches(self, request):
        self.message_user(request, "Matches have been made")
        return HttpResponseRedirect("../")

    def export_matches(self, request):
        self.message_user(request, "Matches have been downloaded")
        return HttpResponseRedirect("../")


admin.site.register(Matches, MatchesAdmin)
