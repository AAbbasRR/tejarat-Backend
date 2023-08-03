from django.urls import path

from .views import *

app_name = 'app_user'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),

    path('users/', ListCreateUserView.as_view(), name='list_create_users'),
    path('users/<int:pk>/', DetailUpdateDeleteUserView.as_view(), name='detail_update_delete_users'),
]
