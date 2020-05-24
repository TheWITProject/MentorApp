"""mentorapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from userProfile import views
from django.conf.urls import include, url


from django.conf.urls.static import static
from django.conf import settings

# from ml_endpoints.urls import urlpatterns as endpoints_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login' ),
    path('logout/', views.logout_view , name="logout"),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('faq/', views.faq_page, name='faq' ),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordReset/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='passwordReset/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordReset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwordReset/password_reset_form.html'), name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordReset/password_reset_complete.html'),
     name='password_reset_complete'),

    path("survey/", include("survey.urls")),

    path('nested_admin/', include('nested_admin.urls')),
    # path(r"^api/v1/", include('router.urls')),
    # path(r"^api/v1/", include('ml_endpoints.urls'))
    path('', include('ml_endpoints.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += endpoints_urlpatterns
