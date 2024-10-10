from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('confirm/', views.confirm_selection, name='confirm_selection'),
]
