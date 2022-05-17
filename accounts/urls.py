
from django.urls import path
from .views import SignUpView

urlpattern = [
    path('signup/', SignupView.as_view(), name='signup')
]