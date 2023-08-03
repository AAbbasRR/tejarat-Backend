from django.urls import path

from .views import *

app_name = 'app_store'
urlpatterns = [
    path('psp/', ListCreatePSPView.as_view(), name='list_create_psp'),
    path('psp/<int:pk>/', DetailUpdateDeletePSPView.as_view(), name='detail_update_delete_psp'),
    path('psp/all/', AllListPSPView.as_view(), name='list_all_psp'),

    path('machines/', ListCreateMachineView.as_view(), name='list_create_machine'),
    path('machines/<int:pk>/', DetailUpdateDeleteMachineView.as_view(), name='detail_update_delete_machine'),
]
