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


def verify_token(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_account = payload['account']
        user = User.objects.get(account=user_account)
    except IndexError:
        return False, Response({'error': 'Missing JWT token'}, status=401)
    except jwt.ExpiredSignatureError:
        return False, Response({'error': 'Token has expired'}, status=401)
    except jwt.InvalidTokenError:
        return False, Response({'error': 'Invalid token'}, status=401)
    except User.DoesNotExist:
        return False, Response({'error': 'Invalid credentials'}, status=400)
    return True, user

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
        is_valid, response = verify_token(request)
        if not is_valid:
            return response
        try:
            article = Article.objects.get(pk = pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=404)
        
    def post(self, request):
        is_valid, response = verify_token(request)
        if not is_valid:
            return response
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        is_valid, response = verify_token(request)
        if not is_valid:
            return response
        try:
            article = Article.objects.get(pk = pk)
            serializer = ArticleSerializer(article, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = 400)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=404)
    
    def delete(self, request, pk):
        is_valid, response = verify_token(request)
        if not is_valid:
            return response
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response(status = 204)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=404)