from django.urls import path
from . import views
from .views import AddCommentView, EditCommentView, DeleteCommentView


urlpatterns = [
    path('', views.index, name='index'),         # root URL now shows home page
    path('learn/', views.index1, name='index1'),
    path('pst/', views.index2, name='index2'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('post/<int:post_id>/comment/add/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/',DeleteCommentView.as_view(), name='delete_comment'),
]
