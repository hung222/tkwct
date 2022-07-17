from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drm2', views.drm2, name='drm2'),
]
