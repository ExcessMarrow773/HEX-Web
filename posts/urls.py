from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.makePost, name="createPost"),
    path('<int:pk>/', views.post_details, name="post_details"),
	path('', views.viewPostIndex, name="postIndex")
]