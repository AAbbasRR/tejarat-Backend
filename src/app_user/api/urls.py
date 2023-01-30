from django.urls import path

from .views import *

app_name = 'app_user'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
]
