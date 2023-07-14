from rest_framework import serializers
from .models import Article

# 將Article model裡的資料轉換成JSON格式
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'