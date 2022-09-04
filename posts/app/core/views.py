import requests
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
# Create your views here.

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response([self.format(post) for post in posts])

    
    def format(self, post):
        formatted = requests.get('http://localhost:8001/api/posts/%d/comments' % post.id).json()
        return {
            "id": post.id,
            "title": post.title,
            "description": post.description,
            "comments": formatted
        }

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)