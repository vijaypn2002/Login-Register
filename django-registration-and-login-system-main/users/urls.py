from django.urls import path,include
from .views import home, profile, RegisterView

urlpatterns = [
    path('auth/',include('social_django.urls', namespace='social')),
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
   
]
