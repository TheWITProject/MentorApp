from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from match.models import *
#
# class MatchesAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Hero)
class MatchesAdmin(admin.ModelAdmin):
    change_list_template = "templates/buttons.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.set_immortal),
            path('mortal/', self.set_mortal),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        self.model.objects.all().update(is_immortal=True)
        self.message_user(request, "All heroes are now immortal")
        return HttpResponseRedirect("../")

    def set_mortal(self, request):
        self.model.objects.all().update(is_immortal=False)
        self.message_user(request, "All heroes are now mortal")
        return HttpResponseRedirect("../")

admin.site.register(Matches, MatchesAdmin)
