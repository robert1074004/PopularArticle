from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)