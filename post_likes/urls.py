from django.urls import path
from . import views

urlpatterns = [
	path('<int:pk>/post_like', views.post_like, name='post_like'), 
]