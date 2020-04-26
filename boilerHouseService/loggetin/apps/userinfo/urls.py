from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='índex'),
    path('application/', views.application, name='application'),
    path('calc/', views.calc, name='calc'),

]


