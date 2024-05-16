from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginForm,name='login'),
    path('logout/',views.logoutUser,name='logout'),
]
