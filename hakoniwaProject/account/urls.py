from django.urls import path
from .views import (
    LoginView,YesView,AccountCreateView,
    AccountReadView,AccountListView,AccountUpdateView,
    AccountDeleteView,
)
app_name = 'account'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('yes/',YesView.as_view(),name='yes'),
    path('create/',AccountCreateView.as_view(),name='create'),
    path('read/',AccountReadView.as_view(),name='read'),
    path('list/',AccountListView.as_view(),name='list'),
    path('update/',AccountUpdateView.as_view(),name='update'),
    path('delete/',AccountDeleteView.as_view(),name='deletes'),
]