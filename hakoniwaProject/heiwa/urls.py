from django.urls import path
from .views import (
    IslandCreateView,CashingView,IslandReadView,
    DevelopmentView,
)
app_name = 'heiwa'

urlpatterns = [
    path('create/', IslandCreateView.as_view(),name='create'),
    path('cashing/',CashingView.as_view(),name='cashing'),
    path('island-read/',IslandReadView.as_view(),name='island-read'),
    path('development/',DevelopmentView.as_view(),name='development'),

]