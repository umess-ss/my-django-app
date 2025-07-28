from django.urls import path
from .views import ListPosts,PostDetails


urlpatterns = [
#     path('', views.api_index, name="api_home"),
    # path('posts/', views.get_all_posts, name="posts_get_api"),
    path('posts/', ListPosts.as_view(), name="posts_list_create_api"), 
    path('posts/slug', PostDetails.as_view(), name="posts_detail_create_api"), 
]