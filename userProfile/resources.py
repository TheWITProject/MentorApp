from import_export import resources
from .models import Profile


class ProfileExport(resources.ModelResource):
    class Meta:
        model = Profile