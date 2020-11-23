from django.urls import path
from . import views

urlpatterns = [
	path('<int:pk>/delete_comment/<int:pk_comment>', views.delete_comment, name='delete_comment'),
]