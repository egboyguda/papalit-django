from django.urls import path
from . import views

urlpatterns = [
    path('seller/',views.dashBoard,name='dashboard'), # type: ignore
]
