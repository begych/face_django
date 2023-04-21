from django.urls import path

from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('home_page/', HomePage, name="home_page"),
    path('register/', register, name='register'),
    path('login/', admin_login, name='login'),
    path('data_change/<str:slug>/', DataChangeView.as_view(), name='data_change'),
    path('person/<slug:slug>/', PersonView.as_view(), name='person'),
    path('delete/<str:slug>/', PersonDeleteView.as_view(), name='delete'),
    path('logout/', admin_logout, name='logout'),
    path('camera/', livefe, name="live_camera"),
    path('camera_2/', livefe_2, name="live_camera_2"),
    # path('get_face/', get_picture, name='get_picture')
   ]
handler404 = 'face.views.error_404'
handler500 = 'face.views.error_500'
handler403 = 'face.views.error_403'
handler400 = 'face.views.error_400'
