from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('sign_in/', view=views.sign_in),
    path('get_img/', view=views.get_image)
]
