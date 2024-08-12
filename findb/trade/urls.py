from django.urls import path
from . import views

urlpatterns = [
    path('', views.trade_view, name='trade_view'),
]