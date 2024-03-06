from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('get_img/', view=views.get_image, name='get_image'),
    path('get_icon/', view=views.get_icon, name='get_icon'),
    path('logout/', view=views.logout_view, name='logout')
]
