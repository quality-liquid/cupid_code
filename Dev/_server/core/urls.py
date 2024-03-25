from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('get_img/', view=views.get_image, name='get_image'),
    path('get_menu/', view=views.get_menu, name='get_icon'),
    path('get_mic/', view=views.get_mic, name='get_icon'),
    path('get_mic_off/', view=views.get_mic_off, name='get_icon'),
    path('get_chat/', view=views.get_chat, name='get_icon'),
    path('get_money/', view=views.get_money, name='get_icon'),
    path('get_emergency/', view=views.get_emergency, name='get_icon'),
    path('get_temp_pfp/', view=views.get_temp_pfp, name='get_icon'),
    path('logout/', view=views.logout_view, name='logout')
]
