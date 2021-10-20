from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="public-index"),
	path('login', views.login, name="public-login"),
]