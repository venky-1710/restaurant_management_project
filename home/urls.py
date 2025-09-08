
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



from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),   # homepage
    path('menu/', views.menu, name='menu'),  # menu page
    path('about/', views.about, name='about'),  # about page
    path('faq/', views.faq, name='faq'),        # FAQ page
    path('privacy/', views.privacy, name='privacy'),  # Privacy Policy
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),  # Order confirmation
    path('login/', views.user_login, name='login'),  # login page
    path('order/',views.order_page, name='order_page'),
]

