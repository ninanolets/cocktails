from django.urls import path
from . import views

urlpatterns = [
	path('<int:pk>/comment_like/<int:comment_pk>', views.comment_like, name='comment_like'), 
]