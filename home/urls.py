
# from django.urls import path
# from . import views
# from .views import MenuAPIView

# urlpatterns = [
#     path('', views.homepage, name='homepage'),
#     path('menu/', MenuAPIView.as_view(), name='menu'),
#     path('about/', views.about_page, name='about'),
#     path('menu-list/', views.menu_list, name='menu_list'),
#     path('feedback/', views.feedback_view, name='feedback'),
#     path('feedback-success/', views.feedback_success_view, name='feedback_success'),
#     path("contact/",views.contact_view, name="contact"),
# ]



from django.urls import path   # ✅ import path
from . import views            # ✅ import views from current app

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/',views.about, name='about'),
]





