from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',MenuAPIView.as_view(),name='menu'),
    path('about/',views.about_page, name='about'),
]