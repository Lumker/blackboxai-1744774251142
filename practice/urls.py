from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clients/', views.client_list, name='client_list'),
    path('cases/', views.case_list, name='case_list'),
    path('cases/<int:pk>/', views.case_detail, name='case_detail'),
    path('appointments/', views.appointment_calendar, name='appointment_calendar'),
    path('billings/', views.billing_list, name='billing_list'),
]
