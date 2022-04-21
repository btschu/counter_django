from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_two', views.add_two),
    path('destroy_session', views.destroy_session),
    path('increase_by_amount', views.increase_by_amount),
]