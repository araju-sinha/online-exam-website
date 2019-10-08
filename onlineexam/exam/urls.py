from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainviewpage.as_view(), name='main' ),
    path('home/', views.homeviewpage.as_view(), name='home'),
    path('about/', views.aboutviewpage.as_view(), name='about'),
    path('contact/', views.contactviewpage.as_view(), name='contact'),

]
