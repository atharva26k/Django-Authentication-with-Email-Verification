from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('about/', views.about, name='about'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
