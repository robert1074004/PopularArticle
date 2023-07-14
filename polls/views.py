from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article, User
from .serializer import ArticleSerializer
from django.contrib.auth.hashers import check_password
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

class UserLoginView(APIView):
    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        user = User.objects.get(account=account)
        password_matched = check_password(password, user.password)
        if not user or not password_matched:
            return Response({'error': 'Invalid credentials'}, status=400)
        payload = {'account': user.account, 'exp': (datetime.utcnow() + timedelta(days=7))}
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return Response({'token': token})

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

    def put(self, request, pk):
        article = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
    
    def delete(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status = 204)