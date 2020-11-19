from django.urls import path, include
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserListView,
	# CommentCreateView,
)

urlpatterns = [
	path('', PostListView.as_view(), name='index'),
	path('user/<str:username>', UserListView.as_view(), name='user-posts'),
	path('post/<int:pk>', PostDetailView.as_view(), name='detail'),
	path('post/create', PostCreateView.as_view(), name='create'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
	path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
	path('post/', include('post_likes.urls')),
	path('post/', include('comment_likes.urls')),

	# path('post/<int:pk>/createcomment', CommentCreateView.as_view(), name='comment_create'),
	# path('post/<int:pk>/comment/', views.create_comment, name='create_comment'),

	# path('post/<int:pk>/create', CommentCreateView.as_view(), name='createcomment'),
]