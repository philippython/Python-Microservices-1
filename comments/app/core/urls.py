from django.urls import path
from .views import CommentAPIView, PostCommentView

urlpatterns = [
    path('posts/<str:pk>/comments', PostCommentView.as_view()),
    path('comments', CommentAPIView.as_view(), name='all_comments')
]