from .serializers import CommentSerializers
from .models import Comment
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class PostCommentView(APIView):
    def get(self, _, pk):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializers(comments, many=True)
        return Response(serializer.data)


class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

