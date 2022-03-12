from django.urls import path
from .views import (
    IslandCreateView,CashingView
)
app_name = 'heiwa'

urlpatterns = [
    path('create/', IslandCreateView.as_view(),name='create'),
    path('cashing/',CashingView.as_view(),name='cashing')
]