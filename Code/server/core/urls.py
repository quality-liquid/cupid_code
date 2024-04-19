from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('get_img/', view=views.get_image, name='get_image'),
    path('get_graph/', view=views.get_graph, name='get_graph'),
    path('logout/', view=views.logout_view, name='logout')
]
