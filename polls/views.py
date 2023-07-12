from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer

class ArticleView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
    
