from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('sign_in/', views.sign_in),
    path('sign_up_dater/', views.sign_up),
    path('sign_up_cupid/', views.sign_up),
    path('logout/', views.logout_view),
]
