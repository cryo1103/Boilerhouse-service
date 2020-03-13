from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name = 'índex'),
    path('application/', views.test, name = 'application'),

]